from zope.interface import implementer
import sqlalchemy as sa
import sqlalchemy.orm  # noqa: F401

from clld.db.meta import Base, PolymorphicBaseMixin
from clld.db.models.common import (
    Contribution, Value,
    IdNameDescriptionMixin, HasDataMixin, HasFilesMixin, HasSourceMixin, DataMixin,
    FilesMixin,
)
from clld_cognacy_plugin.interfaces import ICognateset


class MeaningMixin(object):
    concepticon_id = sa.Column(sa.Integer)


class Cognateset_data(Base, DataMixin):
    pass


class Cognateset_files(Base, FilesMixin):
    pass


@implementer(ICognateset)
class Cognateset(Base,
                 PolymorphicBaseMixin,
                 IdNameDescriptionMixin,
                 HasDataMixin,
                 HasFilesMixin):
    contribution_pk = sa.Column(sa.Integer, sa.ForeignKey('contribution.pk'))
    contribution = sa.orm.relationship(Contribution, backref='cognatesets')


class Cognate(Base):
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


class CognateReference(Base, HasSourceMixin):
    cognate_pk = sa.Column(sa.Integer, sa.ForeignKey('cognate.pk'))
    cognate = sa.orm.relationship(Cognate, backref="references")


class CognatesetReference(Base, HasSourceMixin):
    cognateset_pk = sa.Column(sa.Integer, sa.ForeignKey('cognateset.pk'))
    cognateset = sa.orm.relationship(Cognateset, backref="references")
