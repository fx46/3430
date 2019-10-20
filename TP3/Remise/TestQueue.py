import unittest
from Queue import *


class TestQueue(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_whenCreateEmptyQueue_thenNoElement(self):
        queue = Queue()
        self.assertFalse(queue.hasOne())
        self.assertTrue(queue.isEmpty())
        self.assertFalse(queue.isFull())

    def test_whenCheckTheFirstElmentWithEmptyQueueEnqueueAndDequeue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        try:
            queue.check_first()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

        queue.enqeue(2019)
        self.assertFalse(queue.isEmpty())
        queue.dequeue()
        self.assertTrue(queue.isEmpty())

    def test_whenCheckTheFirstElmentWithEmptyQueueDequeueAndEnequeue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        try:
            queue.check_first()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

        try:
            queue.dequeue()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

        queue.enqeue(2019)
        self.assertFalse(queue.isEmpty())


    def test_whenCheckTheLastElmentWithEmptyQueue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        try:
            queue.check_last()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")


    def test_whenDequeOnEmptyQueue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        try:
            queue.dequeue()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

    def test_whenLastIsCheckedwithOneElement_thenRaisesValueError(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        queue.enqeue(2019)
        self.assertFalse(queue.isEmpty())
        self.assertTrue(queue.hasOne())

        try:
            queue.check_last()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue has only one element (the first one)")



    def test_whenEnqueueMoreThanMaxEnqeueAndDeqeueAndEnqeue_thenRaisesValueErrorQueueOverflowAndDequeueAndEnqeue(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        for k in range(0, queue.MAX):
            queue.enqeue(k)

        self.assertFalse(queue.isEmpty())
        self.assertTrue(queue.isFull())

        try:
            queue.enqeue(2019)
        except Exception as ex:
            self.assertEqual(str(ex), "Queue overflow")

        queue.dequeue()
        self.assertFalse(queue.isFull())
        queue.enqeue(1019)




    def test_whenEnqeueToMax_thenDoesNotRaiseException(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())

        for k in range(0, queue.MAX):
            self.assertFalse(queue.isFull())
            queue.enqeue(k)
            self.assertEqual(queue.size(), k+1)
            self.assertEqual(str(queue.check_first()), str(0))
            if (queue.size() > 1):
                self.assertEqual(str(queue.check_last()), str(k))

        self.assertTrue(queue.isFull())




if __name__ == '__main__':
	unittest.main()
