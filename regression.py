from typing import Union
from numpy import poly1d, polyfit, longlong, linspace, ndarray
from dataset import Dataset
from data_extractor import get_data
import matplotlib.pyplot as plt


class Regression:
    def __init__(self, x: longlong, y: longlong, deg: int):
        self.polynomial = poly1d(polyfit(x, y, deg))

    def __call__(self, x: Union[int, float, longlong, ndarray]):
        return self.polynomial(x)


if __name__ == "__main__":
    d = Dataset(get_data())

    x = longlong(list(map(lambda item: int(item.timestamp()), d.get_date_by_user_id(701714)))[:100])

    y = longlong(d.get_adc_coefficient_by_user_id(701714)[:100])

    regression = Regression(x, y, 5)

    plt.scatter(x, y, s=1, c='red')

    print(x[0])
    print(x[-1])

    sample_x = linspace(x[0], x[-1], len(x))

    plt.plot(sample_x, regression(sample_x))

    plt.show()