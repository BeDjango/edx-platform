"""
Utility methods related to course
"""
import logging

from django.conf import settings

from openedx.core.djangoapps.catalog.utils import get_run_marketing_url

log = logging.getLogger(__name__)


def get_link_for_about_page(course_key, user, catalog_course_run=None):
    """
    Returns the url to the course about page.
    """
    if settings.FEATURES.get('ENABLE_MKTG_SITE'):
        if catalog_course_run:
            marketing_url = catalog_course_run.get('marketing_url')
        else:
            marketing_url = get_run_marketing_url(user, course_key)
        if marketing_url:
            return marketing_url

    return u"{about_base_url}/courses/{course_key}/about".format(
        about_base_url=settings.LMS_ROOT_URL,
        course_key=course_key
    )
