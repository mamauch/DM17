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