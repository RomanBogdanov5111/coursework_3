from os.path import join
from utils.utils import load_data
from utils.last_five_transactions import find_last_transactions
from utils.last_five_transactions import output_data


def main():
    """Просто все печатаем"""
    for data in output_data(find_last_transactions(load_data(join('..', 'data', 'operations.json')))):

        print(data['date'])
        print(data['from_to'])
        print(data['amount_and_name'])
        print()


if __name__ == '__main__':
    main()
