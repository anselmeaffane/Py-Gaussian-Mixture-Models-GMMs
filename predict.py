y = np.random.randint(-10, 20, size=(12, 2))
gmm2d = GMM2D(num_clusters=3, max_iterations=10)
gmm2d.run(X)
gmm2d.predict(y)