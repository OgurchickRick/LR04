import os

path = 'C:\\Obhod'


def obxodFile(path, level=1):
    print('Level=', level, 'Content:0', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


obxodFile(path)
