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

# def tillNode(node):
# 	result = []
# 	for i in node.parent:
# 		result += [i.name] + tillNode(i)
# 	return result

# def fromNode(node):
# 	result = []
# 	for i in node.child:
# 		result += [i.name] + fromNode(i)
# 	return result


class FamilyTree:
	def __init__(self):
		self.family = {}

	def addRelation(self, parent, child):
		if parent not in self.family.keys():
			self.family[parent] = Node(parent)

		if child not in self.family.keys():
			self.family[child] = Node(child)

		parentNode = self.family[parent]
		childNode = self.family[child]

		parentNode.child.append(childNode)
		childNode.parent.append(parentNode)

	def tillNode(self, person):
		result = []
		for i in self.family[person].parent:
			result += [i.name] + self.tillNode(i.name)
		return result

	def fromNode(self, person):
		result = []
		for i in self.family[person].child:
			result += [i.name] + self.fromNode(i.name)
		return result


if __name__=='__main__':
	familyTree = FamilyTree()
	familyTree.addRelation("Sunita Singh", "Satyam Anand");
	familyTree.addRelation("Sunita Singh", "Swati Sneha");

	familyTree.addRelation("Harikant Singh", "Sunita Singh");
	familyTree.addRelation("Sarojani Devi", "Sunita Singh");

	familyTree.addRelation("Lakhpati Singh", "Harikant Singh");
	familyTree.addRelation("Nani Maa", "Sarojani Devi");

	familyTree.addRelation("Harikant Singh", "Madhavi Sinha");
	familyTree.addRelation("Sarojani Devi", "Madhavi Sinha");

	print(familyTree.fromNode("Harikant Singh"))
	print(familyTree.tillNode("Sunita Singh"))