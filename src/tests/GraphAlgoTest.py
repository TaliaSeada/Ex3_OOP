import unittest

from src.DiGraph import DiGraph
from src.Edge import Edge
from src.Node import Node
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_load(self):
        Agraph = GraphAlgo()
        fileName = "C:\\Users\\talia\\PycharmProjects\\Ex3_OOP\\data\\A0"
        self.assertFalse(Agraph.load_from_json(fileName))
        fileName = "C:\\Users\\talia\\PycharmProjects\\Ex3_OOP\\data\\A0.json"
        self.assertTrue(Agraph.load_from_json(fileName))
        self.assertEqual(Agraph.get_graph().v_size(), 11)





