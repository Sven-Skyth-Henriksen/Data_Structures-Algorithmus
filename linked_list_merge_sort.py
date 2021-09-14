from linked_list import LinkedList

def merge_sort(LinkedList):
	"""
	Sorts a linked list in asceeding order
	- Recursivly divide the linked list into sublists containing a single node
	- Repeatedly merge the sublists tp produce sorted sublists until one remains

	Returns a sorted linked list
	"""
	if linked_list.size() == 1:
		return linked_list
	elif linked_list.head is None:
		return linked_list
	
	left_half, right_half = split(linked_list)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)

def split(linked_list):
	"""
	Divide the unsorted list at midpoint into sublist
	"""

	if linked_list.head is None or linked_list is None:
		left_half = linked_list
		right_half = linked_list

		return left_half, right_half
	else:
		size = linked_list.size()
		midpoint = size // 2

		midpoint_node = linked_list.node_at_index(midpoint -1)

		left_half = linked_list
		right_half = LinkedList()
		right_half.head  = midpoint_node.next_node
		midpoint_node.next_node = None

		return left_half, right_half

def merge(left, right):
	"""
	Merges two linked lists, sorting by data in nodes
	Returns a new, merged list
	"""

	# Cretae a new linked list taht contains nodes from merging left and right
	merged = LinkedList()

	# Add a fake head that is discarded later
	merged.add(0)

	# Set current to tze head of the linked list
	current = merged.head

	#Obtain head nodes from left and right
	left_head = left.head
	right_head = right.head

	#Iterate over left and right until we reach the tail node of either
	while left_head or right_head:
		#If the head node of left is None, pass the tail
		#Add the node from right to merged linked list
		if left_head is None:
			current.next_node = right_head
			# Call next on right to set loop condition to False
			right_head = right_head.next_node
			# If the head node of right is None, pass the tail
			# Add the tail not from left to merged linked list
		elif right_head is None:
			current.next_node = left_head
			# Call next on left to set loop condition to False
			left_head = left_head.next_node
		else:
			#Not at either tail node 
			# Obtain node data to perform comparison operations 
			left_data = left_head.data
			right_data = right_head.data
			# If data on left is less than right, set current to left node
		if left_data < right_data:
			current.next_node = left_head
			# Move left head to next node
			left_head = left_head.next_node
			# If data on right is less than left, set current to right node
		else:
			current.next_node = right_head 
			# move right head to next node
			right_head = right_head.next_node
		#Move current to next node
		current = current.next_node

	#Dicsard fake head and set first ,erged node as head 
	head = merged.head.next_node
	merged.head = head 

	return merged 	
