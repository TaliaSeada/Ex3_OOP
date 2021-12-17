from src import Edge


class Node:
    def __init__(self, key, location):
        self._key = key
        self._location = tuple(location)
        self._edgesToNode = {}
        self._edgesFromNode = {}
        self._tag = 0

    def addEdge(self, edge: Edge):
        if edge.getSrcNode() == self._key:
            self._edgesFromNode[str(edge.getDestNode())] = edge.getWeight()
        elif edge.getDestNode() == self._key:
            self._edgesToNode[str(edge.getSrcNode())] = edge.getWeight()

    def removeEdge(self, edge: Edge):
        if edge.getSrcNode() == self._key:
            del self._edgesFromNode[str(edge.getDestNode())]
        elif edge.getDestNode() == self._key:
            del self._edgesToNode[str(edge.getSrcNode())]

    # getters
    def getKey(self):
        return self._key

    def getLocation(self):
        return self._location

    def getTag(self):
        return self._tag

    def getEdgesToNode(self):
        return self._edgesToNode

    def getEdgesFromNode(self):
        return self._edgesFromNode

    # setters
    def setKey(self, k):
        self._key = k

    def setLocation(self, loc):
        self._location = loc

    def setTag(self, t):
        self._tag = t


