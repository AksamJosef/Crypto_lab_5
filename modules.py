def read_data():
    DataList = []
    with open("data.txt", 'r') as Data:
        for el in range(4):
            tempDataList = Data.readline().split(' ')
            DataList.append(tempDataList)
    return DataList


def open_file(path_to_file):
    with open(path_to_file, 'rb') as SFile:  # открываем файл для чтения побайтово
        FileContain = bytearray(SFile.read())  # создаем байтовый массив

    return FileContain


def transform_to_bytes(prepared_list):
    byte_list = []
    for el in prepared_list:
        byte_list.append(int(el, 2))

    return bytearray(byte_list)


def write_to_file(path_to_file, ToFile):
    with open(path_to_file, "wb") as OFile:
        OFile.write(ToFile)
        print("Программа завершена успешно")


def delete_0b(nfromatted_list: list):
    formatted = []

    for el in nfromatted_list:
        formatted.append(el.replace('0b', ''))

    return formatted


def value_to_bin(value):
    bin_value = bin(value).replace('0b', '')
    while len(bin_value) < 4:
        bin_value = '0' + bin_value
    return bin_value


def transform_to_bin(file_contain):
    temp = []
    for el in file_contain:
        temp.append(bin(el))

    result = delete_0b(temp)

    return result


def convert_to_8bits(file_contain: list):
    converted_list = []
    for el in file_contain:
        if len(el) != 8:
            temp = (8-len(el)) * '0' + el
            converted_list.append(temp)
        else:
            converted_list.append(el)
    return converted_list

