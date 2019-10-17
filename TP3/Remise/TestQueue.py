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

    def test_whenCheckTheFirstElmentWithEmptyQueue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        try:
            queue.check_first()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

    def test_whenCheckTheLastElmentWithEmptyQueue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        try:
            queue.check_last()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

    def test_whenDequeOnEmptyQueue_thenRaisesValueErrorQueueUnderFlow(self):
        queue = Queue()
        try:
            queue.dequeue()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue underflow")

    def test_whenLastIsCheckedwithOneElement_thenRaisesValueError(self):
        queue = Queue()
        queue.enqeue(2019)
        self.assertTrue(queue.hasOne())
        try:
            queue.check_last()
        except Exception as ex:
            self.assertEqual(str(ex), "Queue has only one element (the first one)")


    def test_whenEnqueueMoreThanMax_thenRaisesValueErrorQueueOverflow(self):

        queue = Queue()
        for k in range(0, queue.MAX):
            queue.enqeue(k)

        try:
            queue.enqeue(2019)
        except Exception as ex:
            self.assertEqual(str(ex), "Queue overflow")



    def test_whenEnqeueToMax_thenDoesNotRaiseException(self):
        queue = Queue()

        for k in range(0, queue.MAX):
            self.assertFalse(queue.isFull())
            queue.enqeue(k)
            self.assertEqual(queue.size(), k+1)
            self.assertEqual(str(queue.check_first()), str(0))
            if (queue.size() > 1):
                self.assertEqual(str(queue.check_last()), str(k))

        self.assertTrue(queue.isFull())


    # def test_whenValidBasicOperation_thenDoesNotRaiseException(self):
    #     queue = Queue()
    #
    #     for k in range(0, queue.MAX):
    #         queue.enqeue(k)
    #
    #     expected_size = queue.size()
    #
    #     self.assertEqual(str(queue.check_first()), str(0))
    #     self.assertEqual(str(queue.check_last()), str(99))
    #     self.assertTrue(queue.isFull())
    #     self.assertEqual(queue.MAX, expected_size)
    #
    #     self.assertEqual(str(queue.dequeue()), str(0))
    #     self.assertFalse(queue.isFull())
    #     expected_size = expected_size - 1
    #     self.assertEqual(queue.MAX-1, expected_size)
    #
    #     for k in range(1, queue.MAX-1):
    #         self.assertEqual(str(queue.check_last()), str(99))
    #         self.assertEqual(str(queue.check_first()), str(k))
    #         self.assertEqual(str(queue.dequeue()), str(k))
    #         self.assertFalse(queue.isFull())
    #
    #         tailleAttendue = tailleAttendue - 1
    #         self.assertEqual(queue.size(), tailleAttendue)
    #
    #     #tests pour le dernier element
    #     self.assertEqual(queue.size(),1)
    #     self.assertTrue(queue.hasOne)
    #     self.assertRaises(ValueError, queue.check_last)
    #
    #     self.assertEqual(str(queue.check_first()), str(99))
    #     self.assertEqual(str(queue.dequeue()), str(99))
    #
    #     self.assertEqual(queue.size(),0)
    #     self.assertTrue(queue.hasOne)
    #     self.assertRaises(ValueError, queue.check_first)
    #     self.assertRaises(ValueError, queue.check_last)


if __name__ == '__main__':
	unittest.main()
