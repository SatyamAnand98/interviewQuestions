import click
import time

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.addr = None


def appendNode():
	if head.addr == None:
		temp = Node(input("Enter the value to be inserted: "))
		head.addr = temp
		global tail 
		tail = temp
		del temp
	else:
		temp = Node(input("Enter the value to be inserted: "))
		tail.next = temp
		tail = temp
		del temp

def display():
	if head.addr == None:
		print("No elements found.")
	else:
		temp = headl
		result = "" + temp.addr.value + " -> "
		temp = temp.addr.next
		while temp != None:
			result += temp.value+" -> "
			temp = temp.next

		print(f"result = {result[:-4]}")
	input("Do you want to continue? ")

def addElementAny():
	position = int(input("Enter the position you want to insert: "))-1
	temp = head
	temp = temp.addr.next
	prev = head
	pos = 1
	while temp != None:
		if pos == position:
			temp2 = Node(input("Enter the value to be inserted"))
			temp2.next = prev.next
			prev.next = temp2
		pos += 1
		prev = temp
		temp = temp.next


if __name__ == '__main__':

	global head
	head = LinkedList()

	choice = 0

	try:

		while id(choice):

			click.clear()

			print("1. append an element into linkedList")
			print("2. add an element into linkedList (anywhere)")
			print("3. add an element into linkedList in the front")
			print("4. pop an element from linkedList")
			print("5. delete an element from linkedList (anywhere)")
			print("6. delete the front element from linkedList")
			print("7. display the elements in linkedList")
			print("8. get the length of linkedList")
			print("9. Exit.\n\n\n\n\n")
			# print("\n"*42)
			
			choice = int(input("Enter your choice: ") or '1')

			if choice >= 9 or choice <=0:
				del choice
			elif choice == 1:
				appendNode()
			elif choice == 7:
				display()
			elif choice == 2:
				addElementAny()

	except NameError:
		click.clear()
		print("\n"*24)
		print('{:^215}'.format("See you soon brother!!"))
		print("\n"*24)
		time.sleep(1)
		click.clear()