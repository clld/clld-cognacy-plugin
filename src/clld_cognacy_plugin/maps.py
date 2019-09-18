from clld.web.maps import Map, Layer


class CognatesetMap(Map):
    def get_layers(self):
        yield Layer(
            self.ctx.id,
            self.ctx.name,
            self.req.resource_url(self.ctx, ext='geojson'))

    def get_default_options(self):
        return {
            'show_labels': True,
            'info_query': {'parameter': self.ctx.pk},
            'hash': True}
