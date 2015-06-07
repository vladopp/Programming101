from gitsoc import DirectedGraph
import unittest


class testgraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_edge("az", "teb")

    def test_add_edge_baisc(self):
        self.assertEqual(self.graph.graph["az"], ["teb"])
        self.assertEqual(self.graph.graph["teb"], [])

    def test_get_neighbors_for(self):
        self.assertEqual(self.graph.get_neighbors_for("az"), ["teb"])
        self.assertEqual(self.graph.get_neighbors_for("teb"), [])

    def test_path_between(self):
        self.assertTrue(self.graph.path_between("az", "teb"))

if __name__ == '__main__':
    unittest.main()
