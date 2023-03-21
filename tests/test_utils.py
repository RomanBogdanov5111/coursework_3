from utils.utils import load_data
import pytest


@pytest.mark.parametrize('path,result', [
    ('qweqwe', "Неверный путь до файла!"),
    (123, "Неверный путь до файла!"),
    ([], "Неверный путь до файла!"),
    (1.286, "Неверный путь до файла!"),
])
def test_load_data(path, result):
    assert load_data(path) == result
