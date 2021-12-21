# Third Assignment - OOP Course
## Credits:
This Project made by: Talia Seada (ID: 211551601) and Lior Breitman (ID: 212733257). <br>
__NOTE:__ In this projects the group members used "Code With Me" in the Pycharm workspace, so most of the commits are
from one main computer, while all the members were working on the project together.
## Intro:
This project is about Weighted Directional Graphs. <br>
For more information - https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex3 <br>

### The main Task:
The main task of this project is to run and display algorithms on Directed Weighted Graphs.
We achieved it by implementing these four main algorithms: <br>

### Class Node:
This class represents the set of operations applicable on a
node (vertex) in a (directional) weighted graph.
Implements the NodeData interface.

#### The parameters of the class:
- __key__ : Represents a node's ID number
- __location__ : Represents a node's location.
- __edgesToNode__ : holds the edges which goes to a node.
- __edgesFromNode__ : holds the edges which goes from a node.
- __tag__ : Represents the color associated to a node.


#### The functions of this class :
1. __Node(key)__ - Constructor that receives ID number.
2. __getEdgesToNode()__ - Returns the list of edges that goes to this node.
3. __getEdgesFromNode()__ - Returns the list of edges that goes from this node.
4. __addEdge(edge: Edge)__ - Adding an edge to one of the lists of nodes according to the edge's src and dest nodes.
5. __removeEdge(edge: Edge)__ - Removing an edge from one of the lists according to the edge's src and dest nodes.
6. __getKey()__ - Returns the ID of this node.
7. __setKey(k)__ - Setting new key to this node.
8. __getLocation()__ - Returns the location of this node.
9. __setLocation(location)__ - Setting new location to this node.
10. __getTag()__ - Returns the tag (Temporal data) of this node.
11. __setTag(t)__ - Setting new tag to this node.
We defined tag to be colors: 0 - for Undiscovered nodes "white", 1- for discovered but not finished "grey", 2- for finished nodes "black".


### Class Edge:
This class represents the set of operations applicable on a
directional edge(src,dest) in a (directional) weighted graph.
Implements the EdgeData interface

#### The parameters of the class:
- __src__ : source node of the edge
- __dest__ : destination node of the edge
- __w__ : weight of the edge

#### The functions that we received with the given interface:
1. __getSrc()__ - The ID of the source node of this edge.
2. __getDest()__ - The ID of the destination node of this edge
3. __getWeight()__ - The weight of this edge (positive value).

#### The functions of this class :
1. __Edge(src, weight, dest)__ - Constructor that receives the source and destination nodes and weight.
2. __getSrcNode()__ - The ID of the source node of this edge.
3. __getDestNode()__ - The ID of the destination node of this edge
4. __getWeight()__ - The weight of this edge (positive value).
5. __setSrcNode(node: Node)__ - Setting new source to this edge.
6. __setDestNode(node: Node)__ - Setting new destination to this edge.
7. __setWeight(w)__ - Setting new weight to this edge.

### Class DiGraph:
This class represents a Directional Weighted Graph, implementing the GraphInterface.

#### The parameters of the class:
- __nodes__ : holds all the nodes of this graph
- __edges__ : holds all the edges of this graph
- __int MC = 0__ : Mode Count

#### The functions of this class :
1. __DiGraph()__ - Default constructor
2. __get_graph()__ - Returns the graph
3. __add_node(node_id, pos = None)__ - adds a new node to the graph with the given node.
4. __all_in_edges_of_node()__ - Returns all the edges that go to the graph.
5. __all_out_edges_of_node()__ - Returns all the edges that go out of the graph.
6. __remove_node(node_id)__ - Deletes the node (with the given ID) from the graph - and removes all edges which starts or ends at this node. This method run in O(k), V.degree=k, as all the edges removed.
7. __remove_edge(node_id1, node_id2)__ - Deletes the edge from the graph, this method run in O(1) time.
8. __add_edge(id1, id2, weight)__ - adds a new edge to the graph with the given two nodes and a weight.
9. __get_all_v()__ - Returns all the nodes of the graph.
10. __reverse_graph()__ - This method returns a reversed graph.
11. __get_mc()__ - Returns the Mode Count.
12. __e_size()__ - Returns the number of edges of this graph.
13. __v_size()__ - Returns the number of nodes of this graph.

### Class GraphAlgo:
This class represents a Directed (positive) Weighted Graph Theory Algorithms.
Implements the functions of the GraphAlgoInterface.

#### The parameter of the class:
- graph = DiGraph()
- revGraph = DiGraph()

#### The functions of this class :
1. __GraphAlgo(copy = None)__ - Constructor that gets a None type in case we would like to build a copy object. 
2. __get_graph()__ - Returns the underlying graph of which this class works.
3. __get_revGraph()__ - Returns the underlying reversed graph of which this class works.
4. __isConnected()__ - Returns true if and only if (iff) there is a valid path from each node to each other node.  
   In this method we used bfs algorithm:
bfs from a node, reverse edges, again bfs from the same node. If we got an integer that is smaller than infinity in both, it means the graph is strongly connected.
5. __bfs(nodeKey,graph)__ - This method runs over all the nodes in the graph using the BFS algorithm, and checks if these nodes have edges connected to them.
   for bfs algorithm, we will change the tags of the graphs:
   - 0 for undiscovered nodes "white".
   - 1 for discovered but not finished "grey".
   - 2 for finished nodes "black".
6. __min_index(srcNode, dist_v, node_lst, passed)__ - This function returns the index of the minimum node
7. __dijkstra(src)__ - This method finds the shortest path between a given node to the rest of the graph's nodes using Dijkstra Algorithm.
8. __shortest_path(id1, id2)__ - Computes the shortest path between id1 to id2 - as an ordered List of nodes.
   In this method we used Dijkstra algorithm to find the shortest path.
9. __centerPoint()__ - Finds the node which minimizes the max distance to all the other nodes.
   In this method we iterate over the nodes of the graph and run the Dijkstra algorithm on each one of them.
   then, from each hashMap of distances of every node we got, we need to take the longest path.
   then take the minimum longest path of all the nodes.
10. __TSP(node_list)__ - Computes a list of consecutive nodes which go over all the nodes in cities.
    the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution -
    the lower the better.
    in this method we iterate over the given list and run the Dijkstra algorithm on the first node.
    After running once on a node, take the shortest path to a node (it's inside the list).
    Then, run again, but now on the node we took from the last iteration.
    The function stops when we passed all the nodes.
11. __save_to_json(file_name)__ - Saves this weighted (directed) graph to the given file name - in JSON format.
    Here we use the classes "nodeToJson" and "edgeToJson" to save the information into a Json file.
12. __load_from_json(file_name)__ - This method loads a graph to this graph algorithm.
    if the file was successfully loaded - the underlying graph of this class will be changed (to the loaded one), in case the
    graph was not loaded the original graph should remain "as is".
13. __plot_graph()__ - Plots the graph.

### Class plotGraph:
This class plots the graph.
In this class we have created another two classes (circle and line) in order to draw the graph.

#### The functions in this class:
1. __plot(graph)__ - In this function we create the graph.
2. __getBall(balls, node)__ - Return the ball object of the given node.

<B> classes: </B> <br>
<B> circle </B> - This class creates a node and draw it. <br>
<B> line </B> - This class creates a line and draw it.

### Class main:
In this class we run all the classes.

#### The functions in this class:
1. __check()__ - calls the check0(), check1() and the check2() functions
2. __check0()__ 
3. __check1()__ 
4. __check2()__ 
5. __check3()__
6. __main__ - calls the check() and the check3() functions

### Diagram:

### Results:
   


