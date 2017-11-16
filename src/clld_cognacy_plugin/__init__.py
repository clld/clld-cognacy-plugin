from __future__ import unicode_literals

from clld_cognacy_plugin.models import Cognateset
from clld_cognacy_plugin.interfaces import ICognateset
from clld_cognacy_plugin.datatables import Cognatesets


def includeme(config):
    config.add_static_view('clld-cognacy-plugin-static', 'clld_cognacy_plugin:static')
    config.registry.settings['mako.directories'].append(
        'clld_cognacy_plugin:templates')
    config.register_resource('cognateset', Cognateset, ICognateset, with_index=True)
    config.register_datatable('cognatesets', Cognatesets)
