from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes = {}
        self._edges = []
        self.visited = []
        self.mc = 0

    # def __init__(self, nodes, edges):
    #     self._nodes = dict(nodes)
    #     for edge in edges:
    #         node1 = self._nodes[str(edge.getSrcNode())]
    #         node1.addEdge(edge)
    #         node2 = self._nodes[str(edge.getDestNode())]
    #         node2.addEdge(edge)
    #     self._edges = list(edges)
    #     self.mc = 0

    def get_graph(self):
        return self

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        newNode = Node(node_id, pos)
        if str(node_id) not in self._nodes.keys():
            self._nodes[str(node_id)] = newNode
            self.mc += 1
            return True
        else:
            return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        # node = self._nodes[str(id1)]
        # inEdges = {}
        # for key in (node.getEdgesToNode().keys()):
        #     inEdges[str(key)] = node.getEdgesToNode()[str(key)]
        return self._nodes.get(str(id1)).getEdgesToNode()

    def all_out_edges_of_node(self, id1: int) -> dict:
        # node = self._nodes[str(id1)]
        # outEdges = {}
        # for key in (node.getEdgesFromNode().keys()):
        #     outEdges[str(key)] = node.getEdgesFromNode()[str(key)]
        return self._nodes.get(str(id1)).getEdgesFromNode()

    def remove_node(self, node_id: int) -> bool:
        try:
            in_edges = self.all_in_edges_of_node(node_id)
            out_edges = self.all_out_edges_of_node(node_id)
            for key in in_edges:
                self.remove_edge(key, node_id)
            for key in out_edges:
                self.remove_edge(key, node_id)
            del self._nodes[str(node_id)]
            self.mc += 1
            return True
        except KeyError:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if str(node_id1) in self._nodes.keys() and str(node_id2) in self._nodes.keys():
            i = 0
            while i < len(self._edges):
                edge = self._edges[i]
                if edge.getSrcNode() == node_id1 and edge.getDestNode() == node_id2:
                    self._edges.remove(edge)
                    node1 = self._nodes[str(edge.getSrcNode())]
                    node1.removeEdge(edge)
                    node2 = self._nodes[str(edge.getDestNode())]
                    node2.removeEdge(edge)
                    self.mc += 1
                    return True
                i = i + 1
        else:
            return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        try:
            if str(id1) in self._nodes.keys() and str(id2) in self._nodes.keys():
                newEdge = Edge(id1, weight, id2)
                for edge in self._edges:
                    if edge.getSrcNode() == id1 and edge.getDestNode() == id2:
                        return False
                self._edges.append(newEdge)
                node1 = self._nodes[str(id1)]
                node1.addEdge(newEdge)
                node2 = self._nodes[str(id2)]
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

