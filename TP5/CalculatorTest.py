import unittest

from app import LinkedList, Queue, Stack, Calculator

class CalculatorTest(unittest.TestCase):

    def testUnionLinkedList(self):
        # If list1 is bigger
        list1 = LinkedList()
        list2 = LinkedList()
        numbers = [1,2,3,4,5]
        numbersList1 = [1,2,3]
        numbersList2 = [4,5]

        for i in numbersList1:
            list1.append(i)

        for i in numbersList2:
            list2.append(i)

        UnitedList = Calculator.union(list1, list2)
        numbersContained = 0
        for i in numbersList1 + numbersList2:
            number = UnitedList.peek().value
            if number in numbersList1 + numbersList2:
                numbersContained += 1
                numbers.remove(number)
        self.assertEqual(numbersContained, len(numbersList1 + numbersList2))

        # If list2 is bigger
        list1 = LinkedList()
        list2 = LinkedList()
        numbers = [1,2,3,4,5]
        numbersList1 = [1,2]
        numbersList2 = [3,4,5]

        for i in numbersList1:
            list1.append(i)

        for i in numbersList2:
            list2.append(i)

        UnitedList = Calculator.union(list1, list2)
        numbersContained = 0
        for i in numbersList1 + numbersList2:
            number = UnitedList.peek().value
            if number in numbersList1 + numbersList2:
                numbersContained += 1
                numbers.remove(number)
        self.assertEqual(numbersContained, len(numbersList1 + numbersList2))

        # If lists are the same size
        list1 = LinkedList()
        list2 = LinkedList()
        numbers = [1,2,3,4]
        numbersList1 = [1,2]
        numbersList2 = [3,4]

        for i in numbersList1:
            list1.append(i)

        for i in numbersList2:
            list2.append(i)

        UnitedList = Calculator.union(list1, list2)
        numbersContained = 0
        for i in numbersList1 + numbersList2:
            number = UnitedList.peek().value
            if number in numbersList1 + numbersList2:
                numbersContained += 1
                numbers.remove(number)
        self.assertEqual(numbersContained, len(numbersList1 + numbersList2))



    def testUnionQueue(self):
        queue1 = Queue(3)
        queue2 = Queue(3)

        numbers = [1,2,3,4,5,6]
        numbersqueue1 = [1,2,3]
        numbersqueue2 = [4,5,6]

        for i in numbersqueue1:
            queue1.enqueue(i)

        for i in numbersqueue2:
            queue2.enqueue(i)

        unitedStack = Calculator.union(queue1, queue2)

        numbersContained = 0
        for i in numbers:
            number = unitedStack.dequeue().value
            if number in numbers:
                numbersContained += 1
                numbers.remove(number)

        self.assertEqual(numbersContained, len(numbers))
        self.assertEqual(unitedStack.max_size, queue1.max_size + queue2.max_size)

    def testUnionStack(self):
        stack1 = Stack(3)
        stack2 = Stack(3)

        numbers = [1,2,3,4,5,6]
        numbersstack1 = [1,2,3]
        numbersstack2 = [4,5,6]

        for i in numbersstack1:
            stack1.push(i)

        for i in numbersstack2:
            stack2.push(i)

        unitedStack = Calculator.union(stack1, stack2)

        numbersContained = 0
        for i in numbers:
            number = unitedStack.pop().value
            if number in numbers:
                numbersContained += 1
                numbers.remove(number)

        self.assertEqual(numbersContained, len(numbers))
        self.assertEqual(unitedStack.max_size, stack1.max_size + stack2.max_size)

    def testUnionDifferentTypes(self):
        self.assertRaises(ValueError, Calculator.union, Stack(3), 3)