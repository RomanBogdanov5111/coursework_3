from utils.last_five_transactions import find_last_transactions
from utils.last_five_transactions import split_card_number
import pytest


@pytest.mark.parametrize('data,result', [
    ([{"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"},
      {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
      {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"},
      {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
      {"state": "EXECUTED", "date": "2018-10-14T22:27:25.205631"},
      {"state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
      {"state": "EXECUTED", "date": "2018-04-04T17:33:34.701093"}
      ], [
         {'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824'},
         {'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
         {'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230'},
         {'state': 'EXECUTED', 'date': '2018-11-29T07:18:23.941293'},
         {'state': 'EXECUTED', 'date': '2018-10-14T22:27:25.205631'}]),

    ([{"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"},
      {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
      {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"}
      ], [
         {"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"},
         {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
         {"state": "EXECUTED", "date": "2019-07-12T20:41:47.882230"}]),

    ([{"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"}
      ], [
         {"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"}]),

    ([], []),
    (12314, []),
    ([{'q': 343}], []),
    ("word", []),
    ({'q': 'word'}, [])
])
def test_find_last_transactions(data, result):
    assert find_last_transactions(data) == result


@pytest.mark.parametrize('number,res', [
    ("78808375133947439319", "7880 83** **** 9319"),
    ('', ''),
    ('15151', ''),
    ('dd445ssd', ''),
    (15, ''),
])
def test_split_card_number(number, res):
    assert split_card_number(number) == res
