<a id="markdown-ghost-inspector-helper-scripts--importable-testing-utilities" name="ghost-inspector-helper-scripts--importable-testing-utilities"></a>
# Ghost Inspector Helper Scripts & Importable Testing Utilities

Here's a few of my Ghost Inspector Helper Scripts & Importable Testing Utilities someone else may find useful. I'll add more in the future. Follow me [@jakedowns on Twitter](https://twitter.com/jakedowns) for more info!

<!-- TOC -->

- [Ghost Inspector Helper Scripts & Importable Testing Utilities](#ghost-inspector-helper-scripts--importable-testing-utilities)
    - [Importable Testing Utilities](#importable-testing-utilities)
        - [1. _Ghost Inspector wait for Emails to arrive in ___email.ghostinspector.com___ inbox_](#1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_)
            - [A. Definition of ___Importables - GIEmail Wait For Emails to Arrive With Subjects___:](#a-definition-of-___importables---giemail-wait-for-emails-to-arrive-with-subjects___)
            - [B. Definition of ___Importables - GIEmail Assert Subjects in DOM___](#b-definition-of-___importables---giemail-assert-subjects-in-dom___)
        - [2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_](#2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_)
    - [Helper Scripts](#helper-scripts)
        - [1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_](#1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_)

<!-- /TOC -->

Gists:
[Example of How to Programmatically Update EasyMDE/CodeMirror/Simple Editor Input Value for Integration & Acceptance Testing](https://gist.github.com/jakedowns/b3f9a90de1182af083024e037e3ac42f)

---

<a id="markdown-importable-testing-utilities" name="importable-testing-utilities"></a>
## Importable Testing Utilities

<a id="markdown-1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_" name="1-_ghost-inspector-wait-for-emails-to-arrive-in-___emailghostinspectorcom___-inbox_"></a>
### 1. _Ghost Inspector wait for Emails to arrive in ___email.ghostinspector.com___ inbox_

> [WaitForEmails.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/WaitForEmails.md)

---
<a id="markdown-2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_" name="2-_ghost-inspector-test-email-subject-is-present-in-__mailtrapio__-inbox_"></a>
### 2. _Ghost Inspector Test Email Subject is present in __Mailtrap.io__ Inbox_
---

1. set a `mailtrap_assert_subject` to a string Subject you want to check has arrived
2. directly execute or import the following implementation:
- NOTE: this could be adapted to use the repeatable Promise-based looping approach above, it could also be adapted to check for an array of subjects rather than just a single string.

---
- Step 1. **Go to URL** `https://mailtrap.io/api/v1/inboxes/{{inboxId}}/messages?search={{userEmail}}&api_token={{mailtrapAPI_Token}}`
- Step 2. **Javascript returns True**
```js
let emails_array = JSON.parse(document.body.innerText);
console.log('debug emails array ' + document.body.innerText);
let subject_matches = [];
emails_array.map((v,k)=>{
    console.log("debug compare subject", v.subject);
	if(v.subject.toLowerCase().indexOf("{{mailtrap_assert_subject}}".toLowerCase()) > -1){
		subject_matches.push(k);
	}
});
console.log("debug subject matches",JSON.stringify({subject_matches, searching:"{{mailtrap_assert_subject}}"}));
return subject_matches.length > 0;
```
---
<a id="markdown-helper-scripts" name="helper-scripts"></a>
## Helper Scripts
<a id="markdown-1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_" name="1-_python-script-to-backup-all-ghost-inspector-suite-data-exported-as-zipped-json-data-and-automatically-push-it-to-a-github-repo_"></a>
### 1. _Python Script to backup all Ghost Inspector Suite Data (Exported as Zipped JSON data) and automatically push it to a github repo_
See the script in this repo: [backup-all-suites-to-git.py](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/backup-all-suites-to-git.py)

It downloads all of your GhostInspector Suites as zipped json files, then automatically commits and pushes to `master` branch of whatever Git Repository it is nestled within. You just need to find a way to trigger the script to run periodically. Or even better, a Chrome Extension which triggers it each time you hit Save on a Test's "Edit Steps" page (stay tuned for more on that)
