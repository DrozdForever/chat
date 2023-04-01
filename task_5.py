import subprocess


yandex = ['ping', 'yandex.ru']
yandex_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
for num,line in enumerate(yandex_ping.stdout):
    print(line.decode('utf-8'))
    if num == 3:
        break


youtube = ['ping', 'youtube.com']
youtube_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)

for num, line in enumerate(youtube_ping.stdout):
    print(line.decode('utf-8'))
    if num == 3:
        break
    
# P.S Я не понял сути задания. У меня данные поступают на английском, откуда взять кириллицу я не знаю.