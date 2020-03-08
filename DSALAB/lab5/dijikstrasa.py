from collections import defaultdict 
import sys 
  


def take_input():
    G = [] 
    file=open('lab5/input2.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)

    file.close()
    print(G)
    return G


G = take_input()
