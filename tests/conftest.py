from urllib.request import urlopen
import pytest


@pytest.fixture(autouse=True)
def internet_check():
    try:
        urlopen("https://google.com", timeout=2)
    except Exception as e:
        print('Check Your Internet Connection Anil', e, type(e), e.args)
