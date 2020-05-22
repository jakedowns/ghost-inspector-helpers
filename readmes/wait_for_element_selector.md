## A. wait_for_element_selector to be present
```javascript
max_element_timeout = 60s /* max step time */
max_test_execution_time = 10m
```
> Repeat this step 10x times:
> 
> max_test_execution_time / max_element_timeout = 10

Step 1. => 10.
`Import steps from test` = `Importables - wait_for_element_selector to be present (60s step)`

## B. wait_for_element_selector to be present (60s step)

### Step 1.    
- Conditionally:
```javascript
return "{{wait_for_element_resolved}}" !== "true"
```
- `Javascript Returns True` =
```javascript
return "{{wait_for_element_selector}}".trim().length > 0;
```

- Note: `wait_for_element_selector required`

### Step 2.
- Conditionally: same Condition as Step 1.

- Set Variable `return document.querySelectorAll('{{wait_for_element_selector}}')` = `javascript_eventually_returns_true`

### Step 3.

- Import Steps from Test: `Importables - javascript_eventually_returns_true`

### Step 4.

Flag our element as found so we can stop checking and move on

- Set Variable `true` = `wait_for_element_resolved`

> NOTE: this particular implementation uses `document.querySelectorAll` but you can use jQuery or Whatever you want in `SetVariable` `javascript_eventually_returns_true` as long as it ends with a `return` statement


## See Also:
- [readmes/javascript_eventually_returns_true.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/javascript_eventually_returns_true.md)


