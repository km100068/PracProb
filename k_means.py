
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

from data_extractor import get_data_as_numpy_arrays


def get_specific_data(dataset, user_id, column):
    result = []
    for row in dataset:
         # if row[0] == user_id:
         point = [row[2], row[3]]
         result.append(point)


    return result

def find_number_of_clusters(dataset):
    wcss_list = []  # Initializing the list for the values of WCSS
    # Using for loop for iterations from 1 to 10.
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=1)
        kmeans.fit(x)
        wcss_list.append(kmeans.inertia_)
    mtp.plot(range(1, 11), wcss_list)
    mtp.title('The Elbow Method Graph')
    mtp.xlabel('Number of clusters(k)')
    mtp.ylabel('wcss_list')
    mtp.show()


def draw_plot_scripy(whitened, mean_dist, centroids):
    w0 = whitened[mean_dist == 0]
    w1 = whitened[mean_dist == 1]
    w2 = whitened[mean_dist == 2]

    plt.plot(w0[:, 0], w0[:, 1], 'o', alpha=0.5, label='cluster 0')
    plt.plot(w1[:, 0], w1[:, 1], 'd', alpha=0.5, label='cluster 1')
    plt.plot(w2[:, 0], w2[:, 1], 's', alpha=0.5, label='cluster 2')

    plt.plot(centroids[:, 0], centroids[:, 1], 'k*', label='centroids')
    plt.legend(shadow=True)
    plt.xlabel('commits')
    plt.ylabel('additions')
    #plt.axis('equal')
    # plt.scatter(whitened[:, 0], whitened[:, 1])
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='r')
    plt.show()


def draw_plot_sklearn(x):
    # training the K-means model on a dataset
    kmeans = KMeans(n_clusters=3)
    y_predict = kmeans.fit_predict(x)

    mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s=100, c='blue', label='Cluster 1')  # for first cluster
    mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s=100, c='green', label='Cluster 2')  # for second cluster
    mtp.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s=100, c='red', label='Cluster 3')  # for third cluster
    mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroid')
    mtp.title('Clusters of customers')
    mtp.xlabel('Commits')
    mtp.ylabel('Deletions')
    mtp.legend()
    mtp.show()


if __name__ == '__main__':
    dataset = get_data_as_numpy_arrays()
    specific = get_specific_data(dataset, 14953, 2)
    #print(specific)
    whitened = whiten(specific)
    number = 3
    centroids, mean_dist = kmeans2(whitened, number)
    clusters, dist = vq(whitened, centroids)
    print(clusters)
    #print(whitened)
    draw_plot_scripy(whitened, mean_dist, centroids)
    in_0 = list(clusters).count(0)
    in_1 = list(clusters).count(1)
    in_2 = list(clusters).count(2)

    print(" In 0 cluster: " + str(in_0) + "\n In 1 cluster: " + str(in_1) + " \n In 2 cluster: " + str(in_2))
    dataset2 = pd.read_csv('./data/LinuxCommitData.csv')
    x = dataset2.iloc[:, [1, 3]].values
    find_number_of_clusters(dataset2)
    draw_plot_sklearn(x)





