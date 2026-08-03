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


def test_cognates(testapp):
    testapp.get_dt('/cognates')
    testapp.get_dt('/cognates?sSearch_0=m&sSearch_1=n&iSortingCols=1&iSortCol_0=0')
    testapp.get_dt('/cognates?iSortingCols=1&iSortCol_0=1')
    testapp.get_dt('/cognates?cognateset=1')
