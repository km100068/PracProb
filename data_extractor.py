from typing import List, TypedDict
import csv

from datetime import date as Date


class User(TypedDict):
    date: Date
    commits: int
    additions: int
    deletions: int
    id: int


def get_data() -> List[User]:
    with open('./data/LinuxCommitData.csv', 'r') as f:
        reader = csv.reader(f)

        res: List[User, ...] = list()

        for row in reader:
            date_details = list(map(int, row[0].split(' ')[0].split('/')))
            date = Date(date_details[2], date_details[0], date_details[1])

            res.append({
                'date': date,
                'commits': int(row[1]),
                'additions': int(row[2]),
                'deletions': int(row[3]),
                'id': int(row[4]),
            })

        return res


if __name__ == '__main__':
    for rec in get_data():
        print(rec)
