# 5. Importables - Test Guard (Exit Early)

A small ghost inspector test helper that will allow you to "Guard" a test shared between multiple environments, that will only execute if the current url matches a specific sub string, otherwise the text will Exit early with a Passing status.

## Test Definition:

### Step. 1:
- Conditionally ` Execute steps when JavaScript returns true:` =
```
/* returns true when we're NOT at a whitelisted url for the parent test indicating we should soft exit early */
return window.location.href.indexOf("{{guard_url_must_contain}}") === -1;
```
- `Exit Test`: `Passing = checked`

> NOTE: you could also combine this with "6. Setup Shared Test" to guard based on a custom-defined EnvVar of your own.
>
> View Readme: [readmes/SetupSharedTest.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/SetupSharedTest.md)

---

## Usage:

1. `Set Variable`: `guard_url_must_contain` = `example-allowed-url-path-substring`
2. `Import Steps from Test`: `Importables - Test Guard (Exit Early)`
