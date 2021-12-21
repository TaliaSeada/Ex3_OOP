import random

from src.Edge import Edge
from src.api.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes = {}
        self._edges = []
        self.mc = 0

    def __repr__(self):
        return "Graph: |V|={},|E|={}".format(len(self._nodes), len(self._edges))

    def get_graph(self):
        return self

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos is not None:
            newNode = Node(node_id)
            newNode.setLocation(pos)
            if node_id not in self._nodes.keys():
                self._nodes[node_id] = newNode
                self.mc += 1
                return True
            else:
                return False
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = 0.0
            pos = (x, y, z)
            newNode = Node(node_id)
            newNode.setLocation(pos)
            if node_id not in self._nodes.keys():
                self._nodes[node_id] = newNode
                self.mc += 1
                return True
            else:
                return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._nodes.get(id1).getEdgesToNode()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._nodes.get(id1).getEdgesFromNode()

    def remove_node(self, node_id: int) -> bool:
        try:
            if node_id not in self._nodes:
                return False
            in_edges = self.all_in_edges_of_node(node_id)
            out_edges = self.all_out_edges_of_node(node_id)
            for key in in_edges:
                self.remove_edge(key, node_id)
            for key in out_edges:
                self.remove_edge(key, node_id)
            del self._nodes[node_id]
            self.mc += 1
            return True
        except KeyError:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self._nodes.keys() and node_id2 in self._nodes.keys():
            i = 0
            while i < len(self._edges):
                edge = self._edges[i]
                if edge.getSrcNode() == node_id1 and edge.getDestNode() == node_id2:
                    self._edges.remove(edge)
                    node1 = self._nodes[edge.getSrcNode()]
                    node1.removeEdge(edge)
                    node2 = self._nodes[edge.getDestNode()]
                    node2.removeEdge(edge)
                    self.mc += 1
                    return True
                i = i + 1
        else:
            return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        try:
            if id1 in self._nodes.keys() and id2 in self._nodes.keys():
                newEdge = Edge(id1, weight, id2)
                for edge in self._edges:
                    if edge.getSrcNode() == id1 and edge.getDestNode() == id2:
                        return False
                self._edges.append(newEdge)
                node1 = self._nodes[id1]
                node1.addEdge(newEdge)
                node2 = self._nodes[id2]
                node2.addEdge(newEdge)
                self.mc += 1
                return True
            else:
                return False
        except KeyError:
            return False

    def get_all_v(self) -> dict:
        return self._nodes

    def get_mc(self) -> int:
        return self.mc

    def e_size(self) -> int:
        return len(self._edges)

    def v_size(self) -> int:
        return len(self._nodes)

    def reverse_graph(self, g: GraphInterface):
        rever = DiGraph()
        rever_v = g.get_all_v()
        for key in rever_v.keys():
            node = rever_v.get(key)
            rever_e_out = g.all_out_edges_of_node(node.getKey())
            rever_e_in = g.all_in_edges_of_node(node.getKey())
            rever.add_node(node.getKey(), node.getLocation())
            for edge in rever_e_out:
                rever.add_edge(edge, key, rever_e_out.get(edge))
            for edge in rever_e_in:
                rever.add_edge(key, edge, rever_e_in.get(edge))
        return rever

