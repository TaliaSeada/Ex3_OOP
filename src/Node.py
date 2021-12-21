from src import Edge


class Node:
    def __init__(self, key: int):
        self._key = key
        self._location = ()
        self._edgesToNode = {}
        self._edgesFromNode = {}
        self._tag = 0

    def __repr__(self):
        s = str(str(self._key) + ": |edges out| " + str(len(self._edgesFromNode)) + " |edges in| " + str(len(self._edgesToNode)))
        return repr(s)

    def addEdge(self, edge: Edge):
        if edge.getSrcNode() == self._key:
            self._edgesFromNode[edge.getDestNode()] = edge.getWeight()
        elif edge.getDestNode() == self._key:
            self._edgesToNode[edge.getSrcNode()] = edge.getWeight()

    def removeEdge(self, edge: Edge):
        if edge.getSrcNode() == self._key:
            del self._edgesFromNode[edge.getDestNode()]
        elif edge.getDestNode() == self._key:
            del self._edgesToNode[edge.getSrcNode()]

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


