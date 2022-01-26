import os


def path():
    while True:
        way = str(input('Введите путь до папки:'))
        if os.path.exists(way) is True:
            return way
        else:
            print("Неверный путь")


def dictionary(way):
    a = {}
    for filename in os.listdir(way):
        a.update({way + '\\' + filename: os.path.getsize(way + '\\' + filename)})
    print(a)


def duplicate():
    pass


def print_duplicate():
    pass


if __name__ == '__main__':
    p = path()
    dictionary(p)
