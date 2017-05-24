# -*- coding: utf-8 -*-
#

from django.conf import settings
import pumukit2_settings

import requests

import logging

log = logging.getLogger(__name__)

def get_response(url):
    """ Get the response of a given url """
    verify = not pumukit2_settings.DEBUG
    try:
        r = requests.head(url, allow_redirects=True, verify=verify)
        url_code = r.status_code
        if url_code == 200:
            return requests.get(url, allow_redirects=True, verify=verify)
        else:
            log.debug('Connection to {url} had a response of status code {code}'.format(url=url, code=url_code))
    except Exception as exc:
        log.error('Exception: {}'.format(exc))
        raise exc

    return null


def get_json_response(url):
    """ Get json response of a given url """
    try:
        response = get_response(url)
        if response:
            return response.json()
    except Exception as exc:
        log.error('Exception: {}'.format(exc))
        raise exc

    return null
