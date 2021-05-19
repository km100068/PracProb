from numpy import longlong, linspace
from dataset import Dataset
from regression import Regression
from data_extractor import get_data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    linux_data = get_data()

    ids = set(map(lambda item: item['id'], linux_data))

    d = Dataset(linux_data)

    x = list(map(lambda item: item.timestamp(), d.get_date_all()))
    y = list(d.get_adc_coefficient_all())

    avg_point = len(x) // 2

    train_x = longlong(x[:avg_point])
    train_y = longlong(y[:avg_point])

    test_x = longlong(x[avg_point:len(x)])
    test_y = longlong(y[avg_point:len(y)])

    r = Regression(train_x, train_y, 3)

    sample_x = linspace(train_x[0], train_x[-1], len(train_x))
    plt.title(str(r.polynomial))
    plt.gcf().set_size_inches(10,8)
    plt.gca().set_ylim([-10000, 10000])
    plt.plot(sample_x, r(sample_x))
    plt.scatter(train_x, train_y, s=1, c='red')
    plt.scatter(test_x, test_y, s=1, c='red')
    plt.scatter(test_x, r(test_x), s=1, c='yellow')
    plt.savefig(f'./plots/allplot.png')
    # plt.show()

    # fig, axs = plt.subplots(10, 10, figsize=(50,50))
    #
    # for index, user_id in enumerate(ids):
    #     print(user_id)
    #     all_x = list(map(lambda item: int(item.timestamp()), d.get_date_by_user_id(user_id)))
    #     all_y = list(d.get_adc_coefficient_by_user_id(user_id))
    #
    #     avg_point_index = int(len(all_x) * .8)
    #
    #     train_x = longlong(all_x[:avg_point_index])
    #     train_y = longlong(all_y[:avg_point_index])
    #
    #     test_x = longlong(all_x[avg_point_index:-1])
    #     test_y = longlong(all_y[avg_point_index:-1])
    #
    #     r = Regression(train_x, train_y, 1)
    #
    #     sample_x = linspace(train_x[0], train_x[-1], len(train_x))
    #
    #     axs[index // 10, index % 10].title.set_text(str(user_id))
    #     axs[index // 10, index % 10].plot(sample_x, r(sample_x))
    #     axs[index // 10, index % 10].scatter(train_x, train_y, s=1, c='red')
    #     axs[index // 10, index % 10].scatter(test_x, test_y, s=1, c='red')
    #     axs[index // 10, index % 10].scatter(test_x, r(test_x), s=1, c='yellow')
    #
    # for i in range(10):
    #     axs[i, 0].set_ylabel('Coefficient')
    #     axs[9, i].set_xlabel('Unix time [s]')
    #
    plt.savefig(f'./plots/allplot.png')
    # plt.clf()
