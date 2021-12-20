import unittest

from src.DiGraph import DiGraph
from src.Edge import Edge
from src.Node import Node
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_load(self):
        Agraph = GraphAlgo()
        # fileName = "../../data/A0"
        # self.assertFalse(Agraph.load_from_json(fileName))
        fileName = "../../data/A1.json"
        self.assertTrue(Agraph.load_from_json(fileName))
        self.assertEqual(Agraph.get_graph().v_size(), 17)

    def test_save(self):
        Agraph = GraphAlgo()
        fileName = "../../data/A1.json"
        self.assertTrue(Agraph.load_from_json(fileName))
        self.assertTrue(Agraph.save_to_json('test.json'))
        self.assertTrue(Agraph.load_from_json('test.json'))

    def test_center(self):
        Agraph = GraphAlgo()
        fileName = "../../data/G1.json"
        Agraph.load_from_json(fileName)
        self.assertEqual(Agraph.centerPoint()[0], 8)
        fileName = "../../data/G2.json"
        Agraph.load_from_json(fileName)
        self.assertEqual(Agraph.centerPoint()[0], 0)
        fileName = "../../data/G3.json"
        Agraph.load_from_json(fileName)
        self.assertEqual(Agraph.centerPoint()[0], 40)

    def test_shortest_path(self):
        Agraph = GraphAlgo()
        fileName = "../../data/G1.json"
        Agraph.load_from_json(fileName)
        list = [0,1,2,6]
        self.assertEqual(list, Agraph.shortest_path(0,6)[1])

