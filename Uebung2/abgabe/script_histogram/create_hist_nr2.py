import matplotlib.pyplot as plt
import sys
import numpy as np


def plot_hist(input, name):
    data = []
    for i in input:
        try:
            data.append(len(i))
        except:
            data.append(1)
    plt.hist(data)
    plt.xlabel('Groesse der Itemsets der Boarders')
    plt.ylabel('Anzahl der Itemsets der Boarders')
    plt.title(name)
    plt.grid(True)
    plt.savefig(name + ".pdf")
    plt.close()

def readFile(filePath):
    with open(filePath, "r") as input_file:
        counter = 0
        PBoarderList = []
        NBoarderList = []
        for line in input_file:
            if counter == 0:
                counter = 1
                continue
            elif counter == 1:
                tmpList=[]
                for i in line.split(";")[3].split(","):
                    if "[" in i:
                        tmpi = i.replace("[","")
                        if "]" in i:
                            tmpi = tmpi.replace("]","")
                            PBoarderList.append(int(tmpi))
                        else:
                            tmpList.append(int(i.replace("[","")))
                    elif "]" in i :
                        tmpList.append(int(i.replace("]","")))
                        PBoarderList.append(tmpList)
                        tmpList=[]
                    else:
                        tmpList.append(int(i))
                tmpList = []
                for i in line.split(";")[4].split(","):
                    if "[" in i:
                        tmpi = i.replace("[","")
                        if "]" in i:
                            tmpi = tmpi.replace("]","")
                            NBoarderList.append(int(tmpi))
                        else:
                            tmpList.append(int(i.replace("[","")))
                    elif "]" in i :
                        tmpList.append(int(i.replace("]","")))
                        NBoarderList.append(tmpList)
                        tmpList=[]
                    else:
                        tmpList.append(int(i))
                return PBoarderList, NBoarderList

filePath = sys.argv[1]

positiveBoarder, negativeBoarder = readFile(filePath)

plot_hist(positiveBoarder, sys.argv[1]+"positiveBoarder")
plot_hist(negativeBoarder, sys.argv[1]+"negativeBoarder")