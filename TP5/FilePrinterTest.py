import unittest, os

from app import FilePrinter, LinkedList, Stack, Queue

class FilePrinterTest(unittest.TestCase):

    def setUp(self):
        self.printer = FilePrinter("testFile.txt", "testName")
        self.linkedList = LinkedList()
        self.stack = Stack(3)
        self.queue = Queue(3)

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
        self.linkedList.append(2)
        self.linkedList.append(3)

        self.linkedList.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n(1,2,3)\n")

    def test_c_VisitStack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.stack.accept(self.printer)
        filler="\n-------\n"
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name +filler+'   3   '+filler+'   2   '+filler+'   1   '+filler)

    def test_d_VisitLogQueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.queue.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n|1|2|3|\n")
