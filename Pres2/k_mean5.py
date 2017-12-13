# Get distance of current centers
def getDistanceDic(list_of_list, centers):
    dic = {}
    for i in range(len(list_of_list)):
        temp_distance = []
        for point in centers:
            temp_distance.append(sqrt((list_of_list[i][0]-point[0])**2 + (list_of_list[i][1]-point[1])**2))
        dic[i] = temp_distance
    return dic