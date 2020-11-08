# graph.py: class giving adjacency list graph
# link to sources:

1. for this code: http://www.cs.utsa.edu/~wagner/python/knight/knight_tour.html
2. Alternative: https://github.com/muj-programmer/warnsdorff-algorithm-visualizer/blob/master/utils/board.py

import sys

class Graph(object):
    def __init__(self):
        self.__numV = 0 # num of vertices
        self.__g = []
    # insert/put stuff ###############
    def insertVertex(self, d=None):
        self.__numV += 1
        self.__g.append([d, []])
    def insertEdge(self, u, v, d=None):
        self.__g[u][1].append([v,d]);
    def putVertexData(self, v, d):
        self.__g[v][0] = d
    def putEdgeData(self, u, v, d):
        # assumes unique edges
        for w in self.__g[u][1]:
            if w[0] == v:
                w[1] = d
                return
    # get stuff ######################
    def getNumV(self):
        return self.__numV
    def getVertexData(self, u):
        return self.__g[u][0]
    def getEdgeData(self, u, v):
        for w in self.__g[u][1]:
            if w[0] == v:
                return w[1]
        return None
    def getAdjList(self, u, d):
        ret = []
        if u < 0 or u >= self.__numV:
            return None
        elif len(self.__g[u][1]) == 0:
            return None
        else:
            t = len(self.__g[u][1])
            for i in range(0,t):
                if self._g[u][1][i][1] == d:
                  ret.append(self.\
                    __g[u][1][i][0])
            return ret
    # print stuff ####################
    def printGraph(self):
        sys.stdout.write("g = [\n")
        for i in range(len(self.__g)):
            sys.stdout.write(str(self.__g[i])
              + ", # " + str(i) + '\n')
        sys.stdout.write("]\n")