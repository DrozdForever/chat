from chardet import detect

with open('test_file.txt', 'rb') as file:
    for line in file:
        print(detect(line)) # У меня utf-8. Пользуюсь Ubuntu

with open('test_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line) # Всё в порядке, как и ожидалось