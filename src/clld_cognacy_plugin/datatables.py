"""
Datatables
"""
from sqlalchemy.orm import joinedload
from clld.db.util import icontains
from clld.db.models.common import Parameter, Language, Value, ValueSet
from clld.web.datatables.base import DataTable, LinkCol, IdCol, Col, LinkToMapCol
from clld.web.datatables.parameter import Parameters

from clld_cognacy_plugin.util import concepticon_link
from clld_cognacy_plugin.models import Cognateset, Cognate


class Cognatesets(DataTable):  # pylint: disable=C0115
    def col_defs(self):
        return [
            IdCol(self, 'id'),
            LinkCol(self, 'name'),
        ]


class ConcepticonCol(Col):  # pylint: disable=C0115
    __kw__ = {'bSearchable': False}

    def format(self, item):
        return concepticon_link(self.dt.req, item)


class Meanings(Parameters):  # pylint: disable=C0115
    def col_defs(self):
        meaning_cls = list(Parameter.__subclasses__())[0]
        return [
            LinkCol(self, 'name'),
            Col(self, 'description'),
            ConcepticonCol(self, '#', model_col=getattr(meaning_cls, 'concepticon_id')),
        ]


class LanguageCol(LinkCol):  # pylint: disable=C0115
    def get_obj(self, item):
        return item.counterpart.valueset.language

    def order(self):
        return Language.name

    def search(self, qs):
        return icontains(Language.name, qs)


class CounterpartCol(LinkCol):  # pylint: disable=C0115
    def get_obj(self, item):
        return item.counterpart

    def order(self):
        return Value.name

    def search(self, qs):
        return icontains(Value.name, qs)


class Cognates(DataTable):
    """This table should be used with a specific Cognateset only."""
    __constraints__ = [Cognateset]
    cognateset: Cognateset

    def base_query(self, query):
        query = query.join(Cognate.counterpart).join(Value.valueset).options(
            joinedload(Cognate.counterpart))
        query = query.join(ValueSet.language).options(
            joinedload(Cognate.counterpart, Value.valueset, ValueSet.language))
        if self.cognateset:
            query = query.join(ValueSet.contribution).options(
                joinedload(Cognate.counterpart, Value.valueset, ValueSet.contribution))
            query = query.filter(Cognate.cognateset == self.cognateset)
        return query

    def col_defs(self):
        return [
            LanguageCol(self, 'variety'),
            CounterpartCol(self, 'word'),
            LinkToMapCol(
                self,
                '#',
                get_object=lambda i: i.counterpart.valueset.language),
        ]
