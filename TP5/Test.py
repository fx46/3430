import unittest

from NodeTest import NodeTest
from LinkedListTest import LinkedListTest
from QueueTest import QueueTest
from StackTest import StackTest
from AutoAdaptiveQueueTest import AutoAdaptiveQueueTest
from AutoAdaptiveStackTest import AutoAdaptiveStackTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(NodeTest))
suite.addTest(unittest.makeSuite(LinkedListTest))
suite.addTest(unittest.makeSuite(QueueTest))
suite.addTest(unittest.makeSuite(StackTest))
suite.addTest(unittest.makeSuite(AutoAdaptiveQueueTest))
suite.addTest(unittest.makeSuite(AutoAdaptiveStackTest))

unittest.TextTestRunner(verbosity=2).run(suite)