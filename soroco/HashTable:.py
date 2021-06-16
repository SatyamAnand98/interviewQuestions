class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for _ in range(self.MAX)]
		self.len = 0

	def getHash(self, key):
		sum = 0
		for i in key:
			sum += ord(i)
		return sum%self.MAX

	def __setitem__(self, key, val):
		index = self.getHash(key)
		found = False
		if self.len<=self.MAX:
			for idx, element in enumerate(self.arr[index]):
				if len(element)==2 and element[0]==key:
					self.arr[index][idx] = (key, val)
					found = True
					break
			if not found:
				self.arr[index].append((key, val))
		self.len += self.len

	def __getitem__(self, key):
		index = self.getHash(key)
		for element in self.arr[index]:
			if element[0]==key:
				return element[1]

	def __delitem__(self, key):
		index = self.getHash(key)
		for element in self.arr[index]:
			if element[0]==key:
				self.arr[index].remove(element)
		self.len -= self.len


if __name__ == '__main__':
	obj = HashTable()

	
	obj['satyam'] = 24
	obj['swati'] = 27
	obj['sunita'] = 51
	obj['sarojani'] = 70

	print(f"age of satyam = {obj['satyam']}")
	print(f"age of swati = {obj['swati']}")
	print(f"age of sunita = {obj['sunita']}")
	print(f"age of sarojani = {obj['sarojani']}")
	
	print()

	del obj['satyam']

	print(f"age of satyam = {obj['satyam']}")
	print(f"age of swati = {obj['swati']}")
	print(f"age of sunita = {obj['sunita']}")
	print(f"age of sarojani = {obj['sarojani']}")