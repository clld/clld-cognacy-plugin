# coding: utf8
from __future__ import unicode_literals, print_function, division

import sqlalchemy as sa
import pytest
from pyramid.threadlocal import get_current_request
from clld.db.meta import CustomModelMixin
from clld.db.models.common import Parameter
from clld_cognacy_plugin import datatables
from clld_cognacy_plugin import models


def test_ConcepticonCol(mocker, configurator):
    col = datatables.ConcepticonCol(
        mocker.Mock(req=get_current_request()),
        '',
        model_col=mocker.MagicMock())
    col.format(mocker.Mock())


def test_Cognatesets(configurator):
    dt = datatables.Cognatesets(get_current_request(), models.Cognateset)
    dt.col_defs()


def test_Meanings_error(configurator):
    dt = datatables.Meanings(get_current_request(), Parameter)

    with pytest.raises(IndexError):
        dt.col_defs()


def test_Meanings(configurator):
    class Meaning(CustomModelMixin, Parameter, models.MeaningMixin):
        pk = sa.Column(sa.Integer, sa.ForeignKey('parameter.pk'), primary_key=True)

    dt = datatables.Meanings(get_current_request(), Parameter)
    dt.col_defs()
