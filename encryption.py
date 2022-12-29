from modules import *

# основная функция шифровки по битам

def bin_encrypt(bin_contain: list):
    DataList = read_data()
    preblock_list = convert_to_8bits(bin_contain) # преобразуем входные данные, которые могут быть и 6 и 7 бит к одному стандарту
                                                  # - 8 битам. для этого добавляем ничего не значащие нули в начало.
    enc_result = []
    for preblock in preblock_list:
        # убираем префикс - первые два бита
        prefix = preblock[0:2]
        # работаем с оставшимися 6 битами (это и есть блок, внутри которого будут перестановки
        block = preblock[2:8]
        s_string = int((block[4] + block[1]), 2)  # 2 бита - 5 и 2 (задание из варианта
        s_collumn = int(block[0] + block[2] + block[3] + block[5], 2)  # 4 оставшихся
        value = int(DataList[s_string][s_collumn])  # вычисляем номер строки и столбца
        bin_value = value_to_bin(value) # преобразуем в бинарный код
        enc_block = prefix + block[4] + block[1] + bin_value # записываем сначала удаленный префикс, чтобы длина соответствовала 8 битам.
                                                             # потом 5 бит, 1ый и значение из s - таблицы.
        enc_result.append(enc_block)

    return enc_result


def main_encrypt():

    # DataList = read_data()

    path_to_file = input("Введите путь к файлу, который хотите зашифровать: \n")
    file_contain = open_file(path_to_file)  # bytearray
    bin_contain = transform_to_bin(file_contain)  # string bin

    bin_encrypted = bin_encrypt(bin_contain)  # строка с зашифрованным бинарником

    result_encrypyion = transform_to_bytes(bin_encrypted)  # преобразование в bytearray
    write_to_file(path_to_file, result_encrypyion)  # запись в файл
