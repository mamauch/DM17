# Function for validation
def logLikelihood(data, k, parameters):
    logLikeli = 0
    for x in data:
        logLikeli += np.log(parameters["p"] * gaus(parameters["sig1"], parameters["mu1"], x)
                              + parameters["p"] * gaus(parameters["sig2"], parameters["mu2"], x))
    return logLikeli