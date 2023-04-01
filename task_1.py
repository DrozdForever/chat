word_list = ['разработка', 'сокет', 'декоратор']

for word in word_list:
    print(f'{word} - это {type(word)}')

byte_list = [w.encode('utf-8') for w in word_list]

for byte in byte_list:
    print(f'{byte} - это {type(byte)}')