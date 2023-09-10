import os
import time
import configparser
import sys

os.system("mode con cols=115 lines=30")
config = configparser.ConfigParser()
config.read("settings.ini")
d = config["path"]["directory"]
print('╔═══╗╔═══╗╔═══╗\n'
      '╚╗╔╗║║╔═╗║║╔══╝\n'
'─║║║║║║─╚╝║╚══╗\n'
'─║║║║║║─╔╗║╔══╝\n'
'╔╝╚╝║║╚═╝║║║───\n'
'╚═══╝╚═══╝╚╝───\n')
print(config["path"]["directory"])
print("Для успешного изменения необходимо, чтобы у вас был не модифицированный файл Client.dll\n" 
      "Используйте ваш путь к игре в файле settings.ini /**/steamapps/common/dota 2 beta/game/dota/bin/win64/\n" 
      "(C)cmct_\n")
print('Выберете номер в списке соответсвующей желаемому значению\n'
          ' 1) 1250\n'
          ' 2) 1300\n'
          ' 3) 1350\n'
          ' 4) 1400\n'
          ' 5) 1450\n'
          ' 6) 1500\n'
          ' 7) 1550\n'
          ' 8) 1600\n'
          ' 9) 1650\n'
          '10) 1700\n'
          '11) 1750\n'
          '12) 1800\n'
          '13) 1850\n'
          '14) 1900\n'
          '15) 1950\n'
          '16) 2000\n')
s = (b'\x00\x40\x9C\x44',
     b'\x00\x80\xA2\x44',
     b'\x00\xC0\xA8\x44',
     b'\x00\x00\xAF\x44',
     b'\x00\x40\xB5\x44',
     b'\x00\x80\xBB\x44',
     b'\x00\xC0\xC1\x44',
     b'\x00\x00\xC8\x44',
     b'\x00\x40\xCE\x44',
     b'\x00\x80\xD4\x44',
     b'\x00\xC0\xDA\x44',
     b'\x00\x00\xE1\x44',
     b'\x00\x40\xE7\x44',
     b'\x00\x80\xED\x44',
     b'\x00\xC0\xF3\x44',
     b'\x00\x00\xFA\x44')
def redist(disk,j):
    with open(disk, 'rb') as file:
        data = file.read()
    data = bytearray(data)

    # Находим пятую позицию для замены
    fifth_occurrence = 0
    position = -1

    while fifth_occurrence < 5:
        position = data.find(b'\x00\x00\x96\x44', position + 1)
        if position == -1:
            break
        fifth_occurrence += 1

    if fifth_occurrence == 5 and position != -1:
        # Заменяем пятое вхождение
        data[position:position + 4] = s[j]

    with open(disk, 'wb') as file:
        file.write(data)


def loading_bar(duration):
    total_width = 40
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        fraction = (time.time() - start_time) / duration
        width = int(total_width * fraction)
        bar = '[' + '=' * width + ' ' * (total_width - width) + ']'
        sys.stdout.write('\r' + bar)
        sys.stdout.flush()
        time.sleep(0.1)

def out_green(text):
    print("\033[32m {}" .format(text))

def out_red(text):
    print("\033[31m {}" .format(text))


a = input()

try:
    redist(config["path"]["directory"], int(a) - 1)
except Exception:
    out_red('Неверное значение или путь')
else:
    out_green("Успешно\n")
print('Закрытие через 3 секунды\n')
loading_duration = 3
loading_bar(loading_duration)
