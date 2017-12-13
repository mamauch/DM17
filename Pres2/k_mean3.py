# Iterate until maxk
for k in range(int(maxk)):
	# Generate random centers
    random_centers = []
    for i in range(0,int(k+1)-1):
        random_centers.append(random.choice(list_of_list))
    # Get distance for the random centers
    dic = getDistanceDic(list_of_list, random_centers)
    # Get current clusters
    current_cluster = getDicOfCurrentCluster(k+1, dic, list_of_list)
    # Get current centers
    current_centers = getCurrentCenters(current_cluster)
    # Set check for while loop true
    checkCenters = True