# -*- coding: utf-8 -*-
# Main file
# ToDo:

def combination(l, r):
    if r == 0:
        yield []
    elif len(l) == r:
        yield l
    else:
        for c in (combination(l[1:], r-1)):
            yield l[0:1]+c
        for c in (combination(l[1:], r)):
            yield c

def generateNthCandidates(NthTransactions, listOfCombinations, nthCombi, support_thres):
    import pandas as pd

    for combination in listOfCombinations:
        nameColumn = str(combination)
        defaultColumn = []
        for i in range(NthTransactions.shape[1]):
            defaultColumn.append(0)
        dfTmp = pd.DataFrame({nameColumn: defaultColumn})
        for column in combination:
            dfTmp[nameColumn] += NthTransactions[int(column)]
        dfTmp[nameColumn] = (dfTmp[nameColumn]/nthCombi).astype(int)
        print dfTmp[nameColumn]
        NthTransactions.join(dfTmp[nameColumn])

    generateFirstCandidates(NthTransactions, support_thres)

def generateFirstCandidates(transactions, support_thres):
    for i in transactions.sum().iteritems():
        if float(i[1])/transactions.shape[0] < support_thres:
            del transactions[i[0]]
    return transactions




def main():
    import sys
    from reader import reader
    from apriori import apriori

    # Method to generate the candidates
    # sys.argv[1]
    data = "../data/dm3.csv"
    reader = reader(data)
    transactions = reader.readConvertCsv()

    # Delete the first transactions
    FirstTransactions = generateFirstCandidates(transactions, 0.4)

    # Generate nth combination and delete if under support
    for nthCombi in range(FirstTransactions.shape[1]):
        listOfCombinations = []
        combinations = combination(list(FirstTransactions.columns), nthCombi + 2)
        for j in combinations:
            listOfCombinations.append(j)
        FirstTransactions = generateNthCandidates(FirstTransactions, listOfCombinations, nthCombi, 0.4)





    """
    Keyword arguments:
    min_support -- The minimum support of relations (float).
    min_confidence -- The minimum confidence of relations (float).
    min_lift -- The minimum lift of relations (float).
    max_length -- The maximum length of the relation (integer).

    kwargs = {'min_support': 0.9, 'min_confidence': 0.0, 'min_lift': 0.0, 'max_length': None}
    print (list(apriori(transaction, **kwargs)))
        """

if __name__ == "__main__":
    main()