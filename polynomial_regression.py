import numpy
import numpy as numpy
from numpy import poly1d, polyfit, linspace, longlong
import matplotlib.pyplot as plt

from data_extractor import get_data, get_data_as_numpy_arrays

attributes_dict = {
    'id': 0,
    'time': 1,
    'commits': 2,
    'additions': 3,
    'deletions': 4
}


def get_polynomial(x: longlong, y: longlong, deg: int) -> poly1d:
    return poly1d(polyfit(x, y, deg))


def plot_chart(x: longlong, polynomial: poly1d) -> None:
    plt.plot(x, polynomial)
    plt.show()


def get_column_values(data, attribute_name, user_id=None) -> longlong:
    # result_list = []
    # column_num = attributes_dict[attribute_name]
    # for row in data:
    #     if user_id is not None:
    #         if row[0] == user_id:
    #             result_list.append(row[column_num])
    #     else:
    #         result_list.append(row[column_num])
    # return longlong(result_list)
    return longlong(list(map(lambda item: item[attributes_dict[attribute_name]], data)))


if __name__ == "__main__":
    # dataset = get_data()

    dataset = get_data_as_numpy_arrays()

    filtered = sorted(list(filter(lambda item: item[attributes_dict['id']] == 65151, dataset)), key=lambda item: item[1])

    # ids = set(map(lambda item: item['id'] == 701714, dataset))

    # print('records', len(dataset))
    # print('users', len(ids))

    # dataset = get_data_as_numpy_arrays()

    x_values = get_column_values(filtered, 'time', 65151)
    y_values = (numpy.array(get_column_values(filtered, 'additions', 65151) - numpy.array(
        get_column_values(filtered, 'deletions', 65151)))) / numpy.array(get_column_values(filtered, 'commits', 65151))


    _x = longlong(linspace(x_values[0], x_values[-1], len(y_values)))

    plt.scatter(x_values, y_values, s=1, c='red')
    plot_chart(_x, get_polynomial(x_values, y_values, 9)(_x))
