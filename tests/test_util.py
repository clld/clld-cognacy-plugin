# coding: utf8
from __future__ import unicode_literals, print_function, division

from clld_cognacy_plugin import util


def test_concepticon_link(mocker):
    res = util.concepticon_link(
        mocker.Mock(static_url=lambda x: ''),
        mocker.Mock(concepticon_id='12345'))
    assert '12345' in '{0}'.format(res)

    res = util.concepticon_link(
        mocker.Mock(static_url=lambda x: ''),
        mocker.Mock(concepticon_id=None))
    assert '' == '{0}'.format(res)
