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

    # get 1 FreeSet
    currentFreeSet = getFirstFreeSet(oneCSet, freqSet, transactionList)
    currentClosedSet = defaultdict(int)

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

        # get closed set
        minAppear = len(transactionList)*minSupport
        currentClosedSet = getClosedSet(currentClosedSet, freqSet, k, minAppear)

        #get free set
        currentFreeSet = getFreeSet(currentFreeSet, freqSet, k, minAppear)

        k = k + 1

    # get 1 ClosedSet
    currentClosedSet = getLastClosedSet(currentClosedSet, freqSet, k, minAppear)

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    return toRetItems, currentPBoarder, currentNBoarder, currentClosedSet, currentFreeSet


def printResults(items, minSupport, name, PBoarder, NBoarder, ClosedSet, FreeSet):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""

    print ("The positive Boarder is: " + str([list(i) for i in PBoarder]))
    print ("The negative Boarder is: " + str([list(i) for i in NBoarder]))

    print ("The ClosedSet is: " + str([[list(key), ClosedSet.get(key)] for key in ClosedSet.keys()]))
    print ("The FreeSet is: " + str([[list(key), FreeSet.get(key)] for key in FreeSet.keys()]))

    outString = "items;lenItems;support;PBoarder;NBoarder;ClosedSet;FreeSet"
    outString += "\n"
    for item in items:
        outString += str(item[0])
        outString += ";"
        outString += str(len(item[0]))
        outString += ";"
        outString += str(item[1])
        outString += ";"
        outString += str([list(i) for i in PBoarder])
        outString += ";"
        outString += str([list(i) for i in NBoarder])
        outString += ";"
        outString += str([[list(key) , ClosedSet.get(key)] for key in ClosedSet.keys()])
        outString += ";"
        outString += str([[list(key), FreeSet.get(key)] for key in FreeSet.keys()])
        outString += ";"
        outString += "\n"
        print ("item: %s , %.3f" % (str(item[0]), item[1]))
    with open("../output/" + name + "_" + str(minSupport) + ".csv", "w") as output:
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

def getLastClosedSet(tmpCurrentClosedSet, freqSet, currentDic, minAppear):
    for key in freqSet.keys():
        if (len(key) == currentDic - 2) & (freqSet[key] >= minAppear):
            tmpCurrentClosedSet[key] = freqSet.get(key)
    return tmpCurrentClosedSet


def getClosedSet(currentClosedSet, freqSet, currentDic, minAppear):
    """Function which reads from the file and yields a generator
        An itemset is closed if none of its immediate supersets has the
        same support as the itemset
    """
    tmpCurrentClosedSet = defaultdict(int)
    for key in currentClosedSet.keys():
        tmpCurrentClosedSet[key] = currentClosedSet.get(key)

    tmpControlSet = set()

    for nextKey in freqSet.keys():
        for currentKey in freqSet.keys():
            if (len(currentKey) == currentDic-1) & (len(nextKey) == currentDic):
                if currentKey.issubset(nextKey):
                    if (freqSet.get(currentKey) == freqSet.get(nextKey)) & (freqSet.get(currentKey) >=  minAppear):
                        tmpControlSet.add(currentKey)
                    if (freqSet.get(currentKey) > freqSet.get(nextKey)) & (freqSet.get(currentKey) >=  minAppear):
                        tmpCurrentClosedSet[currentKey] = freqSet.get(currentKey)

    for key in tmpControlSet:
        if key in tmpCurrentClosedSet.keys():
            tmpCurrentClosedSet.pop(key)
    return tmpCurrentClosedSet

def getFirstFreeSet(oneCSet, freqSet, transactionList):
    """Function which reads from the file and yields a generator
        An itemset is free if all subsets are greater
    """
    tmpCurrentFreeSet = defaultdict(int)
    for key in freqSet.keys():
        if (len(key) == 1) & (not freqSet.get(key) == len(transactionList)):
            tmpCurrentFreeSet[key] = freqSet.get(key)
    return tmpCurrentFreeSet

def getFreeSet(currentFreeSet, freqSet, currentDic, minAppear):
    """Function which reads from the file and yields a generator
        An itemset is free if all subsets are greater
    """
    tmpCurrentFreeSet = defaultdict(int)
    for key in currentFreeSet.keys():
        tmpCurrentFreeSet[key] = currentFreeSet.get(key)

    for currentKey in freqSet.keys():
        if len(currentKey) == currentDic:
            listOfSupportOfSubs = []
            for lastKey in freqSet.keys():
                if len(lastKey) == currentDic - 1:
                    if lastKey.issubset(currentKey):
                        listOfSupportOfSubs.append(freqSet.get(lastKey))
            if (freqSet.get(currentKey) < min(listOfSupportOfSubs)) & (freqSet.get(currentKey) >= minAppear):
                tmpCurrentFreeSet[currentKey] = freqSet.get(currentKey)
    return tmpCurrentFreeSet
