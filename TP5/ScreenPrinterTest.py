import unittest
import io
import sys

from app import LinkedList, Stack, Queue, ScreenPrinter

class ScreenPrinterTest(unittest.TestCase):

    def setUp(self):
        self.screenPrinter = ScreenPrinter("test")
        self.linkedList = LinkedList()
        self.stack = Stack(3)
        self.queue = Queue(3)

    # Test __init__() 
    def testInit(self):
        self.assertEqual(self.screenPrinter.name, "test")

    def testVisitLinkedList(self):
        self.linkedList.append(1)
        self.linkedList.append(2)
        self.linkedList.append(3)

        sys.stdout = io.StringIO() 
        self.linkedList.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n(1,2,3)\n\n")
        sys.stdout = sys.__stdout__

    def testVisitStack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        sys.stdout = io.StringIO() 
        self.stack.accept(ScreenPrinter(""))
        filler="\n-------\n"
        expected = '\n'+filler+'   3   '+filler+'   2   '+filler+'   1   '+filler+'\n'
        self.assertEqual(sys.stdout.getvalue(), expected)
        sys.stdout = sys.__stdout__

    def testVisitLogQueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        sys.stdout = io.StringIO() 
        self.queue.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n|1|2|3|\n\n")
        sys.stdout = sys.__stdout__        
