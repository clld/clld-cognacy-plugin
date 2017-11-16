# coding: utf8
from __future__ import unicode_literals, print_function, division

from pyramid import testing
from pyramid import config
import pytest


@pytest.fixture(scope='module')
def testapp():
    from webtest import TestApp
    from clld.db.meta import DBSession, VersionedDBSession, Base
    from clld.db.models import common
    from clld_cognacy_plugin.models import Cognateset, Cognate

    def main():
        cfg = config.Configurator(settings={
            'sqlalchemy.url': 'sqlite://',
            'mako.directories': [
                'clld:web/templates',
                'clld_cognacy_plugin:templates'
            ]})
        cfg.include('clld.web.app')
        cfg.include('clld_cognacy_plugin')
        return cfg.make_wsgi_app()

    DBSession.remove()
    VersionedDBSession.remove()
    wsgi_app = main()
    Base.metadata.bind = DBSession.bind
    Base.metadata.create_all()
    DBSession.add(common.Dataset(id='1', name='test app', domain='example.org'))
    cs = Cognateset(id='1', name='cs: test')
    lang = common.Language(id='l', latitude=2, longitude=2)
    vs = common.ValueSet(id='vs', language=lang)
    v = common.Value(id='v', name='abc', valueset=vs)
    DBSession.add(Cognate(cognateset=cs, counterpart=v))
    yield TestApp(wsgi_app)


@pytest.fixture(scope='module')
def configurator():
    config = testing.setUp(
        request=testing.DummyRequest(translate=lambda s: s),
        settings={
            'sqlalchemy.url': 'sqlite://',
            'mako.directories': []})
    config.include('clld.web.app')
    config.include('clld_cognacy_plugin')
    yield config
    testing.tearDown()
