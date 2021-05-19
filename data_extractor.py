import csv
from datetime import datetime
from typing import List, TypedDict

import numpy

"""
Typed dictionary for row representation as a user
"""


class User(TypedDict):
    date: datetime
    commits: int
    additions: int
    deletions: int
    id: int


"""
Extracts data as a list of User objects
"""


def get_data() -> List[User]:
    with open('./data/LinuxCommitData.csv', 'r') as f:
        reader = csv.reader(f)

        res: List[User, ...] = list()

        for row in reader:
            date_details = list(map(int, row[0].split(' ')[0].split('/')))
            date = datetime(date_details[2], date_details[0], date_details[1])
            if 2013 <= date_details[2] <= 2017:
                res.append({
                    'date': date,
                    'commits': int(row[1]),
                    'additions': int(row[2]),
                    'deletions': int(row[3]),
                    'id': int(row[4]),
                })


        return res


"""
Extracts data as a list of numpy.longlong arrays
"""


def get_data_as_numpy_arrays() -> List[numpy.longlong]:
    with open('./data/LinuxCommitData.csv', 'r') as f:
        reader = csv.reader(f)

        res: List[numpy.longlong, ...] = list()

        for row in reader:
            date_details = list(map(int, row[0].split(' ')[0].split('/')))
            if 2013 <= date_details[2] <= 2016:
                res.append(numpy.longlong([
                    row[4],
                    datetime(date_details[2], date_details[0], date_details[1]).timestamp(),
                    row[1],
                    row[2],
                    row[3]
                ]))


        return res


if __name__ == '__main__':
    for rec in get_data():
        print(rec)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for rec in get_data_as_numpy_arrays():
        print(rec)
