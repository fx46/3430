import unittest, os

from app import FilePrinter, LinkedList, Stack, Queue

class FilePrinterTest(unittest.TestCase):

    def setUp(self):
        self.printer = FilePrinter("testFile.txt", "testName")
        self.linkedList = LinkedList()
        self.stack = Stack(1)
        self.queue = Queue(1)

    def tearDown(self):
        try:
            os.remove(self.printer.file_path)
        except IOError:
            pass

    # Test __init__() 
    def test_a_Init(self):
        self.assertEqual(self.printer.file_path, "testFile.txt")
        self.assertEqual(self.printer.name, "testName")

    def test_b_VisitLinkedList(self):
        self.linkedList.append(1)

        self.linkedList.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n(1)\n")

    def test_c_VisitStack(self):
        self.stack.push(1)

        self.stack.accept(self.printer)
        filler="\n-------\n"
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name +filler+'   1   '+filler)

    def test_d_VisitLogQueue(self):
        self.queue.enqueue(1)

        self.queue.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n|1|\n")
