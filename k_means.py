
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2

#whiten(obs[, check_finite]) - Normalize a group of observations on a per feature basis.
#whiten - must be called prior to passing an observation matrix to kmeans.

# whitened = whiten(data)


#kmeans(obs, k_or_guess[, iter, thresh, …]) - Performs k-means on a set of observation vectors forming k clusters.
#obs - Each row of the M by N array is an observation vector. The columns are ->
# the features seen during each observation.


#k_or_guess - The number of centroids to generate. A code is assigned to each centroid, which is also the row index of the centroid in the code_book matrix generated.
# scipy_centers,_ = kmeans(whitened, 3) #musimy tu podać liczbę klasterow na jakie chcemy podzielić



#vq(obs, code_book[, check_finite]) - Assign codes from a code book to observations.

#kmeans2(data, k[, iter, thresh, minit, …]) - Classify a set of observations into k clusters using the k-means algorithm.
#kmeans is alsoa different implementation of k-means clustering with more methods for generating ->
#-> initial centroids but without using a distortion change threshold as a stopping criterion. The algorithm ->
# attempts to minimize the Euclidean distance between observations and centroids. Several initialization methods->
# are included.
from data_extractor import get_data_as_numpy_arrays
import matplotlib.pyplot as plt


def get_specific_data(dataset, user_id, column):
    result = []
    for row in dataset:
        if row[0] == user_id:
            point = [row[1], row[column]]
            result.append(point)

    return result


def draw_plot(whitened, mean_dist, centroids):
    w0 = whitened[mean_dist == 0]
    w1 = whitened[mean_dist == 1]
    w2 = whitened[mean_dist == 2]
    w3 = whitened[mean_dist == 3]
    plt.plot(w0[:, 0], w0[:, 1], 'o', alpha=0.5, label='cluster 0')
    plt.plot(w1[:, 0], w1[:, 1], 'd', alpha=0.5, label='cluster 1')
    plt.plot(w2[:, 0], w2[:, 1], 's', alpha=0.5, label='cluster 2')
    plt.plot(w3[:, 0], w3[:, 1], 'd', alpha=0.5, label='cluster 3')
    plt.plot(centroids[:, 0], centroids[:, 1], 'k*', label='centroids')
    plt.legend(shadow=True)
    plt.axis('equal')
    # plt.scatter(whitened[:, 0], whitened[:, 1])
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='r')
    plt.show()


if __name__ == '__main__':
    dataset = get_data_as_numpy_arrays()
    specific = get_specific_data(dataset, 14953, 2)
    #print(specific)
    whitened = whiten(specific)
    number = 4
    centroids, mean_dist = kmeans2(whitened, number)
    clusters, dist = vq(whitened, centroids)
    print(clusters)
    #print(whitened)
    draw_plot(whitened, mean_dist, centroids)
    in_0 = list(clusters).count(0)
    in_1 = list(clusters).count(1)
    in_2 = list(clusters).count(2)
    in_3 = list(clusters).count(3)
    print(" In 0 cluster: " + str(in_0) + "\n In 1 cluster: " + str(in_1) + " \n In 2 cluster: " + str(in_2) +
          " \n In 3 cluster: " + str(in_3))
