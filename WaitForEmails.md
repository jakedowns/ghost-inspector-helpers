### 1. _Ghost Inspector wait for Emails to arrive in ___email.ghostinspector.com___ inbox_

This answers questions I had like:
- What to do if my Ghost Inspector Test Fails because Emails haven't arrived yet? or Multiple Emails haven't all arrived yet?
- How can I check for emails in a more performant manner than just adding arbitrary pauses into my Tests?
    Sometimes emails will arrive faster than other times, doesn't make sense to wait for a hard-coded amount of time each test run. How can we dynamically wait until *just* the exact moment (+/- some # of milliseconds) when the email arrives?
- How can I create a loop that checks `mail.ghostinspector.com` inbox until my email arrives / all my expected emails arrive?
- How can I uses Promises to dynamically extend the length of a Ghost Inspector test?

---

**Original Usage:** In my experience, sometimes **Mailgun** can be slow to deliver emails to email.ghostinspector.com I kept having to add 30second pauses to my tests, and it seems like every now and then I'd still have tests failing. I knew sometimes emails were coming in faster than the lowest common denomentator and I didn't want to continue to extend the length of _every_ test run that interacted with emails (which is a large portion of my tests) so, I wrote this couplet of Importable Test modules which use Javascript Promises to loop & repeatedly check the mailbox index page for the presence of an Array of Subject Names. __It will only pass once all Subject Names Expected are delivered and present.__

> **Note:** this test intentionally DOES NOT check that emails arrive in a certain order since emails can arrive out of order for various reasons.

> **Note:** you can import these tests from the **ImportableTestingUtilites** directory of this repo, but you'll still have to re-link the Import steps manually.

---
<a id="markdown-a-definition-of-___importables---giemail-wait-for-emails-to-arrive-with-subjects___" name="a-definition-of-___importables---giemail-wait-for-emails-to-arrive-with-subjects___"></a>
#### A. Definition of ___Importables - GIEmail Wait For Emails to Arrive With Subjects___:
---
> Step 1. MUST set a `giemail_assert_emails_arrived_with_subjects` variable that is an array of string subjects for us to check first! e.g. `['Email Subject 1', 'Email Subject 2']`
1. **Javascript Returns True**
```js
let subjects = {{giemail_assert_emails_arrived_with_subjects}};
return subjects.length > 0;
```
> Step 2. Lowercase the asserted subject names for easier matching. **Omit this if you want your test to be case-sensitive**
2. **Extract From Javascript** `giemail_assert_emails_arrived_with_subjects` =
```js
let subjects = {{giemail_assert_emails_arrived_with_subjects}};
subjects = subjects.map(function(v){
    return v.toLowerCase();
});
return subjects;
```
3. **Go to URL** `http://email.ghostinspector.com/{{userEmail}}`
4. **Set Variable** `giemail_all_subject_assertions_passing` = `false` # completion flag
5. **Set Variable** `time_to_email_start` = `{{timestamp}}` # for time-tracking
> Step 6.
>
> repeat this one for as long as you need. by default each import will check every 500ms for the max per-step execution time: **60s**
>
> keep in mind the max Test execution time for GI **Tests are hard-limited to 10 minutes**.
>
> In my case I've added 3 instances so it checks for up to 3 minutes
1. (8. & 9.) **Import Steps From** `Importables - GIEmail Assert Subjects in DOM`  # see definition `B.` below
> Step 10. Time tracking report if you're interested
10. **Execute Javascript**
```js
console.log("time to email end " + ({{timestamp}} - {{time_to_email_start}}));
```
>Step 10. condition
```js
return "{{giemail_all_subject_assertions_passing}}" == "true"
```
> Step 11. Assert all subjects were found and flag the test as passing! :D
11. **Javascript Returns True**
```js
return "{{giemail_all_subject_assertions_passing}}" == "true"
```

---

<a id="markdown-b-definition-of-___importables---giemail-assert-subjects-in-dom___" name="b-definition-of-___importables---giemail-assert-subjects-in-dom___"></a>
#### B. Definition of ___Importables - GIEmail Assert Subjects in DOM___
---
> *!!! Add this Condition for **ALL** of following of steps:*
```js
return "{{giemail_all_subject_assertions_passing}}" !== "true"; /* only check subjects if all asserts are not yet passing. */
```

> Step 1. Could alter this delay as you see fit... it could also just be removed
1. **Pause** `3000`
1. **Refresh** # refresh the mailbox index page
1. **Extract from Javascript** `subjects_in_dom` =
```js
var subjects_in_dom = Array.from(document.getElementsByClassName('subject')).map(function(v){
    return v.textContent.toLowerCase(); // remove this bit, or make it conditional based on a variable if you want case-sensitive matching
});
try{
    console.log('subjects in dom?',JSON.stringify(subjects_in_dom));
}catch(e){
    console.error(e);
}
return subjects_in_dom || [];
```
> Step. 4 keeps checking every 500ms for 60s. alter as you see fit.
4. **Extract from Javascript** `giemail_all_subject_assertions_passing` =
```js
return new Promise((resolve,reject)=>{
    function checkForEmails(){
        var assertions = [];
        var subject_assertions = {{giemail_assert_emails_arrived_with_subjects}};
        var subjects_in_dom = {{subjects_in_dom}};

        for(var i=0; i<subject_assertions.length; i++){
            // TODO swap these comments or add a conditional variable switch if you want full string matching vs. partial string matching

            // [DISABLED] Exact String Matching
            //assertions.push(subjects_in_dom.indexOf(subject_assertions[i]) >-1)

            // [ENABLED] Partial String Matching
            let found = false;
            for(var j=0; j<subjects_in_dom.length; j++){
                if(subjects_in_dom[j].indexOf(subject_assertions[i]) >- 1){
                    found = true;
                }
            }
            assertions.push(found);
        }

        // verify all assertions satisfied
        let result = assertions.reduce(function(acc,curr){
            return curr ? acc+1 : acc;
        },0) === assertions.length;

        // pint debug info
        // console.log('GIEmail Assert Subjects in DOM', JSON.stringify({
        //     subject_assertions,
        //     subjects_in_dom,
        //     assertions,
        //     result
        // }));

        return result;
    }
    let start = Date.now();
    function recursiveCheck(){
        let now = Date.now();
        let passing = checkForEmails();
        if(passing){
            resolve("true");
        // you can tweak max retry time here, keep in mind there's a hard limit of 60s
        }else if(!passing && now - start < 59000){
            setTimeout(()=>{
                recursiveCheck();
                // you can tweak retry frequency here or make it a variable
            },500);
        }else{
            // note we resolve false instead of rejecting so the test can continue
            resolve("false");
        }
    }
    recursiveCheck();
})
```
