class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_tree(root, space =0, t=0):
	COUNT = 3

	if root is None:
		return
	
	space += COUNT

	print_tree(root.right, space, 1)

	for x in range(COUNT, space):
		print(" ", end = " ")

	if t ==1: # Right Node
		print(" / ", root.data)
	elif t == 2: #Left Node
		print(" \ " , root.data)
	else:
		print(root.data)

	print_tree(root.left, space, 2)
		

first = Node(1)
first.left = Node(2)
first.right = Node(3)
first.left.left = Node(4)
first.left.right = Node(5)
first.right.left = Node(6)
first.right.right = Node(7)

print_tree(first)