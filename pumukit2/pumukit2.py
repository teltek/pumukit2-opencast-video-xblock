"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment

from django.conf import settings

from .utils import get_manager_url, get_iframe_url, get_api_video_url, get_repository_search_url, get_personal_recorder_url, get_upload_url
from .connections import get_json_response
from .render_utils import render_template

import pumukit2_settings

import logging

log = logging.getLogger(__name__)

@XBlock.needs("user")
class Pumukit2XBlock(XBlock):
    """
    XBlock to integrate Pumukit2
    """

    display_name = String(
        display_name="Display Name",
        help="Display name for this module in case the source video doesn't have any.",
        default="Pumukit2",
        scope=Scope.settings
    )

    video_id = String(
        display_name="Video ID",
        help="Video ID of the Pumukit2 Multimedia Object.",
        default="",
        scope=Scope.settings
    )

    video_title = String(
        display_name="Video Title",
        help="Video Title of the Pumukit2 Multimedia Object.",
        default="",
        scope=Scope.settings
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the Pumukit2XBlock, shown to students
        when viewing courses.
        """
        try:
            pumukit_url = get_iframe_url(self.video_id)
            content = render_template('static/html/pumukit2.html', {
                'self': self,
                'pumukit_url': pumukit_url,
            })
            frag = Fragment(content)
            frag.add_css(self.resource_string("static/css/pumukit2.css"))
            frag.add_javascript(self.resource_string("static/js/src/pumukit2.js"))
            frag.initialize_js('Pumukit2XBlock')
        except Exception as exc:
            html = self.resource_string("static/html/pumukit2_error.html")
            error_message = "{}".format(exc)
            frag = Fragment(html.format(error_message=error_message))

        return frag

    def studio_view(self, context):
        """
        Editing view in Studio
        """
        try:
            username = self._get_logged_in_user()

            language = settings.LANGUAGE_CODE
            lang = language[:2]

            upload_url = get_upload_url(username, lang)
            recorder_url = get_personal_recorder_url(username)
            pumukit_url = get_manager_url(username)

            show_url_tab = pumukit2_settings.SHOW_URL_TAB
            show_upload_tab = pumukit2_settings.SHOW_UPLOAD_TAB
            show_recorder_tab = pumukit2_settings.SHOW_RECORDER_TAB
            show_library_tab = pumukit2_settings.SHOW_LIBRARY_TAB

            content = render_template('static/html/pumukit2_edit.html', {
                'self': self,
                'upload_url': upload_url,
                'recorder_url': recorder_url,
                'pumukit_url': pumukit_url,
                'show_url_tab': show_url_tab,
                'show_upload_tab': show_upload_tab,
                'show_recorder_tab': show_recorder_tab,
                'show_library_tab': show_library_tab,
            })
            frag = Fragment(content)
            frag.add_css(self.resource_string("static/css/pumukit2_edit.css"))
            frag.add_css(self.resource_string("static/css/pumukit2_select.css"))
            frag.add_javascript(self.resource_string("static/js/src/pumukit2_edit.js"))
            frag.initialize_js('Pumukit2Edit')
        except Exception as exc:
            html = self.resource_string("static/html/pumukit2_error.html")
            error_message = "{}".format(exc)
            frag = Fragment(html.format(error_message=error_message))

        return frag
    
    @XBlock.json_handler
    def pumukit_submit(self, data, suffix=''):
        """
        Actions to take when click save button on edit
        """
        video_id = data['video_id']
        if video_id == self.video_id:
            return {
                'result': 'success',
            }

        try:
            self.video_id = video_id
            self.video_title = ''
        except Exception as exc:
            log.error('Exception: {}'.format(exc))
            return {   
                'result': 'error',
                'message': 'error on saving data',
            }

        try:
            username = self._get_logged_in_user()
            pumukit_url = get_api_video_url(username, video_id)

            language = settings.LANGUAGE_CODE
            lang = language[:2]

            response = get_json_response(pumukit_url)
            self.video_title = response.get('title').get(lang)
        except Exception as exc:
            log.error('Exception: {}'.format(exc))
            self.video_title = ''

        return {
            'result': 'success',
        }

    
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Pumukit2XBlock",
             """<pumukit2/>
             """),
            ("Multiple Pumukit2XBlock",
             """<vertical_demo>
                <pumukit2/>
                <pumukit2/>
                <pumukit2/>
                </vertical_demo>
             """),
        ]

    def _get_logged_in_user(self):
        user_service = self.runtime.service(self, 'user')
        username = user_service.get_current_user().opt_attrs['edx-platform.username']

        return username
