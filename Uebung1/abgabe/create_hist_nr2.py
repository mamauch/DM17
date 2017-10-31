import matplotlib.pyplot as plt
import numpy as np
import sys


def plot_hist(data, name):
    plt.hist(data)
    plt.xlabel('Support-Wert')
    plt.ylabel('Anzahl der Itemsets')
    plt.title(name)
    plt.grid(True)
    plt.savefig(name + ".pdf")

def readFile(filePath):
    with open(filePath, "r") as input_file:
        counter = 0
        output = []
        for line in input_file:
            if counter == 0:
                counter = 1
                continue
            else:
                output.append(float(line.split(";")[2]))
    return output

filePath = sys.argv[1]

input_data = readFile(filePath)
print input_data
plot_hist(input_data, sys.argv[1])