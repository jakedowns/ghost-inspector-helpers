# wait_js_true

> NOTE: Definition of term: in this context, the term **_"truthy"_** is defined as: a non-undefined, non-null, non-empty-string, non-"false", non-"0" value

What is this?
This Importable Helper Utility Test is comprised of two Ghost Inspector Tests that continually execute a string of javascript that **_you_** define until it returns a "truthy" value. It fails when time runs out.

What does it do?
- the first test, using Promises and a loop, waits for Javascript Eventually Returns True (er,... a truthy value) (up to 60 seconds)
- the second test is a higher order function that wraps the first test and calls it 10x, giving the max wait time of 10 minutes

When/Why is it useful?
- When you need to wait for something Longer than the maxium `60s` value of the `Settings > Step Timing > Element Timeout` option.

How is it better?
- it repeats a 60s loop up to 10 times (a max of 10 minutes) to wait for the javascript to resolve.

> NOTE: if you don't want it to wait the full 10 minutes before failing, just include the repeated step less times, or directly import the "single 60s step" instead of the wrapper "repeating" test

Drawbacks?
- it will take a long time to fail if you're not careful, be sure you know what you're doing
- it will clutter your test run output with un-hidable "skipped steps" unfortunately. at the veryΩ least, there's an option to "collapse imported steps"

> Note the Default Checker Interval / Frequency is `100ms`, you can modify this as you see fit by altering the `await sleep(100)` bit below 

### Test Defintions in .json Format:

- [ImportableTestingUtilities/wait_js_true.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true.json) 
- [ImportableTestingUtilities/wait_js_true_single_60s_step.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true_single_60s_step.json) 
> TODO: i'll add `Selenium IDE v1` format reference version in the future

## Usage:

### Step 1: 
- `SetVariable` `wait_js_true` =
> Note this can be whatever as long as it's valid Javascript (ES6 allowed) and ends with a valid `return` statement.

Here's an example taken from [readmes/wait_for_element_selector.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_for_element_selector.md) which returns True once the element(s) are in the DOM:
```javascript
return document.querySelectorAll('{{wait_for_element_selector}}').length > 0
```

you could also have it simply return the .length value 

```javascript
return document.querySelectorAll('{{wait_for_element_selector}}').length
```

or even just the resulting Array:

```javascript
return document.querySelectorAll('{{wait_for_element_selector}}')
```

as long as it's "truthy" and will eventually pass.

## Test Definitions:

### A. Importables - wait_js_true

See Defintion in .json Format: [ImportableTestingUtilities/wait_js_true.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true.json)
> TODO: i'll add `Selenium IDE v1` format reference version in the future

#### Step 1.

Unset our flag in case we imported this once already

Set Variable `wait_js_true_done` = `false`

#### Step 2. => 11.

Given:
```javascript
/* Ghost Inspector Hard Limits */
max_element_timeout = 60s /* aka. max_step_time Configured in Settings > Step Timing > Element Timeout */
max_test_execution_time = 10m /* hard max limit; not configurable */
```

> We can repeat this step at most 10 times:
> 
> max_test_execution_time / max_element_timeout = 10x

`Import steps from test` = `Importables - wait_js_true (60s step)`

#### Step 12.

**Assert** that it did indeed finally resolve as truthy

`Javscript Returns True`:
```javascript
let result = "{{wait_js_true_done}}"
return result.trim().length > 0 && result !== "false" && result !== "0";
```

### B. Importables - wait_js_true (60s step)

See Defintion in .json Format: [ImportableTestingUtilities/wait_js_true_single_60s_step.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true_single_60s_step.json)
> TODO: i'll add `Selenium IDE v1` format reference version in the future

#### Step. 1

Conditionally:
```javascript
let passing = "{{wait_js_true_done}}";
return !passing.trim().length || passing == "false"; /* !wait_js_true_done? */
```

Extract From Javascript:
```javascript
const sleep = m => new Promise(r => setTimeout(r, m))
let start = performance.now();
const MAX = 59000;
return new Promise(async (resolve,reject)=>{
    let check = async function(){
    	let passing = (()=>{
    	    {{wait_js_true}}
    	})();
        // must resolve as "truthy"
        // non-null, non-false, non-zero, // add non-empty-string?
    	if(passing){
    		resolve(passing);
    	}else if(performance.now() - start >= MAX){
    		resolve(false,'ran out of time');
    	}else{
    		await sleep(100)
    		await check();
    	}
    }
    await check();
});
```
= `wait_js_true_done`
