'''
Design a Family Tree of parents and children (one child can have many parents and vice versa) and write two functions :-
a.) tillNode() :- prints all the ancestors (parents, grandparents and above) of a particular node.
b.) fromNode() :- prints all the children (children, grandchildren and below) of a particular node.
You can use any data structure of your choice to implement above. Input will be the number of relations in the tree between different nodes (PARENT<space>CHILD).
'''

class Node:
	def __init__(self, name=None, children=None, ancestors=None):
		self.name = name
		self.children = children
		self.ancestors = ancestors

def tillNode(family, person):
	result = []
	for i in family:
		if (i.name==person):
			if i.ancestors==None:
				return []
			else:
				for j in i.ancestors:
					result += i.ancestors + tillNode(family, j)
	return list(set(result))
	

def fromNode(family, person):
	result = []
	for i in family:
		if (i.name==person):
			if i.children==None:
				return []
			else:
				for j in i.children:
					result += i.children + fromNode(family, j)
	return list(set(result))

if __name__ == '__main__':
	family = [
		Node('Harikant Singh', ['Sunita Singh', 'Madhavi Sinha', 'Niraj Kumar', 'Pankaj Kumar'], ['LakhPati Singh', 'w/o Lakhpati Singh']),
		Node('Sarojani Devi', ['Sunita Singh', 'Madhavi Sinha', 'Niraj Kumar', 'Pankaj Kumar'], ['Nani maa']),
		Node('Sunita Singh', ['Satyam Anand', 'Swati Sneha'], ['Sarojani Devi', 'Harikant Singh']),
		Node('Madhavi Sinha', ['Digvijay Narayan Shahi', 'Raghavendra Narayan Shahi'], ['Sarojani Devi', 'Harikant Singh']),
		Node('Pankaj Kumar', ['Shashank Shekhar', 'Khushboo Kumari'], ['Sarojani Devi', 'Harikant Singh']),
		Node('Niraj Kumar', ['Rajasvi Singh', 'Mimansa Singh'], ['Sarojani Devi', 'Harikant Singh']),
		Node('Swati Sneha', None, ['Sunita Singh']),
		Node('Satyam Anand', None, ['Sunita Singh']),
		Node('Digvijay Narayan Shahi', ['Sharabh Shahi'], ['Madhavi Sinha']),
		Node('Raghavendra Narayan Shahi', None, ['Madhavi Sinha']),
		Node('Shashank Shekhar', None, ['Pankaj Kumar']),
		Node('Khushboo Kumari', None, ['Pankaj Kumar']),
		Node('Rajasvi Singh', None, ['Niraj Kumar']),
		Node('Mimansa Singh', None, ['Niraj Kumar']),
		Node('Sharabh Shahi', None, ['Digvijay Narayan Shahi']),
		Node('Ankita Mishra', ['Sharabh Shahi'], None),
		Node('Neetu Singh', ['Rajasvi Singh', 'Mimansa Singh'], None),
		Node('Heera Devi', ['Shashank Shekhar', 'Khushboo Kumari'], None),
		Node('Ajay Prasad', ['Digvijay Narayan Shahi', 'Raghavendra Narayan Shahi'], None)
	]

	for i in family:
		person = i.name
		print(person)
		print("\tancestor ", end=": ")
		print(tillNode(family, person))
		print("\tchildren ", end=": ")
		print(fromNode(family, person))
		print('#'*50, end='\n\n')

	'''
	family = {
		nanaJi : Node('Harikant Singh', ['Sunita Singh', 'Madhavi Sinha', 'Niraj Kumar', 'Pankaj Kumar'], ['LakhPati Singh', 'w/o Lakhpati Singh']),
		sarojaniDevi : Node('Sarojani Devi', ['Sunita Singh', 'Madhavi Sinha', 'Niraj Kumar', 'Pankaj Kumar'], ['Nani maa']),
		sunitaSingh : Node('Sunita Singh', ['Satyam Anand', 'Swati Sneha'], ['Sarojani Devi', 'Harikant Singh']),
		madhaviSinha : Node('Madhavi Sinha', ['Digvijay Narayan Shahi', 'Raghavendra Narayan Shahi'], ['Sarojani Devi', 'Harikant Singh']),
		pankajKumar : Node('Pankaj Kumar', ['Shashank Shekhar', 'Khushboo Kumari'], ['Sarojani Devi', 'Harikant Singh']),
		nirajKumar : Node('Niraj Kumar', ['Rajasvi Singh', 'Mimansa Singh'], ['Sarojani Devi', 'Harikant Singh']),
		swatiSneha : Node('Swati Sneha', None, ['Sunita Singh']),
		satyamAnand : Node('Satyam Anand', None, ['Sunita Singh']),
		digvijay : Node('Digvijay Narayan Shahi', ['Sharabh Shahi'], ['Madhavi Sinha']),
		raghavendra : Node('Raghavendra Narayan Shahi', None, ['Madhavi Sinha']),
		shashank : Node('Shashank Shekhar', None, ['Pankaj Kumar']),
		khusboo : Node('Khushboo Kumari', None, ['Pankaj Kumar']),
		rajasvi : Node('Rajasvi Singh', None, ['Niraj Kumar']),
		mimansa : Node('Mimansa Singh', None, ['Niraj Kumar']),
		sharabh : Node('Sharabh Shahi', None, ['Digvijay Narayan Shahi']),
		ankita : Node('Ankita Mishra', ['Sharabh Shahi'], None),
		neetuSingh : Node('Neetu Singh', ['Rajasvi Singh', 'Mimansa Singh'], None),
		heeraDevi : Node('Heera Devi', ['Shashank Shekhar', 'Khushboo Kumari'], None),
		ajayPrasad : Node('Ajay Prasad', ['Digvijay Narayan Shahi', 'Raghavendra Narayan Shahi'], None)
	}
	'''