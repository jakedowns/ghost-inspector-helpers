# 5. Importables - Test Guard (Exit Early)

A small ghost inspector test helper that will allow you to "Guard" a test shared between multiple environments, that will only execute if the current url matches a specific sub string, otherwise the text will Exit early with a Passing status.

Step 1: 
- Conditional ` Execute steps when JavaScript returns true:` =
```
/* returns true when we're NOT at a whitelisted url for the parent test indicating we should soft exit early */
return window.location.href.indexOf("{{guard_url_must_contain}}") === -1;
```
- `Exit Test`: `Passing = checked`

## Usage:

1. `Set Variable`: `guard_url_must_contain` = `example-allowed-url-path-substring`
2. `Import Steps from Test`: `Importables - Test Guard (Exit Early)`
