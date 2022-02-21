from bbquote.api import get_quote



def test_quote():

    result = get_quote()

    assert type(result) == str
    assert len(result) > 0
