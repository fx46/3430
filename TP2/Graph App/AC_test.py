import generators
import unittest

class TestSimpleGraphGeneratorsAC(unittest.TestCase):

    def setUp(self):
        self.simpleGraph = None
        self.simpleGraph_Probility = None

    #############################################################################
    #
    # Simple
    #
    # V1 = {V<0}                    	[erreur]
    # V2 = {V>=0}                    	[propriete: NbVerticesvalid]
    # E1 = {E<0}                    	[erreur]
    # E2 = {E > V*(V-1)/2}              [erreur]
    # E3 = {0 <= E <= V*(V-1)/2}        [propriete: NbEdgesvalid]
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

if __name__ == '__main__':
    unittest.main()