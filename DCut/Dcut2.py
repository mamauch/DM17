import networkx as nx
import random as rm
import copy
import  math
import matplotlib.pyplot as plt
import sklearn.metrics as metric

class Vertex():
    """
        Implementation of an Vertex in a graph
    """
    def __init__(self, id_):
        self.id_ = id_
        self.checked = False
        self.connected = None
        self.density = None

    def __str__(self):
        return str(self.id_)


class Edge():
    """
        Implementation of an Edge in a graph
    """
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex

    def __str__(self):
       return str((self.from_vertex, self.to_vertex))

    def connected_to(self, vertex):
        return vertex.id == self.from_vertex.id or \
               vertex.id == self.to_vertex.id




def calculate_neighbors(u, myEdges,vertex_dic):
    result = []
    result.append(u)
    for edge in myEdges:
        if(edge.from_vertex == u.id_):
            result.append(vertex_dic[edge.to_vertex])
        elif(edge.to_vertex == u.id_):
            result.append(vertex_dic[edge.from_vertex])
    return result

def jaccard(u, v, edges,vertex_dic):

    gamma_u = calculate_neighbors(u, edges,vertex_dic)
    gamma_v = calculate_neighbors(v, edges,vertex_dic)
    u = set()
    v = set()
    for i in range(len(gamma_u)):
        u.add(gamma_u[i].id_)

    for j in range(len(gamma_v)):
        v.add(gamma_v[j].id_)

#    gamma_u = set(calculate_neighbors(u, edges))
#    gamma_v = set(calculate_neighbors(v, edges))
    return len(u.intersection(v))/len(u.union(v))

def s(u, v, edges,vertex_dic):
    return jaccard(u, v, edges,vertex_dic)   # todo add weights


def d_cut(T): # TODO there is something wrong...

    d_cut_list=[]

    for i in range (0,len(T)):
        density = T[i].density
        c_one=set()
        c_two=set()
        c_one.add(T[i])
        for k in range(0,i):
            c_one.add(T[k])
        for j in range(i+1,len(T)):
            if T[j].connected in c_one:
                c_two.add(T[j])
            else:
                c_one.add(T[j])
        print(len(c_one),len(c_two))
        print(T[i])
        d_cut_list.append((density/min(len(c_one),len(c_two)),list(c_one),list(c_two)))

    min_cut=d_cut_list[0]
    for i in range(1,len(d_cut_list)):
        if min_cut[0]>d_cut_list[i][0]:
            min_cut=d_cut_list[i]

    return min_cut


def visualize(T):
    G=nx.Graph()
    G.add_nodes_from([t.id_ for t in T])
    G.add_edges_from([(t.id_,t.connected.id_) for t in T])
    nx.draw(G,with_labels=True)
    plt.show()


def evaluate(cluster_list):

    metric.adjusted_rand_score()


def DTree(myNode, myEdges, sim_dic):
    T = []
    u = rm.choice(list(myNode.values()))  # TODO attention... better take just value
    u.checked = True
    T.append(u)

    while len(T) < len(myNode):
        maxv = -1
        p = None
        q = None
        for i in range(len(T)):
            u = T[i]
            gamma_u = calculate_neighbors(u, myEdges, myNode)
            for j in range(len(gamma_u)):
                v = gamma_u[j]
                print("gamma u",gamma_u)
                if v.checked == False:
                    myS = sim_dic[(u.id_, v.id_)]
                    if myS > maxv:
                        maxv = myS
                        p = v
                        q = u
                        print(u,v)
        p.checked = True
        p.connected = q
        p.density = maxv
        T.append(p)
    return T


def read_gml_x(path):
    G = nx.read_gml(path, label='id')

    myNode = {}
    for node in G.nodes:
        mn = Vertex(node)
        myNode[node] = mn

    myEdges = []
    sim_dic = {}
    for edge in G.edges:
        me = Edge(edge[0], edge[1])
        myEdges.append(me)
    for edge in G.edges:
        simi = s(myNode[edge[0]], myNode[edge[1]], myEdges, myNode)
        sim_dic[(edge[0], edge[1])] = simi
        sim_dic[(edge[1], edge[0])] = simi
    return G, myNode,myEdges,sim_dic


def read_data(path):
    x = open(path)
    i=0
    myNode = {}
    myEdges = []
    sim_dic = {}
    true_label={}
    for t in x.readlines():
        if t[0]=="*" and i==0:
            i+=1
        elif t[0]=="*" and i==1:
            i += 1
        elif i==2 and t[0]!="%"and t[0]!="*":
            line= t.strip().split(" ")
            mn = Vertex(line[0])
            myNode[line[0]] = mn
            true_label[line[0]]=line[1]

        elif t[0] == "*" and i == 2 and t[0]!="%":
            i += 1
        elif i==3 and t[0]!="%" and t[0]!="*":
            edget=t.split(" ")
            edge=list(filter(lambda x: x !='',edget))
            me = Edge(edge[0], edge[1].strip())
            myEdges.append(me)


    for edge in myEdges:
        simi = s(myNode[edge.from_vertex], myNode[edge.to_vertex], myEdges, myNode)
        sim_dic[(edge.from_vertex, edge.to_vertex)] = simi
        sim_dic[(edge.to_vertex, edge.from_vertex)] = simi

    print("YeastS completely in storage...")
    return myNode, myEdges, sim_dic,true_label

def main(k):

    #G , myNode, myEdges, sim_dic= read_gml_x('karate.gml')
    myNode, myEdges, sim_dic, true_labels= read_data('YeastS.net')

    T= DTree(myNode,myEdges,sim_dic)

    for i in range(len(T)):
        print(T[i], T[i].connected, T[i].density)

    '''
    T.pop(0)
    visualize(T)

    if k>0:
        pot=int(math.log(k,2))
        residue=k-math.log(pot,2)


        cluster_list=[T]
        for i in range(pot):
            for j in range(len(cluster_list)):
                tree =cluster_list[j]
                t=d_cut(tree)
                cluster_list.append(t[1])
                cluster_list.append(t[2])
                cluster_list.pop(0)

        for j in range(residue):
            tree = cluster_list[j]
            t = d_cut(tree)
            cluster_list.append(t[1])
            cluster_list.append(t[2])
            cluster_list.pop(0)

        for i in range(len(cluster_list)):
            for j in range(len(cluster_list[i])):
                print(cluster_list[i][j],end="\t")
            print()

        evaluate(cluster_list)
    '''

if __name__ == "__main__":
    k=2
    main(k)

