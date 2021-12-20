# Third Assignment - OOP Course
## Table Of Content:
### Credits
### Intro
### Implementation
- Class Node
- Class Edge
- Class DiGraph
- Class GraphAlgo
- Class plotGraph
- Class main
### Results
### How to interact with the project


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

#### 1. shortestPath: 
In this algorithm we need to find the shortest path between two given nodes (return weight of path or list of nodes in this path).

#### 2. center:
In this algorithm we need to find the center node of a graph. 

#### 3. isConnected:
In this algorithm we need to find if there is a path between every two nodes in the graph.

#### 4. tsp:
Traveling Sales Man problem.


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




# HERE !
### Class DiGraph:
This class represents a Directional Weighted Graph, implementing the GraphInterface.

#### The parameters of the class:
- __HashMap<Integer,NodeData> nodes__ : holds all the nodes of this graph
- __HashMap<Integer,HashMap<String,EdgeData>> nodeEdges__ : holds the edges that goes from a node
- __ArrayList<EdgeData> allEdges__ : holds the edges of this graph
- __final String name__ : name of this graph
- __int MC =0__ : Mode Count

#### The functions that we received with the given interface:
1. __getNode(int key)__ - returns the node_data by the node_id.
2. __getEdge(int src, int dest)__ - returns the data of the edge (src,dest).
3. __addNode(NodeData n)__ - adds a new node to the graph with the given node_data.
4. __connect(int src, int dest, double w)__ - Connects an edge with weight w between node src to node dest. this method run in O(1) time.
5. __Iterator<NodeData> nodeIter()__ - This method returns an Iterator for the collection representing all the nodes in the graph.
6. __Iterator<EdgeData> edgeIter()__ - This method returns an Iterator for all the edges in this graph.
7. __Iterator<EdgeData> edgeIter(int node_id)__ - This method returns an Iterator for edges getting out of the given node (all the edges starting (source) at the given node).
8. __removeNode(int key)__ - Deletes the node (with the given ID) from the graph - and removes all edges which starts or ends at this node. This method run in O(k), V.degree=k, as all the edges removed.
9. __removeEdge(int src, int dest)__ - Deletes the edge from the graph, this method run in O(1) time.
10. __nodeSize()__ - Returns the number of vertices (nodes) in the graph.
11. __int edgeSize()__ - Returns the number of edges (assume directional graph).
12. __getMC()__ - Returns the Mode Count.

#### The functions that we added to this class (not included in the interface):
1. __Graph()__ - Default constructor
2. __Graph(ArrayList<Edge> edges, ArrayList<Node> nodes,String name)__ - constructor that receives the edges, nodes and the name of a graph.
3. __Graph(Graph other)__ - copy constructor.
4. __getAllEdges()__ - Returns all the edges of the graph.
5. __getNodeEdges()__ - Returns all the edges associated with a node.
6. __getNodes()__ - Returns all the nodes of the graph.
7. __getName()__ - Returns the name of the graph.


### Class GraphAlgo:
This class represents a Directed (positive) Weighted Graph Theory Algorithms.
Implements the functions of the GraphAlgoInterface.

#### The parameter of the class:
- Graph graph

#### The functions that we received with the given interface:
1. __init(DirectedWeightedGraph g)__ - Inits the graph on which this set of algorithms operates on.
2. __getGraph()__ - Returns the underlying graph of which this class works.
3. __copy()__ - Computes a deep copy of this weighted graph.
4. __isConnected()__ - Returns true if and only if (iff) there is a valid path from each node to each other node.  
   In this method we used bfs algorithm:
bfs from a node, reverse edges, again bfs from the same node. If we got an integer that is smaller than infinity in both, it means the graph is strongly connected.
5. __shortestPathDist(int src, int dest)__ - Computes the length of the shortest path between src to dest.
   In this method we used Dijkstra algorithm to find the shortest path distance.
6. __shortestPath(int src, int dest)__ - Computes the shortest path between src to dest - as an ordered List of nodes.
   In this method we used Dijkstra algorithm to find the shortest path.
7. __center()__ - Finds the api.NodeData which minimizes the max distance to all the other nodes.
   In this method we iterate over the nodes of the graph and run the Dijkstra algorithm on each one of them.
   then, from each hashMap of distances of every node we got, we need to take the longest path.
   then take the minimum longest path of all the nodes.
8. __tsp(List<NodeData> cities)__ - Computes a list of consecutive nodes which go over all the nodes in cities.
   the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution -
   the lower the better.
   in this method we iterate over the given list and run the Dijkstra algorithm on the first node.
   After running once on a node, take the shortest path to a node (it's inside the list).
   Then, run again, but now on the node we took from the last iteration.
   The function stops when we passed all the nodes.
9. __save(String file)__ - Saves this weighted (directed) graph to the given file name - in JSON format.
   Here we use the classes "nodeToJson" and "edgeToJson" to save the information into a Json file.

10. __load(String file)__ - This method loads a graph to this graph algorithm.
    if the file was successfully loaded - the underlying graph of this class will be changed (to the loaded one), in case the
    graph was not loaded the original graph should remain "as is".

#### The functions that we added to this class (not included in the interface):
1. __Dijkstra(int sourceNode)__ - This method finds the shortest path between a given node to the rest of the graph's nodes using Dijkstra Algorithm.
2. __bfs(int nodeKey,Graph graph)__ - This method runs over all the nodes in the graph using the BFS algorithm, and checks if these nodes have edges connected to them.
   for bfs algorithm, we will change the tags of the graphs:
   - 0 for undiscovered nodes "white".
   - 1 for discovered but not finished "grey".
   - 2 for finished nodes "black".
3. __createOppositeGraph()__ - This method creates an opposite graph of this graph.


### Class plotGraph:
This class is used to draw a graph.

#### The functions in this class:
__createMainWindow(String path)__ - In this function we create the main window.
__activateGUI(String path)__ - In this function we activate the GUI.

### Class main:
In this class we run all of the classes.

#### The functions in this class:
1. __showGraph(List<GeoLocation> scores,ArrayList<EdgeData> edgesToPaint, NodeData center)__ - Constructor
2. __paintComponent(Graphics g)__ 
3. __createAndShowGui(DirectedWeightedGraph g, ArrayList<EdgeData> toPaint, NodeData center)__ 
4. __drawArrowLine(Graphics g, int x1, int y1, int x2, int y2, int d, int h)__ 

## How to interact with the project:
### Run:
In order to run the project:
1. Enter the cmd and inside the cmd enter to the file where the jar is.
2. Write the command: java -jar Ex2.jar G1.json 
    - Where "G1.json" you need to write the right path of the graph that you want to load.
   

### GUI:
How to use the menu window:
1. __file__ : Here you can load a new graph to the program, or save the current graph to json file.
2. __Graph__ : Here you can interact with your graph
   - show graph - the graph will appear
   - Add node - adds new node to the graph
   - remove node - removes node from the graph
   - connect between 2 nodes - creates new edge between 2 chosen nodes
   - disconnect 2 nodes - deletes edge that connected between this 2 nodes.
3. __Algorithms__ : Here you can choose which algorithm to run on the graph.

### Diagram:

### Results:
   


