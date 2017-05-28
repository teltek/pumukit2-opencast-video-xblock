# Pumukit2 XBlock

XBlock to integrate Pumukit2 into an Open edX instance. It is intented to work along with:

- [Open edX version open-release/ficus](https://github.com/edx/edx-platform)
- [PuMuKIT2 Video Platform version 2.3.x](https://github.com/campusdomar/PuMuKIT2/blob/2.3.x/README.md)
- [PuMuKIT2 Open edX Bundle](https://github.com/teltek/PuMuKIT2-open-edx-bundle)


# Download this repo

```
git clone 
```

# Configure Pumukit2 XBlock

Define password and domain of your Pumukit2 instance in an `env.json` file
created at the root path of this repository. Change these values:

```
{
    "DEBUG": true,
    "PROTOCOL": "https",
    "DOMAIN": "gcms-local-naked.teltek.es",
    "SSO_URI": "openedx/sso",
    "MANAGER_URI": "manager",
    "IFRAME_URI": "openedx/openedx/embed",
    "VIDEO_URI": "video.json",
    "REPOSITORY_SEARCH_URI": "repository_search.json",
    "PERSONAL_RECORDER_URI": "personal_recorder",
    "UPLOAD_URI": "upload",
    "PASSWORD": "ThisIsASecretPasswordChangeMe",
    "SHOW_URL_TAB": true,
    "SHOW_UPLOAD_TAB": true,
    "SHOW_RECORDER_TAB": false,
    "SHOW_LIBRARY_TAB": true
}
```


# Install XBlock

```
sudo chown -R edxapp:edxapp /path/to/your/xblock
sudo -u edxapp /edx/bin/pip.edxapp install -e /path/to/your/xblock
```

Uncomment this line in common.py files if it is not already uncommented:

```
# XBLOCK_SELECT_FUNCTION = prefer_xmodules
```

# Enable Pumukit2 XBlock in your course

Access to Studio to a given course. In Settings, Advanced Settings, add
the Pumukit2 XBlock in Advanced Modules List as:

```
["pumukit2"]
```

# Documentation about XBlocks

For more info about XBlocks, read [XBlocksInfo.md](XBlocksInfo).