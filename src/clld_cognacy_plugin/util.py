from clld.web.util import htmllib


def concepticon_link(request, meaning):
    if not meaning.concepticon_id:
        return ''
    return htmllib.HTML.a(
        htmllib.HTML.img(
            src=request.static_url('clld_cognacy_plugin:static/concepticon_logo.png'),
            height=20,
            width=30),
        title='corresponding concept set at Concepticon',
        href="http://concepticon.clld.org/parameters/{0}".format(meaning.concepticon_id))
