from sklearn.mixture import GaussianMixture

X,Y = make_blobs(cluster_std=1.5,random_state=20,n_samples=500,centers=3)
X = np.dot(X, np.random.RandomState(0).randn(2,2))

GMM = GaussianMixture(n_components=3)
GMM.fit(X)
Y = np.random.randint(-10, 20, size=(1, 2))
print(GMM.means_, GMM.predict_proba(Y))

"""Out: 
[[19.88168663 17.47097164] 
[-12.83538784   4.89646199] 
[11.09673732 18.67548935]] 
[[1.91500946e-17 9.30483496e-01 6.95165038e-02]]"""