from modules import *


def bin_decrypt(bin_contain):
    DataList = read_data()
    block_list_encrypted = convert_to_8bits(bin_contain) # так же приводим к виду 8 бит, дополняем нулями
    block_list_decrypted = []

    for preblock in block_list_encrypted:
        prefix = preblock[0:2] # как и в функции шифровки, выделяем первые 2 бита
        block = preblock[2:8] # выделяем блок из оставшихся 6 битов

        s_string = int(block[0] + block[1], 2) # первые два бита в шифрованном бинаре будет 5 и 2
        s_value = int(block[2:6], 2) # оставшиеся - значение из s - таблицы

        kostyl = str(s_value) + '\n'

        for pos, val in enumerate(DataList[s_string]): # ищем значение в s - таблице и определяем колонку.
            if val == str(s_value) or val == kostyl:
                s_collumn = int(pos)


        bin_col = value_to_bin(s_collumn) # преобразуем значение в бинар

        block_decrypted = prefix + bin_col[0] + block[1] + bin_col[1] + bin_col[2] + block[0] + bin_col[3] # записываем все в обратном порядке
        block_list_decrypted.append(block_decrypted)




    return block_list_decrypted


def main_decrypt():
    path_to_file = input("Введите путь к файлу, который хотите расшифровать: \n")
    file_contain = open_file(path_to_file)  # список байт
    bin_contain = transform_to_bin(file_contain)  # список строковый (двоичный) (8)
    bin_decrypted = bin_decrypt(bin_contain)
    result_decrypyion = transform_to_bytes(bin_decrypted)
    write_to_file(path_to_file, result_decrypyion)
