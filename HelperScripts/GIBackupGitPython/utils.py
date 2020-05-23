"""
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""
import unicodedata
import string

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
char_limit = 255

def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    # replace spaces
    # for r in replace:
    #     filename = filename.replace(r,'_')

    # whitespace
    cleaned_filename = re.sub(' +', '_', filename)

    # rm parens
    table = str.maketrans(dict.fromkeys("()"))
    cleaned_filename = cleaned_filename.translate(table)# = re.sub(r" ?\([^)]+\)", "", cleaned_filename)

    # keep only valid ascii chars
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # dots to _
    cleaned_filename = cleaned_filename.replace('.','_')

    # alpha numeric and underscores only
    cleaned_filename = re.sub(r'[^A-Za-z0-9_]+', '', cleaned_filename)

    # double _ to single?

    # keep only whitelisted chars
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename)>char_limit:
        print("Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
    return cleaned_filename[:char_limit]
"""
END GIST
"""

def listdir_nohidden(path):
    return [f for f in os.listdir(path) if not f.startswith('.')]