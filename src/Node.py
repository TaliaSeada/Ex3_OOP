from src import Edge


class Node:
    def __init__(self, key, location, edgesToNode, edgesFromNode, tag):
        self._key = key
        self._location = location
        self._edgesToNode = edgesToNode
        self._edgesFromNode = edgesFromNode
        self._tag = tag

    def addEdge(self, edge: Edge):
        if edge.getSrc() == self._key:
            self._edgesFromNode.append(edge)
        elif edge.getDest() == self._key:
            self._edgesToNode.append(edge)

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


