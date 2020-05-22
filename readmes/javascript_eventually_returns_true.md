# javascript_eventually_returns_true

Ghost Inpector Helper that continually executes a bit of javascript until it returns true (Asyncronous Javascript Promise Resolves `true`) or time runs out. Default Checker Interval / Frequency is 100ms, but you can customize it. Just define a variable named `javascript_eventually_returns_true` to a bit of Javascript (that MUST start with a `return` statement) then Import this helper to proceed once it passes as true

```@javascript
/* Ghost Inspector Hard Limits */
max_element_timeout = 60s /* aka. max_step_time Configured in Settings > Step Timing > Element Timeout */
max_test_execution_time = 10m /* hard max limit; not configurable */
```
## A. Importables - javascript_eventually_returns_true

### Step 1.

Unset our flag in case we imported this once already

Set Variable `javascript_eventually_returned_true` = `false`

### Step 2. => 11.
> Repeat this step 10x times:
> 
> max_test_execution_time / max_element_timeout = 10

`Import steps from test` = `Importables - javascript_eventually_returns_true (60s step)`

### Step 12.

`Javscript Returns True`:
```@javascript
return "{{javascript_eventually_returned_true}}" === "true";
```

## B. Importables - javascript_eventually_returns_true (60s step)

### Step. 1

Conditionally:
```@javascript
let passing = "{{javascript_eventually_returned_true}}";
return !passing.trim().length || passing !== "true"; /* javascript_eventually_returned_true */
```

Extract From Javascript:
```@javascript
let start = performance.now();
const MAX = 59000;
return new Promise(async (resolve,reject)=>{
    let check = async function(){
    	let passing = (()=>{
    	    {{javascript_eventually_returns_true}}
    	})();
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
= `javascript_eventually_returned_true`
