# In for-loop
while checkCenters:
		# Generate old_centers
        old_centers = [centers for centers in current_centers]
        # Get distance for the random centers
        dic = getDistanceDic(list_of_list, current_centers)
        # Get current clusters
        current_cluster = getDicOfCurrentCluster(k+1, dic, list_of_list)
        # Get current centers
        current_centers = getCurrentCenters(current_cluster)
        # Check while 
        if old_centers == current_centers:
            checkCenters = False
