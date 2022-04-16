x = np.linspace(-5, 5, 20)

x1 = x*np.random.rand(20)
x2 = x*np.random.rand(20) + 10
x3 = x*np.random.rand(20) - 10

xt = np.hstack((x1,x2,x3))