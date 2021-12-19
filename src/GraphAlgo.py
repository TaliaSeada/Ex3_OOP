import io
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
        self._graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self._graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

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
                    D[i] = D[nodeKey]+1
        # reset tags
        for n in v_group:
            v_group.get(n).setTag(0)
        return max(D.values())

    def reverse_graph(self, g: GraphInterface):
        rever = DiGraph()
        rever_v = g.get_all_v()
        for key in rever_v.keys():
            node = rever_v.get(key)
            rever_e_out = g.all_out_edges_of_node(node.getKey())
            rever_e_in = g.all_in_edges_of_node(node.getKey())
            rever.add_node(node.getKey(), node.getLocation())
            for edge in rever_e_out:
                rever.add_edge(int(edge), int(key), rever_e_out.get(edge))
            for edge in rever_e_in:
                rever.add_edge(int(key), int(edge), rever_e_in.get(edge))
        return rever

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
        bfs_rev = self.bfs(key, self.reverse_graph(self._graph))
        if bfs_rev == float('inf'):
            return False
        return True

    def centerPoint(self) -> (int, float):
        if self.isConnected():
            longest = {v: float('inf') for v in self._graph.get_all_v().keys()}
            for v in self._graph.get_all_v().keys():
                dist, path = self.dijkstra(int(v))
                longest[v] = max(dist.values())
            min_index = float('inf')
            index = -1
            for key in longest.keys():
                if longest[key] < min_index:
                    min_index = longest[key]
                    index = int(key)
            return index, min_index
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
            for i in data["Edges"]:
                src = int(i["src"])
                dest = int(i["dest"])
                weight = float(i["w"])
                self._graph.add_edge(src, dest, weight)
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
                currNode = {"pos":(str(x) + "," + str(y) + "," + str(z)), "id": id}
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
            return True
        except Exception as e:
            print(e)
            return False

    def dijkstra(self, id1: int):
        D = {v: float('inf') for v in self._graph.get_all_v().keys()}
        D[str(id1)] = 0
        path = {v: None for v in self._graph.get_all_v().keys()}

        pq = PriorityQueue()
        pq.put((0, id1))

        while not pq.empty():
            (dist, current) = pq.get()
            self._graph.visited.append(current)

            for neighbor in self._graph.get_all_v().keys():
                if self._graph.all_out_edges_of_node(current).__contains__(neighbor):
                    distance = self._graph.all_out_edges_of_node(current)[neighbor]
                    if neighbor not in self._graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[str(current)] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            path[neighbor] = str(current)
                            D[neighbor] = new_cost
        self._graph.visited = []
        return D, path

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self._graph.get_all_v().__contains__(str(id1)) and self._graph.get_all_v().__contains__(str(id2)):
            p = []
            dist, path = self.dijkstra(id1)
            if dist[str(id2)] == float('inf'):
                return float('inf'), p
            id = id2
            p.append(id)
            while id != id1:
                p.append(int(path[str(id)]))
                id = path[str(id)]
            p.reverse()
            return dist[str(id2)], p
        return float('inf'), []


    def plot_graph(self) -> None:
        pass
















