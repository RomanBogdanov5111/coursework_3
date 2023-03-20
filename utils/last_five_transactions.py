from datetime import datetime


def find_them(transactions_data: list) -> list:
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


def format_them():
    pass


def print_them():
    pass
