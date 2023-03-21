from datetime import datetime
from os.path import join
from utils.utils import load_data
from utils.last_five_transactions import find_last_transactions
from utils.last_five_transactions import split_card_number


def main():
    """
    Просто выводит все в консоль
    """

    # Получили 5 последних транзакций
    last_transactions = find_last_transactions(load_data(join('..', 'data', 'operations.json')))

    # В одной итерации цикла распечатываем данные одной транзакции
    for i in range(len(last_transactions)):
        date = datetime.strptime(last_transactions[i]['date'].split('.')[0], "%Y-%m-%dT%H:%M:%S")

        print(f'{date.day}.{date.month}.{date.year} {last_transactions[i]["description"]}')

        if last_transactions[i]["description"] != "Открытие вклада":
            print(
                f'{last_transactions[i]["from"].split(" ")[0]} '
                f'{split_card_number(last_transactions[i]["from"].split(" ")[-1])} -> '
                f'Счет **{last_transactions[i]["to"].split(" ")[-1][-4:]}'
            )
        else:
            print(f'Счет **{last_transactions[i]["to"].split(" ")[-1][-4:]}')

        print(
            last_transactions[i]["operationAmount"]["amount"] + ' ' +
            last_transactions[i]["operationAmount"]["currency"]["name"]
        )
        print()


if __name__ == '__main__':
    main()
