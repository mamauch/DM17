def mStep(wa, wb, data, parameters):
  parameters['mu1'] = getMu(data, wa)
  parameters['mu2'] = getMu(data, wb)
  parameters['sig1'] = getSig(data, wa, parameters['mu1'])
  parameters['sig2'] = getSig(data, wa, parameters['mu2'])
  return parameters