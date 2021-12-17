from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self, name, nodes, nodeEdges, edges):
        self._name = name
        self._nodes = nodes
        self._nodeEdges = nodeEdges
        self._edges = edges

    def copy(self, attrs=None):
        new_attrs = {k: v.copy() for k, v in self.attrs.items()} if attrs is None else attrs
        return DiGraph(name=self._name, nodes=self._nodes, nodeEdges=self._nodeEdges, edges=self._edges, attrs=new_attrs)

    