import sys
import random
from math import sqrt
import matplotlib.pyplot as plt
#from sklearn import metrics
#from sklearn.metrics import accuracy_score
import numpy as np

# Idea from http://www.caner.io/purity-in-python.html
def purityScore(clusters, classes):
    """
    Calculate the purity score for the given cluster assignments and ground truth classes
    
    :param clusters: the cluster assignments array
    :type clusters: numpy.array
    
    :param classes: the ground truth classes
    :type classes: numpy.array
    
    :returns: the purity score
    :rtype: float
    """
    
    A = np.c_[(clusters,classes)]

    n_accurate = 0.

    for j in np.unique(A[:,0]):
        z = A[A[:,0] == j, 1]
        x = np.argmax(np.bincount(z))
        n_accurate += len(z[z == x])

    return n_accurate / A.shape[0]

def getDistanceDic(list_of_list, centers):
    dic = {}
    for i in range(len(list_of_list)):
        temp_distance = []
        for point in centers:
            temp_distance.append(sqrt((list_of_list[i][0]-point[0])**2 + (list_of_list[i][1]-point[1])**2))
        dic[i] = temp_distance
    return dic


def getDicOfCurrentCluster(k, dic, list_of_list):
    current_cluster = {}
    for i in range(int(k)):
        current_cluster[i] = []
    for key in dic.keys():
        current_cluster[dic[key].index(min(dic[key]))].append([list_of_list[key][0], list_of_list[key][1]])
    return current_cluster

def getCurrentCenters(current_cluster):
    current_centers = []
    for key in current_cluster.keys():
        x, y = zip(*current_cluster[key])
        current_centers.append([sum(x) / len(x), sum(y) / len(y)])
    return current_centers

def plotCurrentClusters(current_cluster, centers):
    x = []
    y = []
    clusters = []
    for key in current_cluster.keys():
        current_x, current_y = zip(*current_cluster[key])
        for xi, yi in zip(current_x, current_y):
            x.append(xi)
            y.append(yi)
            clusters.append(key)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    scatter = ax.scatter(x, y, c = clusters, s = 50)
    for i, j in centers:
        ax.scatter(i, j, s=50, c = 'red', marker= '+')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.colorbar(scatter)
    fig.show()
    input()

argsys = sys.argv

filename = argsys[2]    # erster kommandozeilen parameter
maxk = argsys[1]           # maximales k 



list_of_list = []
with open(filename,'r') as rf:
    for line in rf:
        tokens = line.split('\t')
        tokens = [float(t) for t in tokens]
        list_of_list.append(tokens)


true_cluster = {}
for i in range(6):
    true_cluster[i+1] = []
for key in true_cluster.keys():
    for point in list_of_list:
        if point[2] == key:
            true_cluster[key].append([point[0], point[1]])

plotCurrentClusters(true_cluster, getCurrentCenters(true_cluster))

bestRANDK = 0
bestNormalizedMutualInformationK = 0
bestPurityOfClustersK = 0
currentRAND = 0
currentNormalizedMutualInformation = 0
currentPurityOfClusters = 0
for k in range(int(maxk)):
    random_centers = []

    random.choice(list_of_list)
    random_centers.append(random.choice(list_of_list))

    for i in range(0,int(k+1)-1):
        random_centers.append(random.choice(list_of_list))

    dic = getDistanceDic(list_of_list, random_centers)


    current_cluster = getDicOfCurrentCluster(k+1, dic, list_of_list)

    current_centers = getCurrentCenters(current_cluster)

    checkCenters = True
    while checkCenters:
        old_centers = []
        for centers in current_centers:
            old_centers.append(centers)

        dic = getDistanceDic(list_of_list, current_centers)
        current_cluster = getDicOfCurrentCluster(k+1, dic, list_of_list)
        current_centers = getCurrentCenters(current_cluster)



        plotCurrentClusters(current_cluster, current_centers)

        if old_centers == current_centers:
            checkCenters = False


    