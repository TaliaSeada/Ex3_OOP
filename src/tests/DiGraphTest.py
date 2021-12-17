import unittest

from src.DiGraph import DiGraph
from src.Edge import Edge
from src.Node import Node


class MyTestCase(unittest.TestCase):
    def test_Graph(self):
        node = Node(0, [1.0, 2.0, 0.0])
        node1 = Node(1, [3.0, 4.0, 0.0])
        node2 = Node(2, [5.0, 6.0, 0.0])

        edge = Edge(node.getKey(), 1.0, node1.getKey())
        edge1 = Edge(node1.getKey(), 2.0, node2.getKey())
        edge2 = Edge(node2.getKey(), 3.0, node.getKey())

        edge3 = Edge(node1.getKey(), 1.0, node.getKey())
        edge4 = Edge(node2.getKey(), 2.0, node1.getKey())

        nodes = {'0': node, '1': node1, '2': node2}
        edges = [edge, edge1, edge2, edge3, edge4]

        graph = DiGraph("G1", nodes, edges)

        # getters
        self.assertNotEqual(graph, None)
        v_size = graph.v_size()
        self.assertEqual(v_size, 3)
        e_size = graph.e_size()
        self.assertEqual(e_size, 5)
        v = graph.get_all_v()
        self.assertEqual(v, nodes)

        # addNode
        self.assertTrue(graph.add_node(3, (7.0, 8.0, 0.0)))
        self.assertFalse(graph.add_node(3, (7.0, 8.0, 0.0)))

        # removeNode
        self.assertTrue(graph.remove_node(3))
        self.assertFalse(graph.remove_node(3))

        # addEdge
        self.assertTrue(graph.add_edge(0, 2, 3.0))
        self.assertFalse(graph.add_edge(0, 2, 3.0))

        # removeEdge
        self.assertTrue(graph.remove_edge(0, 2))
        self.assertFalse(graph.remove_edge(0, 2))

        # mc
        self.assertEqual(graph.get_mc(), 4)

        # all edges
        allIn = {str(node1.getKey()): edge3.getWeight(), str(node2.getKey()): edge2.getWeight()}
        self.assertEqual(allIn, graph.all_in_edges_of_node(node.getKey()))

        allOut = {str(node1.getKey()): edge.getWeight()}
        self.assertEqual(allOut, graph.all_out_edges_of_node(node.getKey()))

if __name__ == '__main__':
    unittest.main()
