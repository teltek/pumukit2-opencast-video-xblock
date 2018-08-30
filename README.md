# Pumukit2 XBlock

XBlock to integrate Pumukit2 into an Open edX instance. It is intented to work along with:

- [Open edX version open-release/ficus](https://github.com/edx/edx-platform)
- [PuMuKIT2 Video Platform version 2.3.x](https://github.com/campusdomar/PuMuKIT2/blob/2.3.x/README.md)
- [PuMuKIT2 Open edX Bundle](https://github.com/teltek/PuMuKIT2-open-edx-bundle)

This XBlocks allows to integrate PuMuKIT2 Video Platform into Open edX to add videos,
upload videos, manage videos or even record personal videos.
This XBlock can be used with either PuMuKIT 2.3.x or 2.4.x.
This videos can have public or hidden status in PuMuKIT platform,
easing the privacy of the videos. The XBlock offers different ways to integrate
a PuMuKIT video into Open edX. The professor has an editing modal window
to chose how to add content to the unit. In this modal window the professor
has various options to integrate a video from:

* URL: Through the ID of the video in PuMuKIT.

![Add video ID in URL](/images/01.URL.png)

* UPLOAD: The professor can upload a video to PuMuKIT and publish it directly from Open edX, automatically sharing the video into the Open edX unit.

![Upload video](/images/02.UPLOAD.png)

* RECORDER: If the PuMuKIT plaform has enabled the Personal Recorder, this tool is also integrated into Open edX. The professor can record from his/her own personal computer a dual stream video using this XBlock in Open edX and publish it automatically in PuMuKIT and the Open edX unit.
* LIBRARY: The professor can manage his/her own videos with this XBlock.

![Manage videos](/images/03.LIBRARY.png)

The students will watch the video into the LMS the same way the professor watch it.

![Video in Studio](/images/04.STUDIO.png)

![Video in LMS](/images/05.LMS.png)


# Installation for server


## Download this repo

```
git clone git@github.com:teltek/pumukit2-opencast-video-xblock.git
```

## Configure Pumukit2 XBlock

Define password and domain of your Pumukit2 instance in an `env.json` file
created at the root path of this repository.

* `DEBUG`: Django DEBUG value. Only for development environment.
* `PROTOCOL`: Protocol used by PuMuKIT server.
* `DOMAIN`: Domain or subdomain used to access into the naked backoffice of PuMuKIT server.
* `SSO_URI`: URI defined to access global SSO controller in PuMuKIT2 Open edX Bundle.
* `MANAGER_URI`: URI defined to access Manager request in Manager controller in PuMuKIT2 Open edX Bundle.
* `IFRAME_URI`: URI defined to embed PuMuKIT videos into Open edX. This is the full URI to access Iframe request in Open edX Controller of PuMuKIT2 Open edX Bundle.
* `VIDEO_URI`: URI defined to build the API video URL to get data of the video.
* `PERSONAL_RECORDER_URI`: URI defined to access Personal Recorder request in Personal Recorder Controller of PuMuKIT2 Open edX Bundle. You should install Personal Recorder Bundle to make this work.
* `UPLOAD_URI`: URI defined to access the Upload request in the Upload Controller of PuMuKIT2 Open edX Bundle.
* `PASSWORD`: Shared secret with Open edX Bundle.
* `SHOW_URL_TAB`: Whether to show or not the tab with the URL (ID) of the video in the Studio edit modal window.
* `SHOW_UPLOAD_TAB`: Whether to show or not the Upload tab in the Studio edit modal window.
* `SHOW_RECORDER_TAB`: Whether to show or not the Recorder tab in the Studio edit modal window.
* `SHOW_LIBRARY_TAB`: Whether to show or not the Library tab in the Studio edit modal window.

Example of `env.json` with default values. Change these values:

```
{
    "DEBUG": false,
    "PROTOCOL": "https",
    "DOMAIN": "pumukit-example-naked-uri.com",
    "SSO_URI": "openedx/sso",
    "MANAGER_URI": "manager",
    "IFRAME_URI": "openedx/openedx/embed",
    "VIDEO_URI": "video.json",
    "PERSONAL_RECORDER_URI": "personal_recorder",
    "UPLOAD_URI": "upload",
    "PASSWORD": "ThisIsASecretPasswordChangeMe",
    "SHOW_URL_TAB": true,
    "SHOW_UPLOAD_TAB": true,
    "SHOW_RECORDER_TAB": false,
    "SHOW_LIBRARY_TAB": true
}
```

## Install XBlock

```
sudo chown -R edxapp:edxapp /path/to/your/xblock
sudo -u edxapp /edx/bin/pip.edxapp install -e /path/to/your/xblock
```

Uncomment this line in common.py files if it is not already uncommented:

```
# XBLOCK_SELECT_FUNCTION = prefer_xmodules
```

## Enable Pumukit2 XBlock in your course

Access to Studio to a given course. In Settings, Advanced Settings, add
the Pumukit2 XBlock in Advanced Modules List as:

```
["pumukit2"]
```


# Installation for Hawthorn Dockers


## Mount a folder for xblock outside the docker

Edit file `devstack/docker-compose-host.yml`

```
version: "2.1"

services:
  ...
  lms:
    volumes:
      ...
      - ${DEVSTACK_WORKSPACE}/xblocks:/edx/app/edxapp/xblocks
  ...
  studio:
    volumes:
      ...
      - ${DEVSTACK_WORKSPACE}/xblocks:/edx/app/edxapp/xblocks
```


## Download this repo in xblock folder outside Dockers

```
git clone git@github.com:teltek/pumukit2-opencast-video-xblock.git
```

## Configure Pumukit2 XBlock in xblock folder outside Dockers

Define password and domain of your Pumukit2 instance in an `env.json` file
created at the root path of this repository.

* `DEBUG`: Django DEBUG value. Only for development environment.
* `PROTOCOL`: Protocol used by PuMuKIT server.
* `DOMAIN`: Domain or subdomain used to access into the naked backoffice of PuMuKIT server.
* `SSO_URI`: URI defined to access global SSO controller in PuMuKIT2 Open edX Bundle.
* `MANAGER_URI`: URI defined to access Manager request in Manager controller in PuMuKIT2 Open edX Bundle.
* `IFRAME_URI`: URI defined to embed PuMuKIT videos into Open edX. This is the full URI to access Iframe request in Open edX Controller of PuMuKIT2 Open edX Bundle.
* `VIDEO_URI`: URI defined to build the API video URL to get data of the video.
* `PERSONAL_RECORDER_URI`: URI defined to access Personal Recorder request in Personal Recorder Controller of PuMuKIT2 Open edX Bundle. You should install Personal Recorder Bundle to make this work.
* `UPLOAD_URI`: URI defined to access the Upload request in the Upload Controller of PuMuKIT2 Open edX Bundle.
* `PASSWORD`: Shared secret with Open edX Bundle.
* `SHOW_URL_TAB`: Whether to show or not the tab with the URL (ID) of the video in the Studio edit modal window.
* `SHOW_UPLOAD_TAB`: Whether to show or not the Upload tab in the Studio edit modal window.
* `SHOW_RECORDER_TAB`: Whether to show or not the Recorder tab in the Studio edit modal window.
* `SHOW_LIBRARY_TAB`: Whether to show or not the Library tab in the Studio edit modal window.

Example of `env.json` with default values. Change these values:

```
{
    "DEBUG": false,
    "PROTOCOL": "https",
    "DOMAIN": "pumukit-example-naked-uri.com",
    "SSO_URI": "openedx/sso",
    "MANAGER_URI": "manager",
    "IFRAME_URI": "openedx/openedx/embed",
    "VIDEO_URI": "video.json",
    "PERSONAL_RECORDER_URI": "personal_recorder",
    "UPLOAD_URI": "upload",
    "PASSWORD": "ThisIsASecretPasswordChangeMe",
    "SHOW_URL_TAB": true,
    "SHOW_UPLOAD_TAB": true,
    "SHOW_RECORDER_TAB": false,
    "SHOW_LIBRARY_TAB": true
}
```

## Install XBlock inside both dockers LMS and CMS

```
make lms-shell
sudo chown -R edxapp:edxapp /path/to/your/xblock
sudo -u edxapp /edx/bin/pip.edxapp install -e /path/to/your/xblock
```

Uncomment this line in common.py files if it is not already uncommented:

```
# XBLOCK_SELECT_FUNCTION = prefer_xmodules
```


## Compile assets and restart service

Inside both dockers

```
paver update_assets lms --settings=devstack_docker
paver update_assets cms --settings=devstack_docker
```

Outside dockers

```
make lms-restart
make studio-restart
```


## Enable Pumukit2 XBlock in your course

Access to Studio to a given course. In Settings, Advanced Settings, add
the Pumukit2 XBlock in Advanced Modules List as:

```
["pumukit2"]
```


# Documentation about XBlocks

For more info about XBlocks, read [XBlocksInfo.md](XBlocksInfo.md).
