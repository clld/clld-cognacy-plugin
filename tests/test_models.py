from clld_cognacy_plugin.models import Cognate


def test_Cognate(testapp):
    from clld.db.meta import DBSession

    cog = DBSession.query(Cognate).first()
    assert cog.id
