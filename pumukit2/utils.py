# -*- coding: utf-8 -*-
#

from datetime import datetime
import pumukit2_settings
import hashlib
import logging


def get_hash(email, password, domain):
    """ Get hash of Pumukit user."""
    date = datetime.now().strftime('%d/%m/%Y')
    m = hashlib.md5("{email}{password}{date}{domain}".format(email=email, password=password, date=date, domain=domain))

    return m.hexdigest()


def get_manager_url(username):
    """ Get Pumukit2 Media Manager URL."""
    base_url = pumukit2_settings.BASE_URL
    sso_uri = pumukit2_settings.SSO_URI
    manager_uri = pumukit2_settings.MANAGER_URI

    password = pumukit2_settings.PASSWORD
    domain = pumukit2_settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{manager_uri}?hash={pumukit_hash}&username={username}'.format(base_url=base_url, sso_uri=sso_uri, manager_uri=manager_uri, pumukit_hash=pumukit_hash, username=username)

def get_iframe_url(video_id):
    """ Get Pumukit2 Iframe URL."""
    base_url = pumukit2_settings.BASE_URL
    iframe_uri = pumukit2_settings.IFRAME_URI
    password = pumukit2_settings.PASSWORD
    domain = pumukit2_settings.DOMAIN
    pumukit_hash = get_hash('', password, domain)
    if not video_id and pumukit2_settings.DEFAULT_VIDEO_ID:
        video_id = pumukit2_settings.DEFAULT_VIDEO_ID
    if not video_id:
        return False

    return '{base_url}/{iframe_uri}/?id={video_id}&hash={ph}'.format(base_url=base_url, iframe_uri=iframe_uri, video_id=video_id, ph=pumukit_hash)

def get_api_video_url(username, video_id):
    """ Get Pumukit2 API Video URL."""
    base_url = pumukit2_settings.BASE_URL
    sso_uri = pumukit2_settings.SSO_URI
    video_uri = pumukit2_settings.VIDEO_URI

    password = pumukit2_settings.PASSWORD
    domain = pumukit2_settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{video_id}/{video_uri}?hash={pumukit_hash}&username={username}'.format(base_url=base_url, sso_uri=sso_uri, video_id=video_id, video_uri=video_uri, pumukit_hash=pumukit_hash, username=username)

def get_personal_recorder_url(username):
    """ Get Pumukit2 Personal Recorder URL."""
    base_url = pumukit2_settings.BASE_URL
    sso_uri = pumukit2_settings.SSO_URI
    recorder_uri = pumukit2_settings.PERSONAL_RECORDER_URI

    password = pumukit2_settings.PASSWORD
    domain = pumukit2_settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{recorder_uri}?hash={pumukit_hash}&username={username}'.format(base_url=base_url, sso_uri=sso_uri, recorder_uri=recorder_uri, pumukit_hash=pumukit_hash, username=username)

def get_upload_url(username, lang):
    """ Get Pumukit2 Wizard Simple Upload URL."""
    base_url = pumukit2_settings.BASE_URL
    sso_uri = pumukit2_settings.SSO_URI
    upload_uri = pumukit2_settings.UPLOAD_URI

    password = pumukit2_settings.PASSWORD
    domain = pumukit2_settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{upload_uri}?hash={pumukit_hash}&username={username}&lang={lang}'.format(base_url=base_url, sso_uri=sso_uri, upload_uri=upload_uri, pumukit_hash=pumukit_hash, username=username, lang=lang)
