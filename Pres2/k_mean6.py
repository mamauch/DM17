# Get dic of current clusters
def getDicOfCurrentCluster(k, dic, list_of_list):
    current_cluster = {}
    for i in range(int(k)):
        current_cluster[i] = []
    for key in dic.keys():
        current_cluster[dic[key].index(min(dic[key]))].append([list_of_list[key][0], list_of_list[key][1]])
    return current_cluster