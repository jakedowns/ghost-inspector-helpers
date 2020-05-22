<a id="markdown-ghost-inspector-helper-scripts--importable-testing-utilities" name="ghost-inspector-helper-scripts--importable-testing-utilities"></a>
# Ghost Inspector Helper Scripts & Importable Testing Utilities

Here's a few of my Ghost Inspector Helper Scripts & Importable Testing Utilities someone else may find useful. I'll add more in the future. Follow me [@jakedowns on Twitter](https://twitter.com/jakedowns) for more info!

<!-- TOC -->

- [Ghost Inspector Helper Scripts & Importable Testing Utilities](#ghost-inspector-helper-scripts--importable-testing-utilities)
    - [Importable Testing Utilities](#importable-testing-utilities)
        - [1. _Ghost Inspector wait for Emails to arrive in ___email.ghostinspector.com___ inbox_](#1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_)
        - [2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_](#2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_)
    - [Helper Scripts](#helper-scripts)
        - [1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_](#1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_)

<!-- /TOC -->

Gists:
- [Example of How to Programmatically Update Easy MarkDown Editor / CodeMirror / Simple Editor Input Value for Integration & Acceptance Testing](https://gist.github.com/jakedowns/b3f9a90de1182af083024e037e3ac42f)

---

<a id="markdown-importable-testing-utilities" name="importable-testing-utilities"></a>
## Importable Testing Utilities

<a id="markdown-1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_" name="1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_"></a>
### 1. _Ghost Inspector Email Service wait for Emails to arrive in ___email.ghostinspector.com___ inbox_

A helper that will keep checking for a set of email subjects to be present in a particular email.ghostinspector.com inbox

View Readme: [WaitForEmails.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/WaitForEmails.md)

<a id="markdown-2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_" name="2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_"></a>
### 2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_

A helper that will keep checking Mailtrap.io api for the existence of an email with a particular subject line until time runs out. (could easily be modified to wait for multiple email subjects to be present)

View Readme: [WaitForEmailMailtrap_io.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/WaitForEmailMailtrap_io.md)

### 3. Javascript Eventually Returns True

A helper that will continually execute a bit of javascript until it returns true or time runs out (Ns -> 60s -> 10min depending on your setup)

View Readme: [javascript_eventually_returns_true.md](javascript_eventually_returns_true.md)

### 4. wait_for_element_selector to be present
View Readme: [wait_for_element_selector.md](wait_for_element_selector.md)

A helper that will continually check for the existence of at least one element matching a querySelector until time runs out (Ns -> 60s -> 10min depending on your setup)

---
<a id="markdown-helper-scripts" name="helper-scripts"></a>
## Helper Scripts
<a id="markdown-1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_" name="1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_"></a>
### 1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_
See the script in this repo: [backup-all-suites-to-git.py](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/backup-all-suites-to-git.py)

It downloads all of your GhostInspector Suites as zipped json files, then automatically commits and pushes to `master` branch of whatever Git Repository it is nestled within. You just need to find a way to trigger the script to run periodically. Or even better, a Chrome Extension which triggers it each time you hit Save on a Test's "Edit Steps" page (stay tuned for more on that)
