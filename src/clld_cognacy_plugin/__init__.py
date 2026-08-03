"""
clld plugin to support wordlists with cognacy judgements.
"""
from clld_cognacy_plugin.models import Cognateset
from clld_cognacy_plugin.interfaces import ICognateset
from clld_cognacy_plugin.datatables import Cognatesets, Cognates
from clld_cognacy_plugin.maps import CognatesetMap
from clld_cognacy_plugin.adapters import GeoJsonCognateset


def includeme(config):  # pylint: disable=C0116
    config.add_static_view('clld-cognacy-plugin-static', 'clld_cognacy_plugin:static')
    config.registry.settings['mako.directories'].append('clld_cognacy_plugin:templates')
    config.register_resource('cognateset', Cognateset, ICognateset, with_index=True)
    config.register_datatable('cognatesets', Cognatesets)
    config.register_datatable('cognates', Cognates)
    config.register_map('cognateset', CognatesetMap)
    config.register_adapter(GeoJsonCognateset, ICognateset, name=GeoJsonCognateset.mimetype)
