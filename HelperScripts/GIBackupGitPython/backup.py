import requests
import os
import pathlib
import git
import zipfile
import json
import backup_utils
from multiprocessing.pool import ThreadPool
from dotenv import load_dotenv
load_dotenv()

# Ghostinspector API
GI_API_KEY = os.getenv("GI_API_KEY")
GIT_AUTHOR = os.getenv("GIT_AUTHOR")

cwd = os.getcwd()
_git = git.cmd.Git(cwd)
repo = git.Repo()

_git.pull()

# test = os.listdir(cwd)
# for item in test:
#     if item.endswith(".zip"):
#         path = os.path.join(cwd, item)
#         repo.index.remove([path],working_tree = True)
BACKUPS_DIR = os.path.join(cwd,'backups')
if not os.path.exists(BACKUPS_DIR):
    os.makedirs(BACKUPS_DIR)
#add_names = []
try:
    existing = backup_utils.listdir_nohidden(BACKUPS_DIR)
    if len(existing):
        for ex in existing:
            try:
                repo.index.remove([os.path.join(BACKUPS_DIR,ex)],working_tree = True,r=True)
            except Exception as e:
                print(e)
except Exception as e:
    print(f"warning {e}")

list_suites_resp = requests.get(f"https://api.ghostinspector.com/v1/suites/?apiKey={GI_API_KEY}")

def backup_suite(s):
    resp = requests.get(f"https://api.ghostinspector.com/v1/suites/{s['_id']}/export/json/?apiKey={GI_API_KEY}", stream=True)
    name = f"{s['_id']}_{s['name']}"
    name = backup_utils.clean_filename(name)
    zname = os.path.join(BACKUPS_DIR,f"{name}.zip")
    zfile = open(zname, 'wb')
    zfile.write(resp.content)
    zfile.close()
    #add_names.append(zname)
    return zname

results = ThreadPool(8).imap_unordered(backup_suite, list_suites_resp.json()['data'])
for zname in results:
    OUTPUT_DIR = os.path.join(BACKUPS_DIR,str.replace(zname,'.zip',''))

    with zipfile.ZipFile(zname,"r") as zip_ref:
        print(f"unzipping {zname} to {OUTPUT_DIR}")
        zip_ref.extractall(OUTPUT_DIR)
        zip_ref.close()

    try:
        json_files = [pos_json for pos_json in os.listdir(OUTPUT_DIR) if pos_json.endswith('.json')]
        for json_file in json_files:
            ss = ''
            JSON_FILE = os.path.join(OUTPUT_DIR,json_file)
            with open(JSON_FILE, 'r') as f:
                for line in f:
                    ss += ''.join(line.strip())
            data = json.loads(ss)
            with open(JSON_FILE, 'w') as outfile:
                json.dump(data, outfile, sort_keys=False, indent=4)
            cleaned_name = f"{backup_utils.clean_filename(json_file.rsplit('.',1)[0])}.json"
            #print(json_file,cleaned_name)
            os.rename(
                JSON_FILE,
                os.path.join(OUTPUT_DIR,cleaned_name)
            )
    except Exception as e:
        print(e)
    # delete .zip
    os.remove(zname)


#repo.index.add(add_names)
repo.index.add(BACKUPS_DIR)
repo.index.add('backup.py') # add THIS script! :D :P
try:
    print(_git.status())
    _git.commit('-m', 'GhostInspector Automated Backup', author=GIT_AUTHOR)
    _git.push('origin', 'master')
    pass
except Exception as e:
    print(f"warning - {e}")
else:
    print("success")
