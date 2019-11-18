import unittest

from NodeTest import NodeTest
from LinkedListTest import LinkedListTest
from QueueTest import QueueTest
from StackTest import StackTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(NodeTest))
suite.addTest(unittest.makeSuite(LinkedListTest))
suite.addTest(unittest.makeSuite(QueueTest))
suite.addTest(unittest.makeSuite(StackTest))

unittest.TextTestRunner(verbosity=2).run(suite)