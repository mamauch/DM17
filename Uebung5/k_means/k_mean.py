
import sys
import random
from math import sqrt
import matplotlib.pyplot as plt

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

filename = argsys[1]    # erster kommandozeilen parameter
k = argsys[2]           # zweiter kommandozeilen parameter



list_of_list = []
with open(filename,'r') as rf:
    for line in rf:
        tokens = line.split('\t')
        tokens = [float(t) for t in tokens]
        list_of_list.append(tokens)


true_cluster = {}
for i in range(7):
    true_cluster[i+1] = []
for key in true_cluster.keys():
    for point in list_of_list:
        if point[2] == key:
            true_cluster[key].append([point[0], point[1]])
print(true_cluster)
plotCurrentClusters(true_cluster, getCurrentCenters(true_cluster))


random_centers = []

random.choice(list_of_list)
random_centers.append(random.choice(list_of_list))

for i in range(0,int(k)-1):
    random_centers.append(random.choice(list_of_list))

print(random_centers)

#a = abs(list_of_list[0][0] - random_centers[0][0])
#for i in range(0,len(list_of_list)-1):



dic = getDistanceDic(list_of_list, random_centers)


current_cluster = getDicOfCurrentCluster(k, dic, list_of_list)

current_centers = getCurrentCenters(current_cluster)

print(current_centers)

checkCenters = True
while checkCenters:
    old_centers = []
    for centers in current_centers:
        old_centers.append(centers)

    dic = getDistanceDic(list_of_list, current_centers)
    current_cluster = getDicOfCurrentCluster(k, dic, list_of_list)
    current_centers = getCurrentCenters(current_cluster)



    plotCurrentClusters(current_cluster, current_centers)

    if old_centers == current_centers:
        checkCenters = False


