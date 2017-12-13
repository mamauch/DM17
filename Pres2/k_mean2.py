# Generate a set with key=tCluster, value=point
true_cluster = {}
for i in range(nTrueClusters):
    true_cluster[i+1] = []
for key in true_cluster.keys():
    for point in list_of_list:
        if point[2] == key:
            true_cluster[key].append([point[0], point[1]])