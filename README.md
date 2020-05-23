# Ghost Inspector Helper Scripts & Importable Testing Utilities

Here's a few of my Ghost Inspector Helper Scripts & Importable Testing Utilities someone else may find useful. I'll add more in the future. Follow me [@jakedowns on Twitter](https://twitter.com/jakedowns) for more info!

<!-- TOC -->

- [Ghost Inspector Helper Scripts & Importable Testing Utilities](#ghost-inspector-helper-scripts--importable-testing-utilities)
  - [Importable Testing Utilities](#importable-testing-utilities)
    - [1. _Ghost Inspector Email Service wait for Emails to arrive in ___email.ghostinspector.com___ inbox_](#1-ghost-inspector-email-service-wait-for-emails-to-arrive-in-emailghostinspectorcom-inbox)
    - [2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_](#2-ghost-inspector-test-email-subject-is-present-in-mailtrapio-inbox)
    - [3. Javascript Eventually Returns True](#3-javascript-eventually-returns-true)
    - [4. wait_for_element_selector to be present](#4-waitforelementselector-to-be-present)
    - [5. Test Guard Exit Early](#5-test-guard-exit-early)
    - [6. Setup Shared Test - Custom Environment-based variables ENVVARS depending on startUrl](#6-setup-shared-test---custom-environment-based-variables-envvars-depending-on-starturl)
  - [Helper Scripts](#helper-scripts)
    - [1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_](#1-python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo)

<!-- /TOC -->


Gists:
- [Example of How to Programmatically Update Easy MarkDown Editor / CodeMirror / Simple Editor Input Value for Integration & Acceptance Testing](https://gist.github.com/jakedowns/b3f9a90de1182af083024e037e3ac42f)

---

## Importable Testing Utilities

How to use: 
- You could _technically_ import as many of these Helper Tests using the .json files in the [ImportableTestingUtilities](ImportableTestingUtilities) folder. I'd import them them in a fresh "Importables" Suite. Using the instructions here: [https://ghostinspector.com/docs/selenium-import-export/#import-json]()
    - unfortunately, this import method must be done one test at a time, and it requires you to stub in the tests by hand first, then update the IDs in the JSON files to match your new destination stubs. 
        - __I'll look into altering my `backup.py` script to support exporting the more easily importable "Selenium IDE v1" format soon__ 
        - I'll also be looking into creating an `import.py` script to help with this process
- for now, the better way (altho slower?) way, would probably be to go through the Readme's here: [https://github.com/jakedowns/ghost-inspector-helpers/tree/master/readmes]() and see which helpers you'd like to try, then recreate them yourself using the documented steps. LMK if you run into any issues. Happy to help.


### 1. _Ghost Inspector Email Service wait for Emails to arrive in ___email.ghostinspector.com___ inbox_

A helper that will keep checking for a set of email subjects to be present in a particular email.ghostinspector.com inbox

View Readme: [readmes/WaitForEmails.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/WaitForEmails.md)

### 2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_

A helper that will keep checking Mailtrap.io api for the existence of an email with a particular subject line until time runs out. (could easily be modified to wait for multiple email subjects to be present)

View Readme: [readmes/WaitForEmailMailtrap_io.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/WaitForEmailMailtrap_io.md)

### 3. Javascript Eventually Returns True

A helper that will continually execute a bit of javascript until it returns true or time runs out (Ns -> 60s -> 10min depending on your setup)

View Readme: [readmes/javascript_eventually_returns_true.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/javascript_eventually_returns_true.md)

### 4. wait_for_element_selector to be present

A helper that will continually check for the existence of at least one element matching a querySelector until time runs out (Ns -> 60s -> 10min depending on your setup)

View Readme: [readmes/wait_for_element_selector.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_for_element_selector.md)

### 5. Test Guard Exit Early

A small ghost inspector test helper that will allow you to "Guard" a test shared between multiple environments, that will only execute if the current url matches a specific sub string, otherwise the text will Exit early with a Passing status.

View Readme: [readmes/TestGuardExitEarly.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/TestGuardExitEarly.md)

### 6. Setup Shared Test - Custom Environment-based variables ENVVARS depending on startUrl

A small ghost inspector test helper that one can include at the top of each in a suite of shared tests, it sets up an object full of environemnt variables and then exposes them for other tests to use. It is conditional and idempotent (knows to only execute once), just in case it gets included multiple times

View Readme: [readmes/SetupSharedTest.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/SetupSharedTest.md)

---
## Helper Scripts

TODOS:
- create an import.py script for importing from backups

### 1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_
See the script in this repo: [HelperScripts/GIBackupGitPython/backup.py](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/HelperScripts/GIBackupGitPython/backup.py)

Known Issues / Todos:
- Support option to export in Selenium IDE v1 format

Usage:

- Download the GIBackupGitPython folder into an existing git repo you use, or into a fresh git repo, or fork this repo. 
- copy the `.env.example` file to a new (gitignored) `.env` file and add your GhostInspector api key: `GI_API_KEY` and `GIT_AUTHOR` to define who the commits will be committed as
- cd into the directory in a terminal and run `pip install requirements.txt` (I've only tested with Python3, your mileage may vary, you may need to install deps by hand)
- run `python backup.py` or `python3 backup.py` depending on your setup
- NOTE try commenting out the 'commit' and 'push' lines in `backup.py` if you want to dry run test things first

The script:
- downloads all of your GhostInspector Suites as zipped JSON files, 
- extracts them & deletes the now extraneous .zip files
- formats the JSON files (_**pretty prints**_ with newlines and indentation) 
- automatically commits and pushes to `master` branch of whatever Git Repository it is nestled within. 

For "automated" backups, you just need to find a way to trigger the script to run periodically.
Using a cron-job or some other automated method. Maybe even a Scheduled GI test that hits an api to trigger the script to run on a server you own. 
I also imagine it'd be cool to have a Chrome Extension which triggers it each time you hit Save on a Test's "Edit Steps" page (stay tuned for more on that)
