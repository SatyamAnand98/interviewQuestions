# 1) Find if a Linked List of characters is palindromic, 0(n) time and 0(1) space

class Node:
	def __init__(self):
		self.val = None
		self.next = None

def palindrome(head):
	stack = []
	cur = head
	while(cur!=None):
		stack.append(cur.val)
		cur = cur.next
	while(head!=None):
		data = stack.pop()
		if head.val==data:
			pass
		else:
			stack.append(data)
		head = head.next

	return stack==[]
			

def insert(ll,head):
	curr = Node()
	for i in ll:
		temp = Node()
		if head.val==None:
			head.val = i
			curr = head
		elif head.next==None:
			temp.val = i
			head.next = temp
			curr = temp
		else:
			temp.val = i
			curr.next = temp
			curr = temp

	return head

def traversal(head):
	while(head!=None):
		if head.next==None:
			print(f"| {head.val} |", end=" :")
		else:
			print(f"| {head.val} |", end=' ----> ')
		head = head.next

	return ""

if __name__ == '__main__':
	arr = [1,3,2,2]
	head = Node()
	head = insert(arr, head)
	
	if(palindrome(head)):
		print(f"{traversal(head)} is palindrome.")
	else:
		print(f"{traversal(head)} is not palindrome.")