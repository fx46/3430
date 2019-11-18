import unittest
import io
import sys

from app import AutoAdaptiveStack

class AutoAdaptiveStackTest(unittest.TestCase):

    def setUp(self):
        self.autoStack3 = AutoAdaptiveStack(3, 3, 3)

    # Test __init__() 
    def testInit(self):
        self.assertEqual(self.autoStack3.max_trials, 3)
        self.assertEqual(self.autoStack3.size_increment, 3)
        self.assertEqual(self.autoStack3.trials, 0)

    # Test __init__() -> Push()
    def testPush(self):
        oldMaxSize = self.autoStack3.max_size

        self.assertTrue(self.autoStack3.isEmpty())
        self.autoStack3.push("test1")
        self.autoStack3.push("test2")
        self.autoStack3.push("test3")
        self.assertTrue(self.autoStack3.isFull())
       
        sys.stdout = io.StringIO()

        for i in range(self.autoStack3.max_trials):
            self.assertRaises(ValueError, self.autoStack3.push("test4"))

        sys.stdout = sys.__stdout__  

        self.autoStack3.push("test4")
        self.assertEqual(self.autoStack3.max_size, oldMaxSize + self.autoStack3.size_increment)