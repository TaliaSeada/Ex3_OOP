import time
from heapq import *
from typing import List
import json
from queue import PriorityQueue

import os
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Node import Node
from src.Edge import Edge


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self._revGraph = DiGraph()
        self._graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self._graph

    def min_index(self, srcNode, dist_v, node_lst, passed):
        min = float('inf')
        index = 0
        for key in node_lst:
            if dist_v.get(str(key)) < min and key != srcNode and key not in passed:
                index = int(key)
                min = dist_v.get(str(key))
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
            dist += dist_v.get(str(min_ind))
            v = min_ind

        return path, dist

    def bfs(self, nodeKey: int, g: DiGraph):
        D = {v: float('inf') for v in self._graph.get_all_v().keys()}
        D[str(nodeKey)] = 0
        queue = []
        nodeDict = g.get_all_v()
        node = nodeDict.get(str(nodeKey))

        # Mark the source node as visited and enqueue it
        node.setTag(2)
        queue.append(str(nodeKey))
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
        for i in self._graph.get_all_v().keys():
            key = i
            break
        bfs = self.bfs(key, self._graph)
        if bfs == float('inf'):
            return False
        bfs_rev = self.bfs(key, self._revGraph)
        if bfs_rev == float('inf'):
            return False
        return True

    def centerPoint(self) -> (int, float):
        if self.isConnected():
            minDist = float('inf')
            minIndex = -1
            for v in self._graph.get_all_v().keys():
                dist, path = self.dijkstra(int(v))
                if max(dist.values()) < minDist:
                    minDist = max(dist.values())
                    minIndex = int(v)
            return minIndex, minDist
        else:
            return -1, float('inf')

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            for i in data["Nodes"]:
                id = i['id']
                pos = i['pos']
                xyz = pos.split(',')
                for i in range(len(xyz)):
                    xyz[i] = float(xyz[i])
                self._graph.add_node(id, xyz)
                self._revGraph.add_node(id, xyz)
            for i in data["Edges"]:
                src = int(i["src"])
                dest = int(i["dest"])
                weight = float(i["w"])
                self._graph.add_edge(src, dest, weight)
                self._revGraph.add_edge(dest, src, weight)
            file.close()
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            nodes = []
            edges = []
            nodeDict = self._graph.get_all_v()
            for node in nodeDict:
                thisNode = nodeDict[node]
                location = thisNode.getLocation()
                x = location[0]
                y = location[1]
                z = location[2]
                id = int(node)
                currNode = {"pos": (str(x) + "," + str(y) + "," + str(z)), "id": id}
                nodes.append(currNode)
                allOutEdges = self._graph.all_out_edges_of_node(id)
                for edge in allOutEdges.keys():
                    src = id
                    dest = int(edge)
                    weight = allOutEdges[edge]
                    edgeCurr = {"src": id, "w": weight, "dest": dest}
                    edges.append(edgeCurr)
            all = {"Edges": edges, "Nodes": nodes}
            with open(file_name, "w") as file:
                file.write(json.dumps(all, indent=4))
            file.close()
            return True
        except Exception as e:
            print(e)
            return False

    def dijkstra(self, src: int):
        # print(src)
        Distances = {}
        lastPath = {}
        for v in self._graph.get_all_v():
            Distances[v] = float('inf')
            lastPath[v] = None
        Distances[str(src)] = 0
        h = []
        all_v = self._graph.get_all_v()
        heappush(h, (Distances[str(src)], str(src)))
        while h:
            currNode = heappop(h)[1]
            all_v.get(str(currNode)).setTag(2)
            outEdges = self._graph.all_out_edges_of_node(int(currNode))
            for edge in outEdges.keys():
                if all_v.get(str(edge)).getTag() != 2:
                    currDist = Distances.get(edge)
                    newDist = Distances.get(currNode) + outEdges.get(edge)
                    if newDist < currDist:
                        heappush(h, (newDist, edge))
                        Distances[edge] = newDist
                        lastPath[edge] = currNode
        for v in all_v:
            all_v.get(v).setTag(0)
        return Distances, lastPath

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self._graph.get_all_v().__contains__(str(id1)) and self._graph.get_all_v().__contains__(str(id2)):
            p = []
            dist, path = self.dijkstra(id1)
            if dist[str(id2)] == float('inf'):
                return float('inf'), p
            id = id2
            p.append(id)
            while int(id) != id1:
                p.append(int(path[str(id)]))
                id = path[str(id)]
            p.reverse()
            return dist[str(id2)], p
        return float('inf'), []

    def plot_graph(self) -> None:
        pass
