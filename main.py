from encryption import *
from decryption import *
from modules import *


if __name__ == '__main__':

    print("Приветствую. Эта программа шифрует и дешифрует файлы, используя блочный шифр. \nВ данном примере мы используем блок "
          "S6, а так же значения a == 5, b == 2 \n")
    selected = input("Введите опцию, которую хотите выбрать: \n"
                     "1. Шифровка\n"
                     "2. Дешифровка\n")

    DataList = read_data()

    if selected == '1':
        main_encrypt()
    if selected == '2':
        main_decrypt()
