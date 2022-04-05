## [Classic Dijkstra's Algorithm] ##
## [Uniform Cost Search Variant of Dijkstra] ##
## > Dijkstra's finds the shortest path from the root node to every other node
## > UCS searchest shortest path in terms of dest. cost from root to dest node
## > UCS stops as soon as a finishing point is found
## > Slightly less time consuming due to memory requirements than Dijkstra's algo
import pandas as pd
from queue import PriorityQueue

def dijkstra(G, start, goal):
    visited = set()
    dist = {start: 0}
    root = {start: None}
    pQueue = PriorityQueue()
  
    pQueue.put((0, start))
    while pQueue:
        while not pQueue.empty():
            _, vertex = pQueue.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else: # if pQueue ran out
            break # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue # skip these to save time
            old_cost = dist.get(neighbor, float('inf')) # default to infinity
            new_cost = dist[vertex] + distance
            if new_cost < old_cost:
                pQueue.put((new_cost, neighbor))
                dist[neighbor] = new_cost
                root[neighbor] = vertex

    return root, dist[vertex]

## Generate the shortest path
def generatePath(root, dest):
    rootRoutes = root[0]
    rootDistance = root[1]
    if dest not in rootRoutes:
        return None
    v = dest
    path = []
    while v is not None: # Root has null parent
        path.append(v)
        v = rootRoutes[v]
    
    return path[::-1]    #, rootDistance

## Initialize our GRAPH
## (How our graph will look like in dictionary format)
    # G = {
    # '1': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '2': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '3': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '4': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '5': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '6': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},
    # '7': {('1', 0.0), ('2', 5.0183417), ('3', 1.0213131)...},...
    # }
##
def initGraph(graph):
    for i in graph:
        temp = set()
        for k, v in graph[i].items():
            kv = ((str(k),v))
            temp.add(kv)
        graph[i] = temp
    """ print(graph) """
    return graph

""" graph = pd.read_csv('distances_new.csv', header=0, squeeze=True, index_col=0).to_dict()
graph = initGraph(graph)

SRC = '1'
DEST = '37'

## generatePath() func returns the shortest path routes from <src> to <dest> and the total distance in kilometers, in tuple
root = dijkstra(graph, SRC, DEST) # dijkstra(graph, <start_node>, <end_node>)
print(generatePath(root, DEST)) # generatePath(root, <end_node>)
 """
## TESTING PURPOSES
""" for i in range(1,37):
    SRC = str(i)
    DEST = '37'
    root = dijkstra(graph, SRC, DEST)
    print(generatePath(root, DEST))
for i in range(1,37):
    SRC = '37'
    DEST = str(i)
    root = dijkstra(graph, SRC, DEST)
    print(generatePath(root, DEST)) """