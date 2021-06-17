class Node:
	def __init__(self, val=None):
		self.data = val
		self.left = None
		self.right = None

def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.data,end = " ")
    inorder(temp.right)

def postorder(temp):
	if(not temp):
		return

	postorder(temp.left)
	postorder(temp.right)
	print(temp.data, end=" ")

def insert(temp,data):
	if not temp:
		root = Node(data)
		return root
	q = []
	q.append(temp)

	while (len(q)):
		temp = q[0]
		q.pop(0)

		if (not temp.left):
		    temp.left = Node(data)
		    break
		else:
		    q.append(temp.left)

		if (not temp.right):
		    temp.right = Node(data)
		    break
		else:
		    q.append(temp.right)

def leftView(root):
	if not root:
		return
	print(root.data, end = ' ')
	leftView(root.left)

if __name__ == '__main__':
	li = list(map(int, input().split()))
	root = insert(None, li[0])
	for i in li[1:]:
		insert(root, i)

	print("**************************\tINORDER\t*****************************")
	inorder(root)
	print()
	print("**************************\tPOSTORDER\t*****************************")
	postorder(root)
	print()
	print(f"{'*'*10} LEFT VIEW {'*'*10}")
	leftView(root)
	print()