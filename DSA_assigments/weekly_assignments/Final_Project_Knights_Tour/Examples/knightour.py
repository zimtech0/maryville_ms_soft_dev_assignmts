# knight.py: backtracking search, knight's tour
import sys
from graph import *
N = 6 # size of chessboard

# convert chess coordinates
def itot(i):
    return (i//N, i%N)
def ttoi(t):
    return t[0]*N + t[1]
    
k1, k2 = 1, 2 # knight moves
moves = [(k1,k2),(-k1,k2),(k1,-k2),(-k1,-k2),
         (k2,k1),(-k2,k1),(k2,-k1),(-k2,-k1)]
sys.stdout.write(str(moves) + '\n\n')

# construct graph
ps = open("knight12.ps","w")
graph = Graph()
for i in range(N*N):
    graph.insertVertex(0) # 0 means color white
    t = itot(i)
    for j in range(8):
        # try move j
        s = moves[j]
        if 0 <= (t[0]+s[0]) < N and\
           0 <= (t[1]+s[1]) < N:
            graph.insertEdge(i,
              ttoi((t[0]+s[0],t[1]+s[1])), None)
            # write ps code
            ti = itot(i)
            ps.write(str(ti[0])+" "+str(ti[1])+
              " moveto "+str(t[0]+s[0])+" "+
              str(t[1]+s[1])+" lineto stroke"+'\n')
graph.printGraph()

# carry out recursive backtracking search
st = []
def tour(u, pathlen):
    st.append(u)
    if pathlen > 34:
        if st[0] == st[35]:
            sys.stdout.write("path: " + str(st)+'\n')
    graph.putVertexData(u,1) # color is black
    for v in graph.getAdjList(u):
        if graph.getVertexData(v) == 0: # v is white
            # recursive call
            tour(v, pathlen+1)
            # returned somehow
    # done with adj list,
    graph.putVertexData(u,0) # white, this is key step
    # also pop stack
    st.pop()
tour(7, 0)
    
"""
g =
[
[0,[[ 8,None],[13,None]]] # 0
[0,[[ 9,None],[14,None],[12,None]]] # 1
[0,[[10,None],[ 6,None],[15,None],[13,None]]] # 2
[0,[[11,None],[ 7,None],[16,None],[14,None]]] # 3
[0,[[ 8,None],[17,None],[15,None]]] # 4
[0,[[ 9,None],[16,None]]] # 5
[0,[[14,None],[ 2,None],[19,None]]] # 6
[0,[[15,None],[ 3,None],[20,None],[18,None]]] # 7
[0,[[16,None],[ 4,None],[12,None],[ 0,None],[21,None],[19,None]]] # 8
[0,[[17,None],[ 5,None],[13,None],[ 1,None],[22,None],[20,None]]] # 9
[0,[[14,None],[ 2,None],[23,None],[21,None]]] # 10
[0,[[15,None],[ 3,None],[22,None]]] # 11
[0,[[20,None],[ 8,None],[25,None],[ 1,None]]] # 12
[0,[[21,None],[ 9,None],[26,None],[ 2,None],[24,None],[0,None]]] # 13
[0,[[22,None],[10,None],[18,None],[ 6,None],[27,None],[3,None],[25,None],[1,None]]] # 14
[0,[[23,None],[11,None],[19,None],[ 7,None],[28,None],[4,None],[26,None],[2,None]]] # 15
[0,[[20,None],[ 8,None],[29,None],[ 5,None],[27,None],[3,None]]] # 16
[0,[[21,None],[ 9,None],[28,None],[ 4,None]]] # 17
[0,[[26,None],[14,None],[31,None],[ 7,None]]] # 18
[0,[[27,None],[15,None],[32,None],[ 8,None],[30,None],[6,None]]] # 19
[0,[[28,None],[16,None],[24,None],[12,None],[33,None],[9,None],[31,None],[7,None]]] # 20
[0,[[29,None],[17,None],[25,None],[13,None],[34,None],[10,None],[32,None],[8,None]]] # 21
[0,[[26,None],[14,None],[35,None],[11,None],[33,None],[9,None]]] # 22
[0,[[27,None],[15,None],[34,None],[10,None]]] # 23
[0,[[32,None],[20,None],[13,None]]] # 24
[0,[[33,None],[21,None],[14,None],[12,None]]] # 25
[0,[[34,None],[22,None],[30,None],[18,None],[15,None],[13,None]]] # 26
[0,[[35,None],[23,None],[31,None],[19,None],[16,None],[14,None]]] # 27
[0,[[32,None],[20,None],[17,None],[15,None]]] # 28
[0,[[33,None],[21,None],[16,None]]] # 29
[0,[[26,None],[19,None]]] # 30
[0,[[27,None],[20,None],[18,None]]] # 31
[0,[[28,None],[24,None],[21,None],[19,None]]] # 32
[0,[[29,None],[25,None],[22,None],[20,None]]] # 33
[0,[[26,None],[23,None],[21,None]]] # 34
[0,[[27,None],[22,None]]] # 35
]
"""
