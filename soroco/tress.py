class Node:
	def __init__(self, val=None):
		self.data = val
		self.right = None
		self.left = None

def inorder(root):
	if not root:
		return

	inorder(root.left)
	print(root.data, end=" ")
	inorder(root.right)

def postorder(root):
	if not root:
		return

	postorder(root.left)
	postorder(root.right)
	print(root.data, end=" ")

def preorder(root):
	if not root:
		return

	print(root.data, end=" ")
	preorder(root.left)
	preorder(root.right)

def insertBST(root, x):
	if not root:
		return Node(x)
	elif(x < root.data):
		root.left = insertBST(root.left, x)
	elif(x > root.data):
		root.right = insertBST(root.right, x)
	return root


def KMinimumBST(root, k):
	print(root.data)
	print(k)


if __name__ == '__main__':
	li = list(map(int, input("Enter the elements for the tree:\n").split()))
	k = int(input("Enter the k value: "))
	root = None

	for i in li:
		root = insertBST(root, i)

	KMinimumBST(root, k)

	print(f"{'*'*10} INORDER TRAVERSAL {'*'*10}")
	inorder(root)
	print()
	print(f"{'*'*10} POSTORDER TRAVERSAL {'*'*10}")
	postorder(root)
	print()
	print(f"{'*'*10} PREORDER TRAVERSAL {'*'*10}")
	preorder(root)
	print()