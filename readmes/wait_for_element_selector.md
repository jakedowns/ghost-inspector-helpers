# wait_for_element_selector to be present

### See Also:

- [readmes/wait_js_true.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/wait_js_true.md)

## Usage

### Step 1. set variable `wait_for_element_selector` = `a[href='/account/reset-password']`
> NOTE make sure to use single quotes or escaped-double quotes `\"\"` in your selector as they'll be wrapped in double-quotes when referenced at run-time

### Step 2. Import Steps from Test `Importables - wait_for_element_selector to be present`

## Test Definitions:

### Importables - wait_for_element_selector to be present

> Click here to see the `.json` "Ghost Inspector" source file of this ghostinspector test definition: [ImportableTestingUtilities/wait_for_element_selector_to_be_present.json](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/ImportableTestingUtilities/wait_for_element_selector_to_be_present.json) 

#### Step 1.    
- Conditionally:
```javascript
return "{{wait_for_element_resolved}}" !== "true"
```
- `Javascript Returns True` =
```javascript
return "{{wait_for_element_selector}}".trim().length > 0;
```

- Note: `wait_for_element_selector required`

#### Step 2.
- Conditionally: same Condition as Step 1.

- Set Variable `return document.querySelectorAll("{{wait_for_element_selector}}").length > 0` = `wait_js_true`

#### Step 3.

- Import Steps from Test: `Importables - wait_js_true`

> NOTE: this particular implementation uses `document.querySelectorAll` but you can use jQuery or Whatever you want in `SetVariable` `wait_js_true` as long as it ends with a `return` statement which returns anything other than `null`, an empty string `''`, or `false`;
