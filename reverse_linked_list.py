class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		curr = self.head
		pointer_string = " -> "
		ll_string = ""
		while curr:
			val = curr.value
			ll_string += str(val) + pointer_string
			curr = curr.next
		print(ll_string)

def reverse_linked_list(ll):
	# given an input linked list 1 -> 2 -> 3
	# reverse the linked list in place 3 -> 2 -> 1
	prev = None
	curr = ll.head
	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	ll.head = prev

# generate a test linked list 1 -> 2 -> 3 -> 4 -> 5
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

test_linked_list = LinkedList()
test_linked_list.head = a

test_linked_list.print_list()
reverse_linked_list(test_linked_list)
test_linked_list.print_list()