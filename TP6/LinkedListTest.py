import unittest

from app import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linkedList = LinkedList()

    # Test __init__() 
    def test_a_Init(self):
        self.assertTrue(self.linkedList.isEmpty())

    # Test __init__() -> IsEmpty() -> size() -> check() -> peek() -> append() -> size() -> check() -> peek()
    def test_b_IsEmptyThenAppendThenIsNotEmpty(self):
        self.assertTrue(self.linkedList.isEmpty())
        self.assertEqual(self.linkedList.size(), 0)
        self.assertRaises(ValueError, self.linkedList.check)
        self.assertRaises(ValueError, self.linkedList.peek)

        self.linkedList.append('test')
        self.assertFalse(self.linkedList.isEmpty())
        self.assertEqual(self.linkedList.size(), 1)
        self.assertEqual(self.linkedList.check().value, 'test')
        self.assertEqual(self.linkedList.peek().value, 'test')
        self.assertTrue(self.linkedList.isEmpty())
        self.assertEqual(self.linkedList.size(), 0)

        self.linkedList.append('test1')
        self.linkedList.append('test2')
        self.linkedList.append('test3')
        self.assertFalse(self.linkedList.isEmpty())
        self.assertEqual(self.linkedList.size(), 3)
        self.assertEqual(self.linkedList.check().value, 'test1')
        self.assertEqual(self.linkedList.peek().value, 'test1')
        self.assertEqual(self.linkedList.size(), 2)
        self.assertEqual(self.linkedList.peek().value, 'test2')
        self.assertEqual(self.linkedList.size(), 1)
        self.assertEqual(self.linkedList.peek().value, 'test3')
        self.assertEqual(self.linkedList.size(), 0)
        self.assertTrue(self.linkedList.isEmpty())

    # Test __init__() -> IsEmpty() -> Prepend() -> Prepend() -> check() -> peek()
    def test_c_Prepend(self):
        self.assertTrue(self.linkedList.isEmpty())
        self.linkedList.prepend('test1')

        self.linkedList.prepend('test2')
        self.assertEqual(self.linkedList.check().value, 'test2')

        self.assertEqual(self.linkedList.peek().value, 'test2')
        self.assertEqual(self.linkedList.peek().value, 'test1')
        self.assertTrue(self.linkedList.isEmpty())
