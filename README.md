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

Original doc about XBlocks
http://edx.readthedocs.io/projects/xblock-tutorial/en/latest//getting_started/index.html

# Create and activate virtual env

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

In the xblock_development directory, run the following command to clone the XBlock SDK repository from GitHub.

```
(venv) $ git clone https://github.com/edx/xblock-sdk.git
```

Run the following command to change to the xblock-sdk directory.

```
(venv) $ cd xblock-sdk
```

Run the following command to install the XBlock SDK requirements.

```
(venv) $ pip install -r requirements/base.txt
```

Run the following command to return to the xblock_development directory, where you will perform the rest of your work.

```
(venv) $ cd ..
```

# Create an XBlock

Run the following command to create the skeleton files for the XBlock.

```
(venv) $ xblock-sdk/bin/workbench-make-xblock
```

Instructions in the command window instruct you to determine a short name and a class name. Follow the guidelines in the command window to determine the names that you want to use.

You will be prompted for two pieces of information:

```
* Short name: a single word, all lower-case, for directory and file
  names. For a Pumukit2 XBlock, you might choose "pumukit2".

* Class name: a valid Python class name.  It's best if this ends with
  "XBlock", so for our hologram XBlock, you might choose
    "Pumukit2XBlock".

Once you specify those two names, a directory is created in the
``xblock_development`` directory containing the new project.

If you don't want to create the project here, or you enter a name
incorrectly, type Ctrl-C to stop the creation script.  If you don't want
the resulting project, delete the directory it created.
```

At the command prompt, enter the Short Name you selected for your XBlock.

```
$ Short name: pumukit2
```

At the command prompt, enter the Class name you selected for your XBlock.

```
$ Class name: Pumukit2
```


# Deactivate virtualenv

```
deactivate
```


# Create the SQLite Database

Before running the XBlock SDK the first time, you must create the SQLite database.

In the xblock_development directory, run the following command to create the database.

```
(venv) $ mkdir var
(venv) $ touch var/workbench.log
(venv) $ sudo chown -R edxapp:edxapp var/
(venv) $ sudo -u edxapp /edx/bin/python.edxapp xblock-sdk/manage.py syncdb
```

You are prompted to indicate whether or not to create a Django superuser.

You just installed Django's auth system, which means you don't have any
superusers defined. Would you like to create one now? (yes/no):
Enter no.

```
(venv) $ python no
```
