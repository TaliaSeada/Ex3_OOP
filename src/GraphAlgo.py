from heapq import *
from typing import List
import json
import random

from src.DiGraph import DiGraph
from src.api.GraphAlgoInterface import GraphAlgoInterface
from src.api.GraphInterface import GraphInterface

import pygame
import pygame_widgets
from pygame_widgets.button import Button
from src.Node import Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, copy=None):
        # default
        if not copy:
            self._graph = DiGraph()
            self._revGraph = DiGraph()
            # for GUI
            self.nodes = []
            self.balls = []
            self.lines_in = []
            self.lines_out = []
        # copy
        else:
            self._graph = copy
            self._revGraph = copy.reverse_graph(copy)
            # for GUI
            self.nodes = []
            self.balls = []
            self.lines_in = []
            self.lines_out = []

    # returns the graph
    def get_graph(self) -> GraphInterface:
        return self._graph

    # returns the reversed graph
    def get_revGraph(self) -> GraphInterface:
        return self._revGraph

    # this function returns the index of the minimum distance in a given list of distances
    def min_index(self, srcNode, dist_v, node_lst, passed):
        min = float('inf')
        index = 0
        for key in node_lst:
            if dist_v.get(key) < min and key != srcNode and key not in passed:
                index = key
                min = dist_v.get(key)
        return index

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        # Iterate over the given list and run the Dijkstra function on the first node.
        # After running once on a node, take the shortest path to a node (it's inside the list).
        # Then, run again, but now on the node we took from the last iteration.
        # The function stops when we passed all the nodes.

        dist = 0
        path = []

        passed = []
        v = node_lst[0]
        while len(passed) != len(node_lst) - 1:
            if v in node_lst:
                passed.append(v)
            # get all shortest path's to the node v
            dist_v, path_v = self.dijkstra(v)
            # then get the index of the shortest of them all
            min_ind = self.min_index(v, dist_v, node_lst, passed)
            # and take the path between the two nodes to the main path
            f, currPath = self.shortest_path(v, min_ind)
            for p in currPath:
                if len(path) == 0:
                    path.append(p)
                    continue
                elif path[-1] != p:
                    path.append(p)
            # finally increase the dist by the distance between the two nodes
            dist += dist_v.get(min_ind)
            v = min_ind

        return path, dist

    def bfs(self, nodeKey: int, g: DiGraph):
        D = {v: float('inf') for v in self._graph.get_all_v().keys()}
        D[nodeKey] = 0
        queue = []
        nodeDict = g.get_all_v()
        node = nodeDict.get(nodeKey)

        # Mark the source node as visited and enqueue it
        node.setTag(2)
        queue.append(nodeKey)
        v_group = g.get_all_v()
        while queue:
            # Dequeue a vertex from queue
            nodeKey = queue.pop(0)
            # print(nodeKey, end=" ")
            for i in g.all_out_edges_of_node(nodeKey).keys():
                if v_group.get(i).getTag() == 0:
                    queue.append(i)
                    v_group.get(i).setTag(2)
                    D[i] = D[nodeKey] + 1
        # reset tags
        for n in v_group:
            v_group.get(n).setTag(0)
        return max(D.values())

    def isConnected(self):
        # bfs from a node, reverse edges, again bfs from the same node
        # if we got integer smaller than infinity in both, it means the graph is strongly connected
        key = 0
        # get the node we want to check from
        for i in self._graph.get_all_v().keys():
            key = i
            break
        # run bfs on it
        bfs = self.bfs(key, self._graph)
        # if the result is infinity then the graph is not connected
        if bfs == float('inf'):
            return False
        # else reverse the graph and check from the same node
        bfs_rev = self.bfs(key, self._revGraph)
        # if the result is infinity then the graph is not connected
        if bfs_rev == float('inf'):
            return False
        # is the distance is not infinity then the graph is connected
        return True

    def centerPoint(self) -> (int, float):
        # if the graph is connected
        if self.isConnected():
            minDist = float('inf')
            minIndex = -1
            # run the dijkstra algorithm then take the max value of the
            # minimum values (distances that returned from the dijkstra algorithm)
            for v in self._graph.get_all_v().keys():
                dist, path = self.dijkstra(v)
                if max(dist.values()) < minDist:
                    minDist = max(dist.values())
                    minIndex = int(v)
            # return the node and the distance
            return minIndex, minDist
        # if the graph is not connected we cant have a center
        else:
            return -1, float('inf')

    def load_from_json(self, file_name: str) -> bool:
        # load files using the build in library json
        try:
            file = open(file_name)
            data = json.load(file)
            counter = 0
            # define nodes
            for i in data["Nodes"]:
                id = int(i['id'])
                # if pos is given
                if i.get('pos') is not None:
                    pos = i['pos']
                    xyz = pos.split(',')
                    for i in range(len(xyz)):
                        xyz[i] = float(xyz[i])
                    self._graph.add_node(id, xyz)
                    self._revGraph.add_node(id, xyz)
                # if pos is not given define random pos
                else:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    z = 0.0
                    self._graph.add_node(id, (x, y, z))
                    self._revGraph.add_node(id, (x, y, z))
            # define edges
            for i in data["Edges"]:
                counter += 1
                src = int(i["src"])
                dest = int(i["dest"])
                weight = float(i["w"])
                self._graph.add_edge(src, dest, weight)
                self._revGraph.add_edge(dest, src, weight)
            file.close()
            return True
        # if file does not exist
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        # save files using the build in library json
        try:
            nodes = []
            edges = []
            # create the dictionary for the saved file
            nodeDict = self._graph.get_all_v()
            # add the nodes
            for node in nodeDict:
                thisNode = nodeDict[node]
                location = thisNode.getLocation()
                x = location[0]
                y = location[1]
                z = location[2]
                id = node
                currNode = {"pos": (str(x) + "," + str(y) + "," + str(z)), "id": id}
                nodes.append(currNode)
                allOutEdges = self._graph.all_out_edges_of_node(id)
                # add the edges
                for edge in allOutEdges.keys():
                    src = id
                    dest = edge
                    weight = allOutEdges[edge]
                    edgeCurr = {"src": id, "w": weight, "dest": dest}
                    edges.append(edgeCurr)
            # combine
            all = {"Edges": edges, "Nodes": nodes}
            # write to the file
            with open(file_name, "w") as file:
                file.write(json.dumps(all, indent=4))
            file.close()
            return True
        # if save did not succeeded throw an exception
        except Exception as e:
            print(e)
            return False

    def dijkstra(self, src: int):
        # this function gets a source nodes and calculates the shortest path from it to every other
        # node on the graph, and returns the distances, and also the last node that we got from to
        # every other node

        Distances = {}
        lastPath = {}
        # define all distances to be infinity and all nodes in path to be None
        for v in self._graph.get_all_v():
            Distances[v] = float('inf')
            lastPath[v] = None
        # the distance between node to itself is 0, so add the first node's distance
        Distances[src] = 0
        h = []
        all_v = self._graph.get_all_v()
        # then add the node to the heap
        heappush(h, (Distances[src], src))
        # run over the nodes and get the shortest path by comparing the weights of the edges
        # update if there is shorter path, and note every node we visit as visited
        while h:
            currNode = heappop(h)[1]
            all_v.get(currNode).setTag(2)
            outEdges = self._graph.all_out_edges_of_node(int(currNode))
            for edge in outEdges.keys():
                if all_v.get(edge).getTag() != 2:
                    currDist = Distances.get(edge)
                    newDist = Distances.get(currNode) + outEdges.get(edge)
                    if newDist < currDist:
                        heappush(h, (newDist, edge))
                        Distances[edge] = newDist
                        lastPath[edge] = currNode
        # reset the tags of the nodes
        for v in all_v:
            all_v.get(v).setTag(0)
        # return the shortest distance and the path of it
        return Distances, lastPath

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        # if the nodes exist in the graph
        if self._graph.get_all_v().__contains__(id1) and self._graph.get_all_v().__contains__(id2):
            p = []
            # use dijkstra
            dist, path = self.dijkstra(id1)
            # if node1 is not connected to node2 the shortest path would be infinity
            if dist[id2] == float('inf'):
                return float('inf'), p
            # else find the path between the two nodes
            id = id2
            p.append(id)
            # run over the path from one node to the other and add the nodes its go through
            while int(id) != id1:
                p.append(int(path[id]))
                id = path[id]
            # reverse the result and return it
            p.reverse()
            return dist[id2], p
        # if nodes does not exist return infinity and empty path
        return float('inf'), []

    # use the plotGraph we build to plot the graph
    def plot_graph(self) -> None:
        plot(self)


# graph plot:
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800


class circle:
    def __init__(self, node: Node, min_x, max_x, min_y, max_y, center: bool):

        if center:
            self.key = node.getKey()
            self.x = ((node.getLocation()[0] - min_x) / (max_x - min_x)) * SCREEN_WIDTH
            self.y = ((node.getLocation()[1] - min_y) / (max_y - min_y)) * SCREEN_HEIGHT
            self._radius = 10
            self.color = (255, 0, 0)
        else:
            self.key = node.getKey()
            self.x = ((node.getLocation()[0] - min_x) / (max_x - min_x)) * SCREEN_WIDTH
            self.y = ((node.getLocation()[1] - min_y) / (max_y - min_y)) * SCREEN_HEIGHT
            self._radius = 3
            self.color = (0, 0, 0)

    def drawBall(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self._radius, 10)


class line:
    def __init__(self, startBall: circle, endBall: circle, draw: bool):
        if draw:
            self._src = (startBall.x, startBall.y)
            self._dest = (endBall.x, endBall.y)
            self.color = (255, 0, 0)
        else:
            self._src = (startBall.x, startBall.y)
            self._dest = (endBall.x, endBall.y)
            self.color = (70, 70, 70)

    def drawLine(self, screen, inOut):
        pygame.draw.line(screen, self.color, self._src, self._dest, 2)
        size = 4
        if inOut == "out":
            x = (self._dest[0], self._dest[1])
            y = (self._dest[0] + size, self._dest[1] - size)
            z = (self._dest[0] + size, self._dest[1] + size)
            pygame.draw.polygon(screen, (0, 0, 0), [x, y, z])

        if inOut == "in":
            x = (self._dest[0] - size, self._dest[1] - size)
            y = (self._dest[0] - size, self._dest[1] + size)
            z = (self._dest[0], self._dest[1])
            pygame.draw.polygon(screen, (0, 0, 0), [x, y, z])


def getBall(balls, node):
    j = 0
    for i in balls:
        if i.key == node.getKey():
            return j
        j += 1


def center(graph, screen, min_x, max_x, min_y, max_y, balls):
    node, dist = graph.centerPoint()
    if node != -1:
        ball = circle(graph.get_graph().get_all_v().get(node), min_x, max_x, min_y, max_y, True)
        ind = getBall(balls, graph.get_graph().get_all_v().get(node))
        balls[ind] = ball
        ball.drawBall(screen)
        pygame.display.update()
        pygame.display.flip()
    else:
        nodeIsNotIn()
        print("there is no center")


def show(graph, min_x, max_x, min_y, max_y):
    # set nodes
    for i in graph.get_graph().get_all_v().keys():
        node = graph.get_graph().get_all_v().get(i)
        graph.nodes.append(node)
        ball = circle(node, min_x, max_x, min_y, max_y, False)
        graph.balls.append(ball)

    # set edges
    for i in graph.nodes:
        ball_i = graph.balls[getBall(graph.balls, i)]
        for j in graph.balls:
            if j.key in i.getEdgesFromNode():
                ln = line(ball_i, j, False)
                graph.lines_out.append(ln)
            if j.key in i.getEdgesToNode():
                ln = line(ball_i, j, False)
                graph.lines_in.append(ln)


def reset(graph, min_x, max_x, min_y, max_y):
    graph.balls = []
    graph.nodes = []
    graph.lines_in = []
    graph.lines_out = []
    # reset nodes
    for i in graph.get_graph().get_all_v().keys():
        node = graph.get_graph().get_all_v().get(i)
        graph.nodes.append(node)
        ball = circle(node, min_x, max_x, min_y, max_y, False)
        graph.balls.append(ball)

    # reset edges
    for i in graph.nodes:
        ball_i = graph.balls[getBall(graph.balls, i)]
        for j in graph.balls:
            if j.key in i.getEdgesFromNode():
                ln = line(ball_i, j, False)
                graph.lines_out.append(ln)
            if j.key in i.getEdgesToNode():
                ln = line(ball_i, j, False)
                graph.lines_in.append(ln)


def notInt():
    q = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    problem_text = font.render('NOT AN INTEGER', False, (0, 0, 0), (255, 255, 255))
    textRect = problem_text.get_rect()
    textRect.center = (580, 400)
    q.blit(problem_text, textRect)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    q.fill((200, 210, 200))
    pygame.display.flip()
    clock.tick(30)


def notEnough():
    q = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    problem_text = font.render('NOT ENOUGH NODES', False, (0, 0, 0), (255, 255, 255))
    textRect = problem_text.get_rect()
    textRect.center = (580, 400)
    q.blit(problem_text, textRect)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    q.fill((200, 210, 200))
    pygame.display.flip()
    clock.tick(30)


def nodeIsNotIn():
    q = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    problem_text = font.render('THERE IS NO CENTER', False, (0, 0, 0), (255, 255, 255))
    textRect = problem_text.get_rect()
    textRect.center = (580, 400)
    q.blit(problem_text, textRect)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    q.fill((200, 210, 200))
    pygame.display.flip()
    clock.tick(30)


def notInG():
    q = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    problem_text = font.render('NODE IS NOT IN THE GRAPH', False, (0, 0, 0), (255, 255, 255))
    textRect = problem_text.get_rect()
    textRect.center = (580, 400)
    q.blit(problem_text, textRect)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    q.fill((200, 210, 200))
    pygame.display.flip()
    clock.tick(30)


def read(graph: GraphAlgo):
    nodes = []
    q = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(550, 300, 500, 32)

    color_inactive = pygame.Color((0, 0, 0))
    color_active = pygame.Color((255, 255, 255))
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == '':
                            done = True
                            break
                        try:
                            if int(text) not in nodes:
                                if int(text) in graph.get_graph().get_all_v().keys():
                                    nodes.append(int(text))
                                else:
                                    notInG()
                                    print("node is not in graph")
                        except Exception as e:
                            notInt()
                            print("not an integer")
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        q.fill((200, 210, 200))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        q.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(q, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

    if len(nodes) == 2:
        shortestPath(graph, nodes[0], nodes[1])
    elif len(nodes) == 0 or len(nodes) == 1:
        notEnough()
        print("not enough nodes")
    else:
        tsp(graph, nodes)


def shortestPath(graph: GraphAlgo, node1, node2):
    dist, path = graph.shortest_path(node1, node2)
    # reset edges
    for i in path:
        node = graph.get_graph().get_all_v().get(i)
        ball_i = graph.balls[getBall(graph.balls, node)]
        for j in graph.balls:
            if j.key in node.getEdgesFromNode() and j.key in path:
                ln = line(ball_i, j, True)
                graph.lines_out.append(ln)
            if j.key in node.getEdgesToNode() and j.key in path:
                ln = line(ball_i, j, True)
                graph.lines_in.append(ln)


def tsp(graph: GraphAlgo, nodes):
    path, dist = graph.TSP(nodes)
    for i in path:
        node = graph.get_graph().get_all_v().get(i)
        ball_i = graph.balls[getBall(graph.balls, node)]
        for j in graph.balls:
            if j.key in node.getEdgesFromNode() and j.key in path:
                ln = line(ball_i, j, True)
                graph.lines_out.append(ln)
            if j.key in node.getEdgesToNode() and j.key in path:
                ln = line(ball_i, j, True)
                graph.lines_in.append(ln)


def plot(graph: GraphAlgo):
    min_x = float('inf')
    max_x = - float('inf')

    min_y = float('inf')
    max_y = - float('inf')

    # set the min and max values to set the scale
    for i in graph.get_graph().get_all_v().keys():
        if graph.get_graph().get_all_v().get(i).getLocation()[0] < min_x:
            min_x = graph.get_graph().get_all_v().get(i).getLocation()[0]

    for i in graph.get_graph().get_all_v().keys():
        if graph.get_graph().get_all_v().get(i).getLocation()[0] > max_x:
            max_x = graph.get_graph().get_all_v().get(i).getLocation()[0]

    for i in graph.get_graph().get_all_v().keys():
        if graph.get_graph().get_all_v().get(i).getLocation()[1] < min_y:
            min_y = graph.get_graph().get_all_v().get(i).getLocation()[1]

    for i in graph.get_graph().get_all_v().keys():
        if graph.get_graph().get_all_v().get(i).getLocation()[1] > max_y:
            max_y = graph.get_graph().get_all_v().get(i).getLocation()[1]

    # define the screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("menu")

    running = True
    show(graph, min_x, max_x, min_y, max_y)
    # run the plot
    clock = pygame.time.Clock()
    while running:
        clock.tick(10)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Clear the screan
        screen.fill((200, 210, 200))

        resetB = Button(
            screen, 0, 0, 150, 40, text='reset changes',
            fontSize=25, margin=5,
            inactiveColour=(255, 255, 255),
            pressedColour=(70, 70, 70), radius=0,
            onClick=lambda: reset(graph, min_x, max_x, min_y, max_y)
        )
        centerB = Button(
            screen, 150, 0, 100, 40, text='center',
            fontSize=25, margin=5,
            inactiveColour=(255, 255, 255),
            pressedColour=(70, 70, 70), radius=0,
            onClick=lambda: center(graph, screen, min_x, max_x, min_y, max_y, graph.balls)
        )
        shorterB = Button(
            screen, 250, 0, 150, 40, text='shortest path',
            fontSize=25, margin=5,
            inactiveColour=(255, 255, 255),
            pressedColour=(70, 70, 70), radius=0,
            onClick=lambda: read(graph)
        )
        TSPB = Button(
            screen, 400, 0, 100, 40, text='TSP',
            fontSize=25, margin=5,
            inactiveColour=(255, 255, 255),
            pressedColour=(70, 70, 70), radius=0,
            onClick=lambda: read(graph)
        )

        for i in graph.balls:
            i.drawBall(screen)
        for i in graph.lines_out:
            i.drawLine(screen, "out")
        for i in graph.lines_in:
            i.drawLine(screen, "in")

        pygame_widgets.update(events)
        pygame.display.flip()
