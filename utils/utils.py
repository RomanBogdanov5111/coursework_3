import json


def load_data(path: str, default="Неверный путь до файла!"):
    """
    Функция принимает в виде строки путь до файла ".json"
    и возвращает данные из этого файла в формате python.
    Если путь до файла не корректный вернет строку: "Неверный путь до файла!"
    :param path: Строка, путь до файла
    :param default: Значение по умолчанию
    :return: Данные из этого файла в формате python
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return default
    except TypeError:
        return default
    except OSError:
        return default
