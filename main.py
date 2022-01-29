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
    copies = {}
    names = {}
    d = []
    for key1 in a:
        for key2 in a:
            if key1 == key2:
                pass
            elif key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and a[key1] == a[key2]:
                if key1 in copies:
                    continue
                copies.update({key1: a[key1]})

    else:
        for name in copies:
            name = name[name.rfind('\\'):]
            d.append(name)
        for i in sorted(d):
            names.update({i: copies[i]})
        print(names)
        print(*copies, sep='\n')
        return copies


def print_duplicate():
    pass


if __name__ == '__main__':
    p = path()
    s = dictionary(p)
    duplicate(s, p)
