"""
Utilities
"""
from clld.web.util import htmllib


def concepticon_link(request, meaning):
    """A link to a Concepticon concept set."""
    if not meaning.concepticon_id:
        return ''
    return htmllib.HTML.a(
        htmllib.HTML.img(
            src=request.static_url('clld_cognacy_plugin:static/concepticon_logo.png'),
            height=20,
            width=30),
        title='corresponding concept set at Concepticon',
        href=f"http://concepticon.clld.org/parameters/{meaning.concepticon_id}")
