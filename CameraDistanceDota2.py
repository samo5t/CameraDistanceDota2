import glob
import os
os.system("mode con cols=55 lines=30")

targetPattern = r"\**\**\**\common\dota 2 beta\game\dota\bin\win64\client.dll"

s = (b'\x00\x40\x9C\x44', #1250
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

    data = data.replace(b'\x00\x00\x96\x44',s[j])

    with open(disk, 'wb') as file:
        file.write(data)

def out_green(text):
    print("\033[32m {}" .format(text))

def out_red(text):
    print("\033[31m {}" .format(text))

def searchfile():
    disk = ['C:','D:','E:','F:','G:','D:','H:','I:']
    for i in range(len(disk)):
        if os.path.exists(disk[i] + str(glob.glob(targetPattern)[0]) ):
            return disk[i] + str(glob.glob(targetPattern)[0])
        else:
            return 0
print("Для успешного изменения необходимо, чтобы у вас был не модифицированный файл Client.dll\n (C)cmct_")
try:
    dir = searchfile()
except Exception:
    out_red('Client.dll not found')
else:
    print('Select camera distance\n'
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
    a = input()

try:
    redist(dir,int(a)-1)
except Exception:
    out_red('Неверное значение')
else:
    out_green("Success")
os.system("pause")