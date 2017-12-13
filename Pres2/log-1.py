# Read the date and set the parameters 
lable, data = read("EM-data.csv")
parameters = {'mu1': 1., 'sig1': 1., 'mu2': 4., 'sig2': 1., 'p': 0.5}
k = 2 # We had only 2 clusters here
# Run the main program
for i in range(20):
    print ("########")
    print ("Step "+str(i))
    print (logLikelihood(data, k, parameters))
    print (parameters)
    print ("\n")
    wa, wb = eStep(data, parameters)
    parameters = mStep(wa, wb, data, parameters)