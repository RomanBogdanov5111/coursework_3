from datetime import datetime


def find_last_transactions(transactions_data: list) -> list:
    """
    Функция, которая принимает все данные о транзакциях в виде списка и возвращает список из пяти последних транзакций.
        Внутри основного цикла совершаем 5 итераций.
        Внутри каждой итерации проходим по всему списку, где в переменную "new_transaction" записывается сначала первый
    элемент списка операций "transactions_data", а потом путем сравнения "new_transaction" с текущим элементом списка
    "transactions_data" по времени, с помощью библиотеки "datetime", если текущий новее, чем предыдущий
    в предыдущий записывается значение текущего. В конце цикла значение "new_transaction" удаляется из
    "transactions_data".
    Если на вход попадут данные не верного формата, вернет пустой список.
    :param transactions_data: Список словарей с данными о денежных переводах
    :return: Список данных с пятью последними денежными переводами.
    """

    if type(transactions_data) != list:
        return []

    counter = 5 if len(transactions_data) > 5 else len(transactions_data)
    last_five_transactions = []

    try:
        for i in range(counter):
            new_transaction = transactions_data[0]
            index = 0

            for transaction in transactions_data:

                if transaction['state'] == 'EXECUTED':

                    if datetime.strptime(transaction['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S") > \
                       datetime.strptime(new_transaction['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S"):

                        new_transaction = transaction
                        index = transactions_data.index(transaction)

            last_five_transactions.append(transactions_data.pop(index))
    except TypeError:
        return []
    except KeyError:
        return []

    return last_five_transactions


def split_card_number(card_number: str) -> str:
    """
    Принимает номер в виде "00000000000000000000" возвращает "0000 00** **** 0000"
    если номер карты не правильного формата, возвращает пустую строку.
    :param card_number: Номер банковской карты в виде строки.
    :return: Номер банковской карты, в виде строки, видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры.
    """

    if type(card_number) != str or len(card_number) < 15 or not card_number.isdigit():
        return ''

    new_card_number = [n for n in card_number]
    return ''.join(
        new_card_number[:4] + [' '] +
        new_card_number[4:6] + ['** **** '] +
        new_card_number[-4:]
    )
