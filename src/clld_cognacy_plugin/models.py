"""
Models
"""
from zope.interface import implementer
import sqlalchemy as sa
import sqlalchemy.orm  # noqa: F401  # pylint: disable=W0611

from clld.db.meta import Base, PolymorphicBaseMixin
from clld.db.models.common import (
    Contribution, Value,
    IdNameDescriptionMixin, HasDataMixin, HasFilesMixin, HasSourceMixin, DataMixin,
    FilesMixin,
)
from clld_cognacy_plugin.interfaces import ICognateset, ICognate


class MeaningMixin:  # pylint: disable=R0903
    """Add Concepticon mapping."""
    concepticon_id = sa.Column(sa.Integer)


class Cognateset_data(Base, DataMixin):  # pylint: disable=C0103
    """Data properties of a cognate set."""


class Cognateset_files(Base, FilesMixin):  # pylint: disable=C0103
    """Files related to a cognate set."""


@implementer(ICognateset)
class Cognateset(Base,
                 PolymorphicBaseMixin,
                 IdNameDescriptionMixin,
                 HasDataMixin,
                 HasFilesMixin):
    """A cognate set object."""
    contribution_pk = sa.Column(sa.Integer, sa.ForeignKey('contribution.pk'))
    contribution = sa.orm.relationship(Contribution, backref='cognatesets')


@implementer(ICognate)
class Cognate(Base, PolymorphicBaseMixin):
    """
    The association table between counterparts for concepts in particular languages and
    cognate sets.
    """
    cognateset_pk = sa.Column(sa.Integer, sa.ForeignKey('cognateset.pk'))
    cognateset = sa.orm.relationship(Cognateset, backref='cognates')
    counterpart_pk = sa.Column(sa.Integer, sa.ForeignKey('value.pk'))
    counterpart = sa.orm.relationship(Value, backref='cognates')
    doubt = sa.Column(sa.Boolean, default=False)
    alignment = sa.Column(sa.Unicode)


class CognateReference(Base, HasSourceMixin):  # pylint: disable=C0115
    cognate_pk = sa.Column(sa.Integer, sa.ForeignKey('cognate.pk'))
    cognate = sa.orm.relationship(Cognate, backref="references")


class CognatesetReference(Base, HasSourceMixin):  # pylint: disable=C0115
    cognateset_pk = sa.Column(sa.Integer, sa.ForeignKey('cognateset.pk'))
    cognateset = sa.orm.relationship(Cognateset, backref="references")
