# wait_js_true

Test Defintions .json Format:
> TODO: i'll add `Selenium IDE v1` format reference version in the future

- [ImportableTestingUtilities/wait_js_true.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true.json) 
- [ImportableTestingUtilities/wait_js_true_single_60s_step.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_js_true_single_60s_step.json) 

Ghost Inspector Helper that continually executes a bit of javascript until it returns true (Asyncronous Javascript Promise Resolves `true`) or time runs out. Default Checker Interval / Frequency is 100ms, but you can customize it. Just define a variable named `wait_js_true` to a bit of Javascript (that MUST end with a `return` statement) then Import this helper to proceed once it passes as true

After the importer runs and passes, you can access the "truthy" (non-undefined, non-null, non-empty-string, non-"false", non-"0") result of the operation via the `{{wait_js_true_done}}` variable

## Usage:

### Step 1: 
- `SetVariable` `wait_js_true` =
> Note this can be whatever as long as it's valid Javascript (ES6 allowed) and ends with a valid `return` statement.

Here's an example taken from [readmes/wait_for_element_selector.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_for_element_selector.md) which returns True once the element(s) are in the DOM:
```javascript
return document.querySelectorAll('{{wait_for_element_selector}}')
```

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
return !passing.trim().length && passing !== "false" && result !== "0"; /* !wait_js_true_done? */
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
