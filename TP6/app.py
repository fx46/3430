import random as rand
import abc

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None # the pointer initially points to nothing

	def __str__(self):
		return str(self.value)

class LinkedList :
	# Initializes an empty linked list.
	def __init__(self):
		self.list = []

	# Returns true if this linked list is empty.
	def isEmpty(self):
		return len(self.list) == 0

	# Returns the number of items in this linked list.
	def size(self):
		return len(self.list)

	# Returns the first item added to this linked list
	def check(self):
		if self.isEmpty():
			raise ValueError("linked list underflow")
		return self.list[0]

	#Removes and returns the first item in the linked list
	def peek(self):
		if self.isEmpty():
			raise ValueError("linked list underflow")
		return self.list.pop(0)

	def append(self, item):
		self.list.append(Node(item))

	def prepend(self, item):
		self.list.insert(0, Node(item))

	def accept(self, visitor):
		visitor.visit(self)

class Queue(LinkedList):

	# Initializes an empty queue.
	def __init__(self, max_size,  *args, **kwargs):
		self.max_size = max_size
		super(Queue, self).__init__(*args, **kwargs)

	def isFull(self):
		return len(self.list) == self.max_size

	# Adds the item to this queue.
	def enqueue(self, item):
		if self.isFull():
			raise ValueError("Queue overflow")
		self.append(item)

	#Removes and returns the item on this queue that was least recently added.
	def dequeue(self):
		try:
			return self.peek()
		except ValueError:
			raise ValueError("Stack underflow")

class Stack(LinkedList):
	# Initializes an empty stack.
	def __init__(self, max_size, *args, **kwargs):
		self.max_size = max_size
		super(Stack, self).__init__(*args, **kwargs)

	# Returns true if this stack is full.
	def isFull(self):
		return len(self.list) == self.max_size

	# Adds the item to this stack.
	def push(self, item):
		if self.isFull():
			raise ValueError("Stack overflow")
		self.prepend(item)

	# Removes and returns the item most recently added to this stack.
	def pop(self):
		try:
			return self.peek()
		except ValueError:
			raise ValueError("Stack underflow")

class AutoAdaptiveStack(Stack):

	def __init__(self, max_trials, size_increment, queueSize, *args, **kwargs):
		self.max_trials = max_trials
		self.size_increment = size_increment
		self.trials = 0
		self.queueSize = queueSize
		self.queue = Queue(queueSize)
		super(AutoAdaptiveStack, self).__init__(*args, **kwargs)

	def push(self, item):
		try:
			super(AutoAdaptiveStack, self).push(item)
		except:
			print("There is no free space actually :( adding item to queue")
			try:
				self.queue.enqueue(item)
			except:
				print("There is no free space in the queue either D: ")
				self.trials += 1
				if self.trials == self.max_trials:
					self.max_size += self.size_increment
					self.trials = 0

	def pop(self):
		item = None
		try:
			item =  self.peek()
		except ValueError:
			print("Stack underflow")

		if not self.queue.isEmpty():
			self.push(self.queue.dequeue())

		return item

class AutoAdaptiveQueue(Queue):

	def __init__(self, max_trials, size_increment, queueSize, *args, **kwargs):
		self.max_trials = max_trials
		self.size_increment = size_increment
		self.trials = 0
		self.queueSize = queueSize
		self.queue = Queue(queueSize)
		super(AutoAdaptiveQueue, self).__init__(*args, **kwargs)

	def enqueue(self, item):
		try:
			super(AutoAdaptiveQueue, self).enqueue(item)
		except ValueError:
			print("There is no free space actually :( adding item to queue")
			try:
				self.queue.enqueue(item)
			except:
				print("There is no free space in the queue either D: ")
				self.trials += 1
				if self.trials == self.max_trials:
					self.max_size += self.size_increment
					self.trials = 0
	
	def dequeue(self):
		item = None
		try:
			item = self.peek()
		except ValueError:
			print("Stack underflow")

		if not self.queue.isEmpty():
			self.enqueue(self.queue.dequeue())

		return item

class Printer(object, metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name

	def visit(self, list_obj):
		if isinstance(list_obj, Stack):
			display_message = "\n-------\n"
			node = list_obj.list[0]
			while node:
				display_message += '   '+str(node.value)+'   '
				display_message += "\n-------\n"
				node = node.next
		elif isinstance(list_obj, Queue):
			display_message = "\n|"
			node = list_obj.list[0]
			while node:
				display_message += str(node.value) + "|"
				node = node.next
			display_message += "\n"
		else:
			display_message = "\n("
			node = list_obj.list[0]
			while node.next:
				display_message += str(node.value) + ","
				node = node.next
			display_message += str(node.value) + ")\n"
		self.log(display_message)

	@abc.abstractmethod
	def log(self, display_message):
		raise NotImplementedError('child objects must define log to create a printer')

class ScreenPrinter(Printer):
	def __init__(self, *args, **kwargs):
		super(ScreenPrinter, self).__init__(*args, **kwargs)

	def log(self, display_message):
		print(self.name)
		print(display_message)

class FilePrinter(Printer):
	def __init__(self, file_path, *args, **kwargs):
		self.file_path = file_path
		super(FilePrinter, self).__init__(*args, **kwargs)

	def log(self, display_message):
		with open(self.file_path, 'a') as f:
			f.write(self.name)
			f.write(display_message)

class Calculator:

	@staticmethod
	def union(first_list, second_list):
		if isinstance(first_list,Queue) and isinstance(second_list,Queue):
			merged_queue = Queue(max_size=first_list.max_size+second_list.max_size)
			for item in second_list.list:
				first_list.append(item)
			merged_queue.list = first_list.list
			return merged_queue
		elif isinstance(first_list,Stack) and isinstance(second_list,Stack):
			merged_stack = Stack(max_size=first_list.max_size+second_list.max_size)
			for item in second_list.list:
				first_list.append(item)
			merged_stack.list = first_list.list
			return merged_stack
		elif isinstance(first_list,LinkedList) and isinstance(second_list,LinkedList):
			merged_list = LinkedList()
			for item in second_list.list:
				first_list.append(item)
			merged_list.list = first_list.list
			return merged_list
		else:
			raise ValueError('The types of both lists are different')
