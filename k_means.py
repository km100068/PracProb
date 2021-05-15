from os import SEEK_DATA
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten

#whiten(obs[, check_finite]) - Normalize a group of observations on a per feature basis.
#whiten - must be called prior to passing an observation matrix to kmeans.

whitened = whiten(data)


#kmeans(obs, k_or_guess[, iter, thresh, …]) - Performs k-means on a set of observation vectors forming k clusters.
#obs - Each row of the M by N array is an observation vector. The columns are ->
# the features seen during each observation.


#k_or_guess - The number of centroids to generate. A code is assigned to each centroid, which is also the row index of the centroid in the code_book matrix generated.
scipy_centers,_ = kmeans(whitened, 3) #musimy tu podać liczbę klasterow na jakie chcemy podzielić



#vq(obs, code_book[, check_finite]) - Assign codes from a code book to observations.

#kmeans2(data, k[, iter, thresh, minit, …]) - Classify a set of observations into k clusters using the k-means algorithm.
#kmeans is alsoa different implementation of k-means clustering with more methods for generating ->
#-> initial centroids but without using a distortion change threshold as a stopping criterion. The algorithm ->
# attempts to minimize the Euclidean distance between observations and centroids. Several initialization methods->
# are included.