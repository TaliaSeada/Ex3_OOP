# Third Assignment - OOP Course
## Credits:
This Project made by: Talia Seada (ID: 211551601) and Lior Breitman (ID: 212733257). <br>
__NOTE:__ In this projects the group members used "Code With Me" in the Pycharm workspace, so most of the commits are
from one main computer, while all the members were working on the project together.
## Intro:
This is the 4th assignment on our OOP course as part of our B.sc in computer science
In this assignment, we were asked to implement 3 graph theory algorithms: TSP, shortest path, and Center Point
We implemented a DiGraph class where the directed graph is represented using a dictionary of nodes and a list of edges
To implement all the algorithms we added 2 more algorithms, Dijkstra and BFS: Dijkstra for the shortest path between nodes, and BFS to check if the graph is strongly connected so we can search for a center.
The last part was the GUI which we implemented using PyGame. In the Gui, you can see the graph as well as run algorithms on It to see the results <br>
For more information - https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex3 <br>

### The main Task:
The main task of this project is to run and display algorithms on Directed Weighted Graphs.
We achieved it by implementing these four main algorithms: <br>

### GUI:
When running the plot_graph() in the GraphAlgo class we get here. <br>
How to use the buttons:
1. Reset changes button : This button reset the graph to the default. 
2. Center button : This button prints the center node on the graph.
3. ShortestPath button : This button ask from the user to insert two nodes (integers) and print the shortest path on the graph.
4. TSP button : This button ask from the user to insert two or more nodes (integers) and print the TSP path on the graph.

### Diagram:
![](src/diagram.png)
### Results:
Time of running each algorithm in each graph (name), when time is in nanoseconds.
![image](https://user-images.githubusercontent.com/78349342/147124465-aa80df58-ad2c-4c66-b5fe-a5eabb56d8b0.png)


