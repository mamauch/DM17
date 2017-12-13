def gaus(sigma, mu, x):
    return 1./(np.sqrt(2. * math.pi) * sigma) * math.exp(-(x - mu)**2. / (2. * sigma**2.))