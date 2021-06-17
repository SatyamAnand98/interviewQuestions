'''
Design a Family Tree of parents and children (one child can have many parents and vice versa) and write two functions :-
a.) tillNode() :- prints all the ancestors (parents, grandparents and above) of a particular node.
b.) fromNode() :- prints all the children (children, grandchildren and below) of a particular node.
You can use any data structure of your choice to implement above. Input will be the number of relations in the tree between different nodes (PARENT<space>CHILD).
'''

class Node:
	def __init__(self, name):
		self.name = name
		self.parent = []
		self.child = []

def tillNode(node):
	result = []
	for i in node.parent:
		result += [i.name] + tillNode(i)
	return result

def fromNode(node):
	result = []
	for i in node.child:
		result += [i.name] + fromNode(i)
	return result



if __name__ == '__main__':
	satyam = Node('Satyam Anand')
	swati = Node('Swati Sneha')
	sunita = Node('Sunita Singh')
	harikantSingh = Node('Harikant Singh')
	sarojaniDevi = Node('Sarojani Devi')
	lakhpatiSingh = Node('LakhPati Singh')
	naniMaa = Node('Nani Maa')

	l = [satyam, swati, sunita, harikantSingh, sarojaniDevi, lakhpatiSingh, naniMaa]

	satyam.parent.append(sunita)
	sunita.child.append(satyam)
	
	swati.parent.append(sunita)
	sunita.child.append(swati)

	sunita.parent.append(harikantSingh)
	harikantSingh.child.append(sunita)

	sunita.parent.append(sarojaniDevi)
	sarojaniDevi.child.append(sunita)

	harikantSingh.parent.append(lakhpatiSingh)
	lakhpatiSingh.child.append(harikantSingh)

	sarojaniDevi.parent.append(naniMaa)
	naniMaa.child.append(sarojaniDevi)

	for node in l:
		print("----------------------------"+node.name+"----------------------------")
		print(f"Ancestors: {tillNode(node)}")
		print(f"Children : {fromNode(node)}")
		print('#'*50)
		print()