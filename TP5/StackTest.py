import unittest

from app import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)

    # Test __init__() 
    def testInit(self):
        self.assertEqual(self.stack.max_size, 3)

    # Test __init__() -> push() -> pop()
    def testPushPop(self):
        self.stack.push("test")
        self.assertFalse(self.stack.isEmpty())
        self.assertTrue(self.stack.size() == 1)
        self.assertEqual(self.stack.check().value, "test")
        self.assertEqual(self.stack.peek().value, "test")
        self.assertTrue(self.stack.isEmpty())

        self.stack.push("test1")
        self.stack.push("test2")
        self.stack.push("test3")
        self.assertTrue(self.stack.isFull())
        self.assertEqual(self.stack.size(), self.stack.max_size)
        try:
            self.stack.push("test4")
        except Exception as ex:
            self.assertEqual(str(ex), "Stack overflow")
            
        self.assertEqual(self.stack.pop().value, "test3")
        self.assertEqual(self.stack.pop().value, "test2")
        self.assertEqual(self.stack.pop().value, "test1")
        try:
            self.stack.pop()
        except Exception as ex:
            self.assertEqual(str(ex), "Stack underflow")
