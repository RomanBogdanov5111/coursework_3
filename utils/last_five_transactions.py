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


def output_data(last_transactions: list) -> list:
    """
    Функция принимает данные последних пяти операций и приводит их в состояние, готовое для вывода пользователю.
    :param last_transactions: Список словарей с данными последних пяти транзакций
    :return: Список словарей с данными последних пяти транзакций, подготовленных для вывода на экран
    """

    if type(last_transactions) != list or len(last_transactions) == 0:
        return []

    # Новый список, который вернет функция
    new_last_transactions = []
    try:
        # Цикл, в каждой итерации которого, создается словарь внутри списка "new_last_transactions"
        for index in range(len(last_transactions)):

            # Создали пустой словарь. Преобразовали дату в понятный для питона вид и записали в переменную
            new_last_transactions.append({})
            date = datetime.strptime(last_transactions[index]['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S")

            # Создали ключ 'date', записали по нему дату и описание перевода
            new_last_transactions[index]['date'] = f'{date.day}.{date.month}.{date.year} ' \
                                                   f'{last_transactions[index]["description"]}'

            # Если описание перевода не "Открытие вклада" создали ключ "from_to", записали в него номер отправителя
            # и получателя
            if last_transactions[index]["description"] != "Открытие вклада":

                new_last_transactions[index]['from_to'] = \
                    f'{last_transactions[index]["from"].split(" ")[0]} ' \
                    f'{split_card_number(last_transactions[index]["from"].split(" ")[-1])} -> ' \
                    f'Счет **{last_transactions[index]["to"].split(" ")[-1][-4:]}'

            # Если операция "открытие вклада" записывается только номер карты получателя
            else:
                new_last_transactions[index]['from_to'] = f'Счет **{last_transactions[index]["to"].split(" ")[-1][-4:]}'

            # Создали ключ "amount_and_name", записали в него сумму и валюту перевода
            new_last_transactions[index]['amount_and_name'] = \
                f'{last_transactions[index]["operationAmount"]["amount"]} ' \
                f'{last_transactions[index]["operationAmount"]["currency"]["name"]}'
    except KeyError:
        return []
    except TypeError:
        return []

    return new_last_transactions
