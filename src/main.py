from os.path import join
from utils.utils import load_data
from utils.last_five_transactions import find_last_transactions
from utils.last_five_transactions import print_last_transactions


def main():
    # Загрузили данные из файла
    data = load_data(join('..', 'data', 'operations.json'))
    # Нашли последние 5 и распечатали
    print_last_transactions(find_last_transactions(data))


if __name__ == '__main__':
    main()




