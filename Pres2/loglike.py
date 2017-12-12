import numpy as np
import math

def read(path):
    data = []
    lable = []
    with open(path) as csv:
        for line in csv:
            data.append(float(line.split("\n")[0]))
            lable.append(0)
    return lable, data

def logLikelihood(data, k, parameters):
    logLikeli = 0
    for x in data:
        logLikeli += np.log(parameters["p"] * gaus(parameters["sig1"], parameters["mu1"], x)
                              + parameters["p"] * gaus(parameters["sig2"], parameters["mu2"], x))
    return logLikeli

def gaus(sigma, mu, x):
    return 1./(np.sqrt(2. * math.pi) * sigma) * math.exp(-(x - mu)**2. / (2. * sigma**2.))

def eStep(data, parameters):
  wa = []
  wb = []
  for i in range(len(data)):
      wai = gaus(parameters["sig1"], parameters["mu1"], data[i]) * parameters["p"] / \
           (gaus(parameters["sig1"], parameters["mu1"], data[i]) * parameters["p"] +
            gaus(parameters["sig2"], parameters["mu2"], data[i]) * parameters["p"])
      wa.append(wai)
      wb.append(1 - wai)
  return wa, wb

def getMu(data, ws):
    zaehler = 0
    nenner = 0
    for x, w in zip(data, ws):
        zaehler += float(x*w)
        nenner += float(w)
    return zaehler/nenner

def getSig(data, ws, mu):
    zaehler = 0
    nenner = 0
    for x, w in zip(data, ws):
        zaehler += float(w * (x - mu)**2)
        nenner += float(w)
    return float(np.sqrt(zaehler/nenner))

def mStep(wa, wb, data, parameters):
  parameters['mu1'] = getMu(data, wa)
  parameters['mu2'] = getMu(data, wb)
  parameters['sig1'] = getSig(data, wa, parameters['mu1'])
  parameters['sig2'] = getSig(data, wa, parameters['mu2'])
  return parameters


lable, data = read("EM-data.csv")
k = 2
parameters = {'mu1': 1., 'sig1': 1., 'mu2': 4., 'sig2': 1., 'p': 0.5}

for i in range(20):
    print ("########")
    print ("Step "+str(i))
    print (logLikelihood(data, k, parameters))
    print (parameters)
    print ("\n")

    wa, wb = eStep(data, parameters)
    parameters = mStep(wa, wb, data, parameters)
