import unittest, io, sys

from app import LinkedList, Stack, Queue, ScreenPrinter

class ScreenPrinterTest(unittest.TestCase):

    def setUp(self):
        self.screenPrinter = ScreenPrinter("test")
        self.linkedList = LinkedList()
        self.stack = Stack(1)
        self.queue = Queue(1)

    # Test __init__() 
    def test_a_Init(self):
        self.assertEqual(self.screenPrinter.name, "test")

    def test_b_VisitLinkedList(self):
        self.linkedList.append(1)

        sys.stdout = io.StringIO() 
        self.linkedList.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n(1)\n\n")
        sys.stdout = sys.__stdout__

    def test_c_VisitStack(self):
        self.stack.push(1)

        sys.stdout = io.StringIO() 
        self.stack.accept(ScreenPrinter(""))
        filler="\n-------\n"
        self.assertEqual(sys.stdout.getvalue(), '\n'+filler+'   1   '+filler+'\n')
        sys.stdout = sys.__stdout__

    def test_d_VisitLogQueue(self):
        self.queue.enqueue(1)

        sys.stdout = io.StringIO() 
        self.queue.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n|1|\n\n")
        sys.stdout = sys.__stdout__        
