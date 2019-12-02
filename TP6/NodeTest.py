import unittest

from app import Node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = Node('test')
        self.node2 = Node('test2')

    # Test __init__() 
    def test_a_Init(self):
        self.assertEqual(self.node.value, 'test')
        self.assertEqual(self.node2.value, 'test2')

        self.assertIsNone(self.node.next)
        self.node.next = self.node2
        self.assertIsNotNone(self.node.next)
        self.assertEqual(self.node.next.value, 'test2')
        self.assertIsNone(self.node.next.next)

    # Test __init__() -> __str__() 
    def test_b_Str(self):
        self.assertEqual(self.node.__str__(), str(self.node))
        self.assertEqual(self.node2.__str__(), str(self.node2))
