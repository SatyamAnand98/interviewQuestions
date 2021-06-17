'''
Design a Family Tree of parents and children (one child can have many parents and vice versa) and write two functions :-
a.) tillNode() :- prints all the ancestors (parents, grandparents and above) of a particular node.
b.) fromNode() :- prints all the children (children, grandchildren and below) of a particular node.
You can use any data structure of your choice to implement above. Input will be the number of relations in the tree between different nodes (PARENT<space>CHILD).
'''

class Node:
	def __init__(self, name=None, children=None, ancestors=None):
		self.mem_name = name
		self.children = children
		self.ancestors = ancestors

def tillNode(family, person):
	

def fromNode(family, person):
	pass

if __name__ == '__main__':
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