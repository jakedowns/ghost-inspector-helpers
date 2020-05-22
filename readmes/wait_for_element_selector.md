## A. wait_for_element_selector to be present
```@javascript
max_element_timeout = 60s /* max step time */
max_test_execution_time = 10m
```
> Repeat this step 10x times:
> 
> max_test_execution_time / max_element_timeout = 10

Step 1. => 10.
`Import steps from test` = `Importables - wait_for_element_selector to be present (60s step)`

## B. wait_for_element_selector to be present (60s step)

Step 1.    
- Conditional:
```@javascript
return "{{wait_for_element_resolved}}" !== "true"
```
- `Javascript Returns True` =
```@javascript
return "{{wait_for_element_selector}}".trim().length > 0;
```

- Note: `wait_for_element_selector required`

Step 2.
- Conditional: same as Step 1.

- `Extract from Javascript`: `wait_for_element_resolved` =
```@javascript
const selector = "{{wait_for_element_selector}}"
let start = performance.now();
const MAX = 59000;
return new Promise(async (resolve,reject)=>{
    let check = async function(){
    	let selected = $(selector);
    	if(selected.length>0){
    		resolve(selected.length);
    	}else if(performance.now() - start >= MAX){
    		//reject("failed to locate ".selector);
    		resolve(false);
    	}else{
    		await sleep(100)
    		await check();
    	}
    }
    await check();
});
```

> NOTE: this particular implementation relies on jQuery. if you want to change it to be Vanilla Javascript Only:
> 1. `SetVariable` `javascript_eventually_returns_true` = `return document.querySelector({{wait_for_element_selector}})` OR `return document.querySelectorAll({{wait_for_element_selector}})`
> 2. Import Importables - javascript_eventually_returns_true Instead. View Readme: [javascript_eventually_returns_true.md](javascript_eventually_returns_true.md)


