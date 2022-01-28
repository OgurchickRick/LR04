import os
import collections


def path():
    while True:
        way = str(input('Введите путь до папки:'))
        if os.path.exists(way):
            return way
        else:
            print("Неверный путь")


def dictionary(way, a={}):
    for filename in os.listdir(way):
        if os.path.isdir(way + '\\' + filename):
            dictionary(way + '\\' + filename)
        else:
            a.update({way + '\\' + filename: os.path.getsize(way + '\\' + filename)})
    return a


def duplicate(a, b):
    keys = list(a)
    names = []
    for i in a.keys():
        names.append(i[i.rfind('\\')+1:])

    print(keys)
    print(names)




def print_duplicate():
    pass


if __name__ == '__main__':
    p = path()
    s = dictionary(p)
    duplicate(s, p)
