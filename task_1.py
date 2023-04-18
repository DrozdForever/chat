"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:

    a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
    данными, их открытие и считывание данных. В этой функции из считанных данных
    необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
    каждого параметра поместить в соответствующий список. Должно получиться четыре
    списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
    функции создать главный список для хранения данных отчета — например, main_data
    — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
    системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
    столбцов также оформить в виде списка и поместить в файл main_data (также для
    каждого файла);

    b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
    функции реализовать получение данных через вызов функции get_data(), а также
    сохранение подготовленных данных в соответствующий CSV-файл;

    c. Проверить работу программы через вызов функции write_to_csv()
"""
import re
import csv
import chardet


# Решил добавить функцию конвертации,
# так как на линукс предоставленные данные не считываются и возникает ошибка
def encoding_convert(input_file):
    with open(input_file, 'rb') as f:
        content_bytes = f.read()
    detected = chardet.detect(content_bytes)
    encoding = detected['encoding']
    data = content_bytes.decode(encoding)
    return data


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        data = encoding_convert(f'data/info_{i}.txt')

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s\S*')
        os_name_list.append(os_name_reg.findall(data)[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for i in range(3):
        row_data = []
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)
    return main_data
    

def write_to_csv(out_file):
    """Запись данных в csv"""

    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for row in main_data:
            writer.writerow(row)


if __name__ == '__main__':
    write_to_csv('data/final_data.csv')
