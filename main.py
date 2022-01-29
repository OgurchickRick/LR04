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


def duplicate(a):
    copies = {}
    for key1 in a:
        for key2 in a:
            if key1 == key2:
                pass
            elif key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and a[key1] == a[key2]:
                if key1 in copies:
                    continue
                copies.update({key1: a[key1]})
    else:
        return copies


def print_duplicate(copies):
    hlam = []
    for key1 in copies:
        if key1 not in hlam:
            print('\n', '-----', os.path.getsize(key1), 'байт -----')
            print(key1)
            for key2 in copies:
                if key1 == key2:
                    pass
                elif key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and copies[key1] == copies[key2]:
                    print(key2)
                    hlam.append(key2)


if __name__ == '__main__':
    p = path()
    s = dictionary(p)
    duplicate(s)
    d = duplicate(s)
    print(print_duplicate(d))

