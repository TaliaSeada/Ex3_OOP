import unittest

from src.Edge import Edge
from src.Node import Node


class MyTestCase(unittest.TestCase):
    def test_Node(self):
        node = Node(0)

        self.assertNotEqual(node, None)

        key = node.getKey()
        loc = node.getLocation()
        edToN = node.getEdgesToNode()
        edFrN = node.getEdgesFromNode()
        tag = node.getTag()

        # getters
        self.assertEqual(key, 0)
        self.assertEqual(loc, ())
        self.assertEqual(edToN, {})
        self.assertEqual(edFrN, {})
        self.assertEqual(tag, 0)

        # setters
        node.setTag(0)
        node.setKey(3)
        node.setLocation((3.0, 4.0, 7.0))

        key = node.getKey()
        loc = node.getLocation()
        tag = node.getTag()

        self.assertEqual(key, 3)
        self.assertEqual(loc, (3.0, 4.0, 7.0))
        self.assertEqual(tag, 0)

        # addEdge
        edge = Edge(3, 1.0, 1)
        node.addEdge(edge)
        edge2 = Edge(1, 1.0, 3)
        node.addEdge(edge2)

        edToN = node.getEdgesToNode()
        edFrN = node.getEdgesFromNode()

        e = {str(edge.getDestNode()): edge.getWeight()}
        e2 = {str(edge2.getSrcNode()): edge2.getWeight()}
        self.assertEqual(edFrN, e)
        self.assertEqual(edToN, e2)

        # removeEdge
        node.removeEdge(edge)
        self.assertEqual(edFrN, {})
        node.removeEdge(edge2)
        self.assertEqual(edToN, {})

if __name__ == '__main__':
    unittest.main()

