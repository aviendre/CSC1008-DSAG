## [Classic Dijkstra's Algorithm] ##
""" #Initializing the Graph Class
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

#Implementing Dijkstra's Algorithm
def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 2)
customGraph.addEdge("C", "B", 6)
customGraph.addEdge("C", "A", 5)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)
customGraph.addEdge("F", "C", 2)

print(dijkstra(customGraph, "F")) """

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
    todo = PriorityQueue()
  
    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else: # if todo ran out
            break # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue # skip these to save time
            old_cost = dist.get(neighbor, float('inf')) # default to infinity
            new_cost = dist[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                dist[neighbor] = new_cost
                root[neighbor] = vertex

    return root

## Generate the shortest path
def generatePath(root, dest):
    if dest not in root:
        return None
    v = dest
    path = []
    while v is not None: # Root has null parent
        path.append(v)
        v = root[v]
    
    return path[::-1]

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

graph = pd.read_csv('distances_new.csv', header=0, squeeze=True, index_col=0).to_dict()

root = dijkstra(initGraph(graph), '10', '34') # dijkstra(graph, <start_node>, <end_node>)
print(generatePath(root, '34')) # generatePath(root, <end_node>)