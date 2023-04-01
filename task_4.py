word_list = ['разработка', 'администрирование', 'protocol', 'standard']

byte_list = [w.encode('utf-8') for w in word_list]
print(byte_list)

word_list = [b.decode('utf-8') for b in byte_list]
print(word_list) 