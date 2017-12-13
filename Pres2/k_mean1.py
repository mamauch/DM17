argsys = sys.argv
# Input of the program
filename = argsys[2]    
maxk = argsys[1]           
# Read the file
list_of_list = []
with open(filename,'r') as rf:
    for line in rf:
        tokens = line.split('\t')
        tokens = [float(t) for t in tokens]
        list_of_list.append(tokens)