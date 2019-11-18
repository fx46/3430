import unittest

from NodeTest import NodeTest
from LinkedListTest import LinkedListTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(NodeTest))
suite.addTest(unittest.makeSuite(LinkedListTest))

unittest.TextTestRunner(verbosity=2).run(suite)