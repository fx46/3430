import unittest

from NodeTest import NodeTest
from LinkedListTest import LinkedListTest
from QueueTest import QueueTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(NodeTest))
suite.addTest(unittest.makeSuite(LinkedListTest))
suite.addTest(unittest.makeSuite(QueueTest))

unittest.TextTestRunner(verbosity=2).run(suite)