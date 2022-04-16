class GMM1D:
    """Apply GMM to 1D Data"""
    
    def __init__(self, X, max_iterations):
        """Initialize data and max_iterations"""
        self.X = X
        self.max_iterations = max_iterations
        
    def run(self):
        """Initialize parameters mu, var, pi"""
        self.pi = np.array([1/3, 1/3, 1/3])
        self.mu = np.array([5,8,1])
        self.var = np.array([5,3,1])
        
        r = np.zeros((len(self.X), 3))
        
        for itr in range(self.max_iterations):
    
            gauss1 = norm(loc=self.mu[0], scale=self.var[0])
            gauss2 = norm(loc=self.mu[1], scale=self.var[1])
            gauss3 = norm(loc=self.mu[2], scale=self.var[2])
            
            # E-Step
            for c,g,p in zip(range(3), [gauss1, gauss2, gauss3], self.pi):
                r[:,c] = p*g.pdf(xt[:])

            for i in range(len(r)):
                r[i,:] /= np.sum(r[i,:])

            fig = plt.figure(figsize=(10,10))
            ax0 = fig.add_subplot(111)

            for i in range(len(r)):
                ax0.scatter(xt[i],0,c=r[i,:],s=100) 

            for g,c in zip([gauss1.pdf(np.linspace(-15,15)),gauss2.pdf(np.linspace(-15,15)),gauss3.pdf(np.linspace(-15,15))],['r','g','b']):
                ax0.plot(np.linspace(-15,15),g,c=c,zorder=0)

            plt.show()

            # M-Step
            mc = np.sum(r, axis=0)
            self.pi = mc/len(self.X)
            self.mu = np.sum(r*np.vstack((self.X, self.X, self.X)).T, axis=0)/mc
            self.var = []

            for c in range(len(self.pi)):
                self.var.append(np.sum(np.dot(r[:,c]*(self.X[i] - self.mu[c]).T, r[:,c]*(self.X[i] - self.mu[c])))/mc[c])

gmm = GMM1D(xt, 10)
gmm.run()