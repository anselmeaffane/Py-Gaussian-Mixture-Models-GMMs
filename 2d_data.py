from sklearn.datasets.samples_generator import make_blobs
from scipy.stats import multivariate_normal

X,Y = make_blobs(cluster_std=1.5,random_state=20,n_samples=500,centers=3)

X = np.dot(X, np.random.RandomState(0).randn(2,2))
plt.figure(figsize=(8,8))
plt.scatter(X[:, 0], X[:, 1])
plt.show()