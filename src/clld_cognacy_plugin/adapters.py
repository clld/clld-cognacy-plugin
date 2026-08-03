"""
Adapters
"""
from clld.web.adapters.geojson import GeoJson
from clld import interfaces
from clld.db.models.common import ValueSet


class GeoJsonCognateset(GeoJson):

    """Render a parameter's values as geojson feature collection."""

    def featurecollection_properties(self, ctx, req):
        marker = req.registry.getUtility(interfaces.IMapMarker)
        return {
            'name': getattr(ctx, 'name', 'Values'),
            'domain': [
                {'icon': marker(de, req), 'id': de.id, 'name': de.name}
                for de in getattr(ctx, 'domain', [])]}

    def feature_iterator(self, ctx, req):
        return [cognate.counterpart.valueset for cognate in ctx.cognates]

    def get_language(self, ctx, req, feature: ValueSet):
        return feature.language

    def feature_properties(self, ctx, req, feature: ValueSet):
        values = [co.counterpart for co in ctx.cognates]
        return {
            'label': ', '.join(v.name for v in feature.values if v in values and v.name) or
                     self.get_language(ctx, req, feature).name}
