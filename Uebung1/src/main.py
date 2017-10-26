import sys
from apyori import apriori
import csv

transactions = []
with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in reader:
        print line


#results = list(apriori(transactions))

#print (results)
