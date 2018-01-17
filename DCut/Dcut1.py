import networkx as nx
import random as rm

class Vertex():
    """
        Implementation of an Vertex in a graph
    """
    checked = False
    connected = None
    density = None
    dfs_id = 0

    def __init__(self, id_, label):
        self.id_ = id_
        self.label = label

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




def calculate_neighbors(u, myEdges):
    result = []
    result.append(u)
    for edge in myEdges:
        if(edge.from_vertex == u.id_):
            result.append(Vertex(edge.to_vertex, edge.to_vertex))
        elif(edge.to_vertex == u.id_):
            result.append(Vertex(edge.from_vertex, edge.from_vertex))
    return result

def jaccard(u, v, edges):

    gamma_u = calculate_neighbors(u, edges)
    gamma_v = calculate_neighbors(v, edges)
    u = set()
    v = set()
    for i in range(len(gamma_u)):
        u.add(gamma_u[i].id_)
        i += 1
    for j in range(len(gamma_v)):
        v.add(gamma_v[j].id_)
        j += 1

#    gamma_u = set(calculate_neighbors(u, edges))
#    gamma_v = set(calculate_neighbors(v, edges))
    return len(u.intersection(v))/len(u.union(v))

a = jaccard(u,u,myEdges)

def s(u, v, edges):
    return jaccard(u, v, edges)   # todo add weights



def main():

    G = nx.read_gml('karate.gml', label='id')

    myNode = {}
    for node in G.nodes:
        mn = Vertex(node, node)
        myNode[]

    for edge in G.edges:
        me = Edge(edge[0], edge[1])
        myEdges.append(me)

    print('test')
    print(myEdges[0])

    T = []
    u = rm.choice(myNode)
    u.checked = True
    T.append(u)

    while len(T) < len(myNode):
        maxv = -1
        p = Vertex(0, 0)
        q = Vertex(0, 0)
        for i in range(len(T)):
            u = T[i]
            gamma_u = calculate_neighbors(u, myEdges)
            for j in range(len(gamma_u)):
                v = gamma_u[j]

                if v.checked == False:
                    myS = s(u, v, myEdges)
                    if myS > maxv:
                        maxv = myS
                        p = v
                        q = u
        p.checked = True
        p.connected = q
        p.density = maxv
        T.append(p)

    for i in range(len(T)):
        print(T[i], T[i].connected, T[i].density)
        i += 1




if __name__ == "__main__":
    main()


