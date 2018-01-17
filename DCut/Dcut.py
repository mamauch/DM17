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

