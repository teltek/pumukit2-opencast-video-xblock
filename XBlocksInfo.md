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
