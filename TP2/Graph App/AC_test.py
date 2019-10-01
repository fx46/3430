import generators
import unittest

class TestSimpleGraphGeneratorsAC(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = None
        self.simpleGraph_Probility = None
        self.bipartiteGraph = None

    #############################################################################
    #
    # Simple
    #
    # V1 = {V<0}                    	[erreur]
    # V2 = {V>=0}
    # E1 = {E<0}                    	[erreur]
    # E2 = {E > V*(V-1)/2}              [erreur]
    # E3 = {0 <= E <= V*(V-1)/2}
    #
    #############################################################################

    def test_simple_V1E1(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(-1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is None and bException)

    def test_simple_V1E2(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(-1, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is None and bException)

    def test_simple_V1E3(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(-1, 1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is None and bException)

    def test_simple_V2E1(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is None and bException)

    def test_simple_V2E2(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(1, 1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is None and bException is True)

    def test_simple_V2E3(self):
        bException = False
    
        try:
            self.simpleGraph = generators.simple(3, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph is not None and bException is False)

    #############################################################################
    #
    # Simple_with_probability
    #
    # V1 = {V<0}           	    [ValueError]
    # V2 = {V>=0}
    # P1 = {P<0.0}           	[ValueError]
    # P2 = {P>1.0}           	[ValueError]
    # P3 = {0 <= P <= 1}
    #
    #############################################################################

    def test_simple_graph_probility_V1P1(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(-1, -0.1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is None and bException is True)

    def test_simple_graph_probility_V1P2(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(-1, 1.1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is None and bException is True)

    def test_simple_graph_probility_V1P3(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(-1, 0.5)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is None and bException is True)

    def test_simple_graph_probility_V2P1(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(2, -0.1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is None and bException is True)

    def test_simple_graph_probility_V2P2(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(2, 1.1)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is None and bException is True)

    def test_simple_graph_probility_V2P3(self):
        bException = False

        try:
            self.simpleGraph_Probility = generators.simple_with_probability(2, 0.5)
        except ValueError:
            bException = True

        self.assertTrue(self.simpleGraph_Probility is not None and bException is False)

    #############################################################################
    #
    # Bipartite
    #
    # V1_1 = {V<0}           	[ValueError]
    # V1_2 = {V>=0}
    # V2_1 = {V<0}           	[ValueError]
    # V2_2 = {V>=0}
    # E1 = {E<0}           	    [ValueError]
    # E2 = {E>V1*V2}         	[ValueError]
    # E3 = {0 <= E <= V1*V2}
    #
    #############################################################################

    def test_bipartite_V1_1V2_1E1(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(-1, -1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V2_1V2_1E2(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(-1, -1, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V1_1V2_1E3(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(-1, -1, 1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V1_1V2_2E1(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(-1, 1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V2_1V2_2E2(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(-1, 1, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V1_2V2_1E1(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(1, -1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V2_2V2_1E2(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(1, -1, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V1_2V2_2E1(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(1, 1, -1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V2_2V2_2E2(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(1, 1, 2)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is None and bException is True)

    def test_bipartite_V1_2V2_2E3(self):
        bException = False

        try:
            self.bipartiteGraph = generators.bipartite(1, 1, 1)
        except ValueError:
            bException = True

        self.assertTrue(self.bipartiteGraph is not None and bException is False)



if __name__ == '__main__':
    unittest.main()