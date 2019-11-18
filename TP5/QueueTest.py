import unittest

from app import Queue

class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(3)

    # Test __init__() 
    def testInit(self):
        self.assertEqual(self.queue.max_size, 3)

    # Test __init__() -> Enqueue() -> Dequeue()
    def testEnqueuDequeue(self):
        self.queue.enqueue("test")
        self.assertFalse(self.queue.isEmpty())
        self.assertTrue(self.queue.size() == 1)
        self.assertEqual(self.queue.check().value, "test")
        self.assertEqual(self.queue.peek().value, "test")
        self.assertTrue(self.queue.isEmpty())

        self.queue.enqueue("test1")
        self.queue.enqueue("test2")
        self.queue.enqueue("test3")
        self.assertTrue(self.queue.isFull())
        self.assertEqual(self.queue.size(), self.queue.max_size)
        try:
            self.queue.enqueue("test4")
        except Exception as ex:
            self.assertEqual(str(ex), "Queue overflow")
            
        self.assertEqual(self.queue.dequeue().value, "test1")
        self.assertEqual(self.queue.dequeue().value, "test2")
        self.assertEqual(self.queue.dequeue().value, "test3")
        try:
            self.queue.dequeue()
        except Exception as ex:
            self.assertEqual(str(ex), "Stack underflow")
