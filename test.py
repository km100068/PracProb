import matplotlib.pyplot as plt
import pandas as pd

from data_extractor import get_data_as_numpy_arrays

if __name__ == '__main__':
    dataset = get_data_as_numpy_arrays()

    x_value = []
    y_value = []
    for row in dataset:
        x_value.append(row[2])
        y_value.append(row[4])

    plt.scatter(x_value, y_value)
    plt.show()