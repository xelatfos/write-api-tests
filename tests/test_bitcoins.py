import pytest
import requests
import time


def get_pairs():
    objects = []
    pairs = [
        "tBTCUSD",
        "tLTCUSD",
        "tETHUSD"
    ]
    if len(pairs) < 25:
        timeout = 2
    else:
        timeout = 3
    for pair in pairs:
        req = requests.get(F"https://api-pub.bitfinex.com/v2/ticker/{pair}")
        objects.append(req)
        time.sleep(timeout)
    return objects

pairs = get_pairs()
@pytest.mark.parametrize("raw", pairs, ids = [str(x) for x in pairs])
class TestRequests:
    def test_code(self, raw):
        assert raw.status_code == 200, "Код выполнения запроса не 200"

    def test_values_count(self, raw):
        data = raw.json()
        assert len(data) == 10, "В объекте не 10 значений"

    def test_types(self, raw):
        data = raw.json()
        for value in data:
            assert isinstance(value, (int, float)), "Одно из значений объекта - не числовое"
