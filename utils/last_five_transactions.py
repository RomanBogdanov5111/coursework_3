from datetime import datetime


def find_last_transactions(transactions_data: list) -> list:
    """
    Функция, которая принимает все данные о транзакциях в виде списка и возвращает список из пяти последних транзакций.
        Внутри основного цикла совершаем 5 итераций.
        Внутри каждой итерации проходим по всему списку, где в переменную "new_transaction" записывается сначала первый
    элемент списка операций "transactions_data", а потом путем сравнения "new_transaction" с текущим элементом списка
    "transactions_data" по времени, с помощью библиотеки "datetime", если текущий новее, чем "new_transaction",
    в "new_transaction" записывается значение текущего. В конце цикла значение "new_transaction" удаляется из
    "transactions_data" по индексу.
    :param transactions_data: Список словарей с данными о денежных переводах
    :return: Список из пяти последних денежных переводах
    """

    last_five_transactions = []
    for counter in range(5):
        new_transaction = transactions_data[0]
        index = 0

        for transaction in transactions_data:

            if datetime.strptime(transaction['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S") > \
               datetime.strptime(new_transaction['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S"):

                if transaction['state'] == 'EXECUTED':
                    new_transaction = transaction
                    index = transactions_data.index(transaction)

                else:
                    transactions_data.remove(transaction)

        last_five_transactions.append(transactions_data.pop(index))

    return last_five_transactions


def split_card_number(card_number: str) -> str:
    """
    Маскирует часть цифр номера банковской карты '*' и разбивает по блокам по 4 цифры.
    :param card_number: Номер банковской карты в виде строки.
    :return: Номер банковской карты, в виде строки, видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры.
    """

    new_card_number = [n for n in card_number]

    return ''.join(
        new_card_number[:4] + [' '] +
        new_card_number[4:6] + ['** **** '] +
        new_card_number[-4:]
    )


def print_last_transactions(last_five_transactions: list):
    """
    Просто выводит все в консоль
    :param last_five_transactions: Список словарей с данными о переводах
    """

    for i in range(5):
        date = datetime.strptime(last_five_transactions[i]['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S")

        print(f'{date.day}.{date.month}.{date.year} {last_five_transactions[i]["description"]}')

        if last_five_transactions[i]["description"] != "Открытие вклада":
            print(
                f'{last_five_transactions[i]["from"].split(" ")[0]} ' 
                f'{split_card_number(last_five_transactions[i]["from"].split(" ")[-1])} -> '
                f'Счет **{last_five_transactions[i]["to"].split(" ")[-1][-4:]}'
            )
        else:
            print(f'Счет **{last_five_transactions[i]["to"].split(" ")[-1][-4:]}')

        print(
              last_five_transactions[i]["operationAmount"]["amount"] + ' ' +
              last_five_transactions[i]["operationAmount"]["currency"]["name"]
        )
        print()
