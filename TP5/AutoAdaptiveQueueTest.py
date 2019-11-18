import unittest
import io
import sys

from app import AutoAdaptiveQueue

class AutoAdaptiveQueueTest(unittest.TestCase):

    def setUp(self):
        self.autoQueue3 = AutoAdaptiveQueue(3, 3, 3)

    # Test __init__() 
    def testInit(self):
        self.assertEqual(self.autoQueue3.max_trials, 3)
        self.assertEqual(self.autoQueue3.size_increment, 3)
        self.assertEqual(self.autoQueue3.trials, 0)

    # Test __init__() -> Enqueue()
    def testEnqueue(self):
        oldMaxSize = self.autoQueue3.max_size

        self.assertTrue(self.autoQueue3.isEmpty())
        self.autoQueue3.enqueue("test1")
        self.autoQueue3.enqueue("test2")
        self.autoQueue3.enqueue("test3")
        self.assertTrue(self.autoQueue3.isFull())
       
        sys.stdout = io.StringIO()

        for i in range(self.autoQueue3.max_trials):
            self.assertRaises(ValueError, self.autoQueue3.enqueue("test4"))

        sys.stdout = sys.__stdout__  

        self.autoQueue3.enqueue("test4")
        self.assertEqual(self.autoQueue3.max_size, oldMaxSize + self.autoQueue3.size_increment)
