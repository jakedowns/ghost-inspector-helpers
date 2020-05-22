# Ghost Inspector Test Email Subject is present in Mailtrap.io Inbox 

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
