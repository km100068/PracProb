import numpy
from typing import List
from data_extractor import get_data_as_numpy_arrays
from datetime import datetime


def ten_most_active(lista) -> List[numpy.longlong]:
    res: List[numpy.longlong, ...] = list()
    x = get_data_per_user(lista)
    y = sorted(x, key=lambda x: x[1])

    for i in y :
        res.append(numpy.longlong([
            i[0],
            i[1],
            i[2],
            i[3]
        ]))
    del res[10:]
    return res


def get_data_per_user(lista) -> List[numpy.longlong]:
    res: List[numpy.longlong, ...] = list()

    for row in lista:
        res.append(numpy.longlong([
            row[0],
            0,
            0,
            0
        ]))

    l1 = numpy.unique(res, axis=0)

    res: List[numpy.longlong, ...] = list()
    for i in l1:
        commit = 0
        addition = 0
        deletion = 0
        for j in lista:

            if i[0] == j[0]:
                commit = commit + j[2]
                addition = addition + j[3]
                deletion = deletion + j[4]
        res.append(numpy.longlong([
            i[0],
            commit,
            addition,
            deletion
        ]))

    return res


def average_commit_time(lista):
    f = lista
    sorted_multi_list = sorted(f, key=lambda x: x[1])
    c = 0
    r1 = datetime.fromtimestamp(sorted_multi_list[0][1])
    r2 = datetime.fromtimestamp(sorted_multi_list[-1][1])
    l = (r2 - r1).total_seconds()

    x = get_all_commits(lista)

    y = l / x[0]

    return y


def get_average_commit(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[2]
    n = n / len(x)

    return n


def get_average_addition(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[3]
    n = n / len(x)

    return n


def get_average_deletion(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[4]
    n = n / len(x)

    return n


def get_all_commits(lista):
    x = get_data_per_user(lista)
    c = 0
    c1 = 0
    c2 = 0
    for i in x:
        c = c + i[1]
        c1 = c1 + i[2]
        c2 = c2 + i[3]
    return [c, c1, c2]


def get_average_commit_(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[1]

    n = n / 10

    return n


def get_average_addition_(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[2]

    n = n / 10

    return n


def get_average_deletion_(lista):
    n = 0
    x = lista
    for i in x:
        n = n + i[3]

    n = n / 10

    return n


def date_filter(start, end):
    x = get_data_as_numpy_arrays()
    res: List[numpy.longlong, ...] = list()
    for i in x:
        if datetime.fromtimestamp(i[1]) > start and datetime.fromtimestamp(i[1]) < end:
            res.append(numpy.longlong([
                i[0],
                i[1],
                i[2],
                i[3],
                i[4]
            ]))
    return res


x = datetime(2016, 12, 31)
y = datetime(2013, 1, 1)
get_data_per_user(date_filter(y, x))

g = date_filter(y, x)
h = ten_most_active(g)
print(g)
print("średni czas")

print("średnie komity dla usera")
print(get_average_commit(g))
print("średnie additions dla usera")
print(get_average_addition(g))
print("średnie deletions dla usera")
print(get_average_deletion(g))
print("średnie komity dla top 10")
print(get_average_commit_(h))
print("średnie additons dla top 10")
print(get_average_addition_(h))
print("średnie deletions dla top 10")
print(get_average_deletion_(h))
