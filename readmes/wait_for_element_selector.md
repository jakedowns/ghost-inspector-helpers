# wait_for_element_selector to be present

### See Also:

- Click here to see the `.json` "Ghost Inspector" reference / source file of _this_ test definition: [ImportableTestingUtilities/wait_for_element_selector_to_be_present.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_for_element_selector_to_be_present.json)
  
  TODO: i'll add `Selenium IDE v1` format reference version in the future

- This test depends on: [readmes/wait_js_true.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_js_true.md)

## Usage

### Step 1. set variable `wait_for_element_selector` = `a[href='/account/reset-password']`
> NOTE make sure to use single quotes or escaped-double quotes `\"\"` in your selector as they'll be wrapped in double-quotes when referenced at run-time

### Step 2. Import Steps from Test `Importables - wait_for_element_selector to be present`

## Test Definition for __Importables - wait_for_element_selector to be present__

> Click here to see the `.json` "Ghost Inspector format" source file of this ghostinspector test definition: [ImportableTestingUtilities/wait_for_element_selector_to_be_present.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_for_element_selector_to_be_present.json) 
> 
> TODO: i'll add `Selenium IDE v1` format reference version in the future

### Step 1.    
- `Javascript Returns True` =
```javascript
return "{{wait_for_element_selector}}".trim().length > 0;
```

- Note: `wait_for_element_selector required`

### Step 2.

- Set Variable `return document.querySelectorAll("{{wait_for_element_selector}}").length > 0` = `wait_js_true`

> NOTE: this particular implementation uses `document.querySelectorAll` but you can use jQuery or Whatever you want in `SetVariable` `wait_js_true` as long as it ends with a `return` statement which returns anything "truthy", basically other than something `undefined`, `null`, an empty string `''`, `false`, or `0`;

### Step 3.

- Import Steps from Test: `Importables - wait_js_true`

> See Dependency Test Definition: [readmes/wait_js_true.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_js_true.md)
