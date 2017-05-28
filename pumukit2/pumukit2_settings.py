import sys
import os
import json

# Debug for developers
DEBUG = False

# Protocol: HTTP vs HTTPS
PROTOCOL = 'https'

# Domain of Pumukit2 instance. For example: pumukit2instance.com
DOMAIN = 'localhost'

# Open edX URI for Pumukit2 instance with SSO: For example: openedx/sso
SSO_URI = 'openedx/sso'

# Pumukit2 Media Manager URI. For example: manager
MANAGER_URI = 'manager'

# Pumukit2 Iframe URI. For example: iframe
IFRAME_URI = 'openedx/openedx/embed'

# Pumukit2 API Video URI. For example: video.json
VIDEO_URI = 'video.json'

# Pumukit2 Personal Recorder URI. For example: personal_recorder
PERSONAL_RECORDER_URI = 'personal_recorder'

# Pumukit2 Wizard Simple Upload URI. For example: upload
UPLOAD_URI = 'upload'

# Pumukit2 Open edX Bundle defined password.
PASSWORD = 'AddPumukit2OpenEdxBundlePasswordHere'

# Show URL tab in Edit modal window
SHOW_URL_TAB = True

# Show UPLOAD tab in Edit modal window
SHOW_UPLOAD_TAB = True

# Show PERSONAL RECORDER tab in Edit modal window
SHOW_RECORDER_TAB = False

# Show LIBRARY tab in Edit modal window
SHOW_LIBRARY_TAB = True

# Default video ID in Pumukit2
DEFAULT_VIDEO_ID = ''

# Root directory of this file
CONFIG_ROOT = os.path.dirname(os.path.abspath(__file__))

with open(CONFIG_ROOT + "/../env.json") as env_file:
    ENV_TOKENS = json.load(env_file)

DEBUG = ENV_TOKENS.get('DEBUG', DEBUG)
PROTOCOL = ENV_TOKENS.get('PROTOCOL', PROTOCOL)
DOMAIN = ENV_TOKENS.get('DOMAIN', DOMAIN)
SSO_URI = ENV_TOKENS.get('SSO_URI', SSO_URI)
MANAGER_URI = ENV_TOKENS.get('MANAGER_URI', MANAGER_URI)
IFRAME_URI = ENV_TOKENS.get('IFRAME_URI', IFRAME_URI)
VIDEO_URI = ENV_TOKENS.get('VIDEO_URI', VIDEO_URI)
PERSONAL_RECORDER_URI = ENV_TOKENS.get('PERSONAL_RECORDER_URI', PERSONAL_RECORDER_URI)
UPLOAD_URI = ENV_TOKENS.get('UPLOAD_URI', UPLOAD_URI)
PASSWORD = ENV_TOKENS.get('PASSWORD', PASSWORD)
SHOW_URL_TAB = ENV_TOKENS.get('SHOW_URL_TAB', SHOW_URL_TAB)
SHOW_UPLOAD_TAB = ENV_TOKENS.get('SHOW_UPLOAD_TAB', SHOW_UPLOAD_TAB)
SHOW_RECORDER_TAB = ENV_TOKENS.get('SHOW_RECORDER_TAB', SHOW_RECORDER_TAB)
SHOW_LIBRARY_TAB = ENV_TOKENS.get('SHOW_LIBRARY_TAB', SHOW_LIBRARY_TAB)
DEFAULT_VIDEO_ID = ENV_TOKENS.get('DEFAULT_VIDEO_ID', DEFAULT_VIDEO_ID)

ACCEPTED_PROTOCOLS = {'http', 'https'}
if PROTOCOL not in ACCEPTED_PROTOCOLS:
    PROTOCOL = 'https'

BASE_URL = "{}://{}".format(PROTOCOL, DOMAIN)
