import requests
import os
from multiprocessing.pool import ThreadPool
import git

# call this script periodically to automatically keep backups of changes to your GhostInspector changes

cwd = os.getcwd()
g = git.cmd.Git(cwd)

g.pull

API_KEY = "XXX"

r = requests.get(f"https://api.ghostinspector.com/v1/suites/?apiKey={API_KEY}")

def backup_suite(s):
    resp = requests.get(f"https://api.ghostinspector.com/v1/suites/{s['_id']}/export/json/?apiKey={API_KEY}", stream=True)
    name = f"{s['_id']}-{s['name']}"
    zname = os.path.join(f"{name}.zip")
    zfile = open(zname, 'wb')
    zfile.write(resp.content)
    zfile.close()
    return name

results = ThreadPool(8).imap_unordered(backup_suite, r.json()['data'])
for id in results:
    print(id)

r = git.Repo()
r.git.add(u=True)

r.git.commit('-m', 'GhostInspector Automated Backup', author='Utility Server <utility-server@domain.com>')

r.git.push('origin', 'master')