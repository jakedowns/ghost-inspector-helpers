# 6. Setup Shared Test (Custom Environment-based variables ENVVARS depending on startUrl)

A small ghost inspector test helper that one can include at the top of each in a suite of shared tests, it sets up an object full of environemnt variables and then exposes them for other tests to use. It is conditional and idempotent (knows to only execute once), just in case it gets included multiple times.

For Example, we use this script in order to re-use a single Suite of tests, and run them against multiple instances of our application, hosted across 2 TLD domain names and 3 environments each (dev,staging,prod/www)

> NOTE: this might be inefficient (since each EXTRACT step takes valuable time, since min step time is usually set to at least 250ms or .25s), as i've just realized I could run the suites with a pre-calculated CSV of data. Will investigate that approach and update this file in the future.

> NOTE: Sometimes you may want to conditionally bypass sections of Tests or Whole Tests in a Suite being shared between Environments, Checkout "5. Test Guard (ExitEarly)" for an example of how to do that.
>
> View Readme: [readmes/TestGuardExitEarly.md](https://github.com/jakedowns/ghost-inspector-helpers/blob/master/readmes/TestGuardExitEarly.md)

## Step 1:

- Conditional `Execute steps when JavaScript returns true:`:

```javascript
return "{{shared_test_setup_completed}}" !== "true"
```

```javascript
let startUrl = "{{startUrl}}";
if(typeof(startUrl) == "undefined" || startUrl === "about:blank"){
    startUrl = "{{myStartUrl}}";
}
if(typeof(startUrl) == "undefined"){
    throw new Error('startUrl and fallback myStartUrl both undefined');
    return;
}
var split = startUrl.indexOf('//') > -1 ? startUrl.split('//')[1].split('.') : startUrl.split('.');
if(['www','staging','dev'].indexOf(split[0])===-1){
    split.unshift('www');
}
var subdomain = split[0]+'.';
var host = split[1]+'.'+split[2];

var house_names = {
    "wright20.com":"wright",
    "ragoarts.com":"rago"
};

var auction_house = house_names[host];
var house_name_proper = auction_house.charAt(0).toUpperCase() + auction_house.slice(1)

var deep_subdomain = subdomain;
if(subdomain === 'www.'){
    deep_subdomain = '';
}

var hostname = 'https://'+subdomain+host;
var cms_hostname = 'https://cms.'+deep_subdomain+host;
var api_url = 'https://api.'+deep_subdomain+host;
var live_url = 'https://live.'+deep_subdomain+host;
var realtime_url = 'https://realtime.'+deep_subdomain+host;

var session_paths = {
    wright: 'auctions/2024/12/test-session-wright',
    rago: 'auctions/2024/12/test-session-rago'
}

// TODO: maybe make this an API call?
var test_items = {
    rago: [{
        name: 'Chair test by steve ghostinspector',
        artist_name: 'Bob',
        item_number:'TEST100.004'
    }],
    wright: [{
        name: 'Painting Number 1 ghostinspector',
        artist_name: 'Betsey Johnson',
        item_number:'TEST100.006'
    }]
}

return {
    tld: host,
    subdomain: subdomain,
    hostname: hostname,
    api_url: api_url,
    cms_hostname: cms_hostname,
    live_url,
    realtime_url,
    auction_house: auction_house,
    house_name_proper: house_name_proper,
    test_auction_fd_key: auction_house === 'wright' ? 'YFWV' : '9SJ0',
    test_session_fd_key: auction_house === 'wright' ? 'YFWW' : '9SJ1',
    test_auction_title: 'Test Auction ' + house_name_proper + ' (DO NOT USE)',
    test_session_title: 'Test Session ' + house_name_proper,
    test_session_url: 'https://'+subdomain+host+'/'+session_paths[auction_house],
    test_items: test_items[auction_house],
    house_tz_abbr: auction_house === 'wright' ? 'ct' : 'et',
};
```

## Step 2., 3., etc... (and beyond...)

> Unfortunately GhostInspector does not offer a clean way to [extract()](https://www.php.net/manual/en/function.extract.php) or use ES6 [Destructuring Assignment: Object Destructure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Object_destructuring) an object into individual variables _in a SINGLE STEP_, just yet. Please send them feedback if you'd like this feature as much as I would!

For each of the variables you want to expose you'll need to:

- Conditionally: (Same Conditional as Step. 1)
- `Extract From Javascript`: `YOUR_ENVVAR_NAME` =  
```javascript
const config = {{config}}
return config.my_envvar_name;
```

## Final Step

Last step is to flag the config extraction as complete so it doesn't need to run again

`Set Variable` `shared_test_setup_completed` = `true`
