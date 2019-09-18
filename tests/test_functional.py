import pytest


@pytest.mark.parametrize(
    "url,content",
    [
        ('/cognatesets', 'Cognatesets'),
        ('/cognatesets/1', 'cs: test'),
        ('/cognatesets/1.geojson', 'cs: test'),
    ])
def test_url(testapp, url, content):
    res = testapp.get(url)
    assert content in res.body.decode('utf8')
