import unittest
import unittest.mock
import os
from Stack import *

class TestQueue(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

		
	def test_whenPopAndPeekWithEmptyStack_thenRaisesError(self):
		stack = Stack(1, 2, 3)

		#Initial State
		self.assertTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)				
		self.assertEqual(str(stack),"|")

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
	
	
	
	    
	def test_whenPushOnEmptyStackAndPop_thenChangeStateStateFromVideAndComeBack(self):
		stack = Stack(4,5,6)

		#Initial State
		self.assertTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)				
		self.assertEqual(str(stack),"|")

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")


        #Change the state from "Vide" to "Partiellement plein"
		stack.push(Node("LOG3430"))
		
        #Test "Partiellement plein" State
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 1)
		self.assertEqual(stack.peek(), "LOG3430")
		self.assertEqual(str(stack),"|LOG3430|")

		#Change the state from "Partiellement plein" to "Vide"
		self.assertEqual(stack.pop(),"LOG3430")

        #Check "Vide" State
		self.assertTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)				
		self.assertEqual(str(stack),"|")

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
			
			
			
	def test_whenEmptyStacktoFullAndBackToEmpty_thenGetsFullAndGetsEmpty(self):
		stack = Stack(2,1,1)

       
		#Initial State
		self.assertTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)				
		self.assertEqual(str(stack),"|")

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
			
		#Change the state from "Vide" to "Partiellement plein"
		stack.push(Node("LOG3430"))
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 1)
		self.assertEqual(str(stack.peek()), "LOG3430")
		self.assertEqual(str(stack),"|LOG3430|")
		
		#Change the state from "Partiellement plein" to "Plein"
		stack.push(Node("TP4"))
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 2)
		self.assertEqual(str(stack.peek()), "TP4")
		self.assertEqual(str(stack),"|LOG3430|TP4|")
		
		#Test "Plein" State
		self.assertFalse(stack.isEmpty())
		self.assertTrue(stack.isFull())
		self.assertEqual(stack.size(), stack.max_size)
		
		#Change the state from "Plein" to "Partiellement plein"
		node = stack.pop()
		self.assertEqual(str(node), "TP4")
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 1)
		self.assertEqual(stack.peek(), "LOG3430")
		self.assertEqual(str(stack),"|LOG3430|")
		
		
		#Change the state from "Partiellement plein" to "Vide"
		node = stack.pop()
		self.assertEqual(str(node), "LOG3430")
		self.asserTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
	
	
	def test_whenEmptyStacktoFullAndPush_thenIncrement(self):
		max_size = randint(3,5)
		size_increment = randint(2,3)
		stack = Stack(max_size,1,size_increment)

       
		#Initial State
		self.assertTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)				
		self.assertEqual(str(stack),"|")

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		for i in range(1, max_size-1):	
			#Change the state from "Vide" to "Partiellement plein"
			stack.push(Node("LOG3430"))
			self.assertFalse(stack.isEmpty())
			self.assertFalse(stack.isFull())
			self.assertEqual(stack.size(), 1)
			self.assertEqual(str(stack.peek()), "LOG3430")
		
		
		#Change the state from "Partiellement plein" to "Plein"
		stack.push(Node("TP4"))
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 2)
		self.assertEqual(str(stack.peek()), "TP4")
		self.assertEqual(str(stack),"|LOG3430" * max_size + "|TP4")
		
		#Test "Plein" State
		self.assertFalse(stack.isEmpty())
		self.assertTrue(stack.isFull())
		self.assertEqual(stack.size(), stack.max_size)
		
		#Change the state from "Plein" to "Partiellement plein"
		node = stack.pop()
		self.assertEqual(str(node), "TP4")
		self.assertFalse(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 1)
		self.assertEqual(stack.peek(), "LOG3430")
		self.assertEqual(str(stack),"|LOG3430|")
		
		
		#Change the state from "Partiellement plein" to "Vide"
		node = stack.pop()
		self.assertEqual(str(node), "LOG3430")
		self.asserTrue(stack.isEmpty())
		self.assertFalse(stack.isFull())
		self.assertEqual(stack.size(), 0)

		try:
			stack.peek()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
		try:
			stack.pop()
		except Exception as ex:
			self.assertEqual(str(ex), "Stack underflow")
		
	