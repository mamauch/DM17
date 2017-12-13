# Generate current centers
def getCurrentCenters(current_cluster):
    current_centers = []
    for key in current_cluster.keys():
        x, y = zip(*current_cluster[key])
        current_centers.append([sum(x) / len(x), sum(y) / len(y)])
    return current_centers