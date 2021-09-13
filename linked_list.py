class Node:
	"""
	An object for storing a single node of a linked list.
	Models two attributes - data and the link to the next node in the list.
	"""

	data = None
	next_node = None

	def __init__(self, data):
		self.data = data


	def __repr__(self):
		return "<Node data: %s>" % self.data

class LinkedList:
	head = None
	"""
	Singly linked list
	"""

	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def size(self):
		"""
		Returns the number of nodes in the list.
		Takes O(n) time. (linear time)
		"""
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.next_node
		return count

	def add(self, data):
		"""
		Add a new Node containing at the Head of the list.
		This is a O(1) operation. (constant time)
		"""
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node

	def __repr__(self):
		"""
		Returns a string representation of the list.
		Takes O(n) time. (linear time)
		"""

		nodes = []
		current = self.head
		
		while current:
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)
			else:
				nodes.append("[%s]" % current.data)
				
			current = current.next_node
		return " -> ".join(nodes)


