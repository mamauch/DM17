# -*- coding: utf-8 -*-

from itertools import chain, combinations
from collections import defaultdict

def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
        """calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support"""
        _itemSet = set()
        localSet = defaultdict(int)

        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)

                if support >= minSupport:
                        _itemSet.add(item)

        return _itemSet


def joinSet(itemSet, length):
        """Join a set with itself and returns the n-element itemsets"""
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))              # Generate 1-itemSets
    return itemSet, transactionList


def runApriori(data_iter, minSupport):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules

    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet)

    # get 1 NBoarder ; 1 PBoarder is zero
    oneNBoarder = getFirstNegativBoarder(itemSet, oneCSet)
    currentNBoarder = oneNBoarder
    currentPBoarder = set()

    currentLSet = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet)

        currentLSet = currentCSet

        # get k NBoarder
        currentNBoarder = calculateKNegativeBoarder(currentNBoarder, currentCSet, freqSet)

        # get k PBoarder
        currentPBoarder = calculateKPositivBoarder(currentPBoarder, largeSet, k)

        k = k + 1

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    return toRetItems, currentPBoarder, currentNBoarder


def printResults(items, minSupport, name, PBoarder, NBoarder):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""

    print ("The positive Boarder is: " + str([list(i) for i in PBoarder]))
    print ("The negative Boarder is: " + str([list(i) for i in NBoarder]))

    outString = "items;lenItems;support;PBoarder;NBoarder"
    outString += "\n"
    for item, support in sorted(items, key=lambda (item, support): support):
        outString += str(item)
        outString += ";"
        outString += str(len(item))
        outString += ";"
        outString += str(support)
        outString += ";"
        outString += str([list(i) for i in PBoarder])
        outString += ";"
        outString += str([list(i) for i in NBoarder])
        outString += ";"
        outString += "\n"
        print ("item: %s , %.3f" % (str(item), support))
    with open("../output_nr1/" + name + "_" + str(minSupport) + ".csv", "w") as output:
        output.write(outString)


def dataFromFile(fname):
        """Function which reads from the file and yields a generator
            Here the file is in a format like: 1,0,1,0,1 to make it less operations
            We will first convert this in a form like

            A|B|C|D|E
            --------- --->
            1|0|0|1|0       A|D
            0|1|1|0|0       B|C
            ...             ...
        """
        with open(fname, 'rU') as file_iter:
            for line in file_iter:
                line_tmp = [i for (i, elem) in enumerate(line.split(",")) if int(elem)]
                record = frozenset(line_tmp)
                yield record

def getFirstNegativBoarder(itemSet, oneCSet):
    for item in oneCSet:
        itemSet.remove(item)
    return itemSet

def calculateKNegativeBoarder(currentNBoarder, currentCSet, freqSet):
    # B-i = B-(i-1) U (Ci - Fi)
    tmpCurrentSet = []
    for item in currentCSet:
        tmpCurrentSet.append(item)

    for item in freqSet:
        if item in tmpCurrentSet:
            tmpCurrentSet.remove(item)
    for i in tmpCurrentSet:
        currentNBoarder.append(i)
    return currentNBoarder

def calculateKPositivBoarder(currentPBoarder, largeSet, currentDic):
    # B+(i-1) = B+(i-2) U (Schnittmenge von F(i-1) und Fi)
    tmpCurrentPBoarder = set()
    if currentDic-2 == 0:
        tmpCurrentPBoarder = largeSet[currentDic-1]
    else:
        for item in currentPBoarder:
            tmpCurrentPBoarder.add(item)
        for SubLarge in largeSet[currentDic - 1]:
            tmp = 0
            for SubBoarder in currentPBoarder:
                if SubBoarder <= SubLarge:
                    if SubBoarder in tmpCurrentPBoarder:
                        tmpCurrentPBoarder.remove(SubBoarder)
                        tmpCurrentPBoarder.add(SubLarge)
                        tmp = 1
            if tmp == 0:
                tmpCurrentPBoarder.add(SubLarge)
    return tmpCurrentPBoarder
