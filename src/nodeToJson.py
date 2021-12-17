from src import Node


class nodeToJson:
    def __init__(self, node: Node):
        self._location = node.getLocation()
        self._id = node.getKey()

    # getters
    def getPos(self):
        return self._location

    def getId(self):
        return self._id

    # setters
    def setPos(self, pos):
        self._location = pos

    def setId(self, key):
        self._id = key


