import unittest

from NodeTest import NodeTest
from LinkedListTest import LinkedListTest
from QueueTest import QueueTest
from StackTest import StackTest
from AutoAdaptiveQueueTest import AutoAdaptiveQueueTest
from AutoAdaptiveStackTest import AutoAdaptiveStackTest
from CalculatorTest import CalculatorTest
from ScreenPrinterTest import ScreenPrinterTest
from FilePrinterTest import FilePrinterTest

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(NodeTest))
suite.addTest(unittest.makeSuite(LinkedListTest))
suite.addTest(unittest.makeSuite(QueueTest))
suite.addTest(unittest.makeSuite(StackTest))
suite.addTest(unittest.makeSuite(AutoAdaptiveQueueTest))
suite.addTest(unittest.makeSuite(AutoAdaptiveStackTest))
suite.addTest(unittest.makeSuite(CalculatorTest))
suite.addTest(unittest.makeSuite(ScreenPrinterTest))
suite.addTest(unittest.makeSuite(FilePrinterTest))

unittest.TextTestRunner(verbosity=2).run(suite)