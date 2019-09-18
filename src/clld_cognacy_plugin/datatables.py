from clld.db.models.common import Parameter
from clld.web.datatables.base import DataTable, LinkCol, IdCol, Col
from clld.web.datatables.parameter import Parameters

from clld_cognacy_plugin.util import concepticon_link


class Cognatesets(DataTable):
    def col_defs(self):
        return [
            IdCol(self, 'id'),
            LinkCol(self, 'name'),
        ]


class ConcepticonCol(Col):
    __kw__ = dict(bSearchable=False)

    def format(self, item):
        return concepticon_link(self.dt.req, item)


class Meanings(Parameters):
    def col_defs(self):
        meaning_cls = list(Parameter.__subclasses__())[0]
        return [
            LinkCol(self, 'name'),
            Col(self, 'description'),
            ConcepticonCol(self, '#', model_col=getattr(meaning_cls, 'concepticon_id')),
        ]
