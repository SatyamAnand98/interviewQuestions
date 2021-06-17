def ancestors(genealogy, person):
	if person in genealogy:
		parents = genealogy[person]
		result = parents
		for parent in parents:
			result = result + ancestors(genealogy, parent)
		return result
	return []

def children(genealogy, person):
	status = 0
	result = []
	for i in genealogy.keys():
		if person in genealogy[i]:
			status = 1

	if status == 0:
		return []

	for i in genealogy.keys():
		if person in genealogy[i]:
			result += children(genealogy, i) + [i]

	return result


if __name__ == '__main__':
	genealogy = {
		'Satyam Anand': ['Sunita Singh'],
		'Swati Sneha': ['Sunita Singh'],
		'Sunita Singh': ['Sarojani Devi', 'Harikant Singh'],
		'Harikant Singh': ['LakhPati Singh'],
		'Sarojani Devi': ['Nani Maa'],
		'Madhavi Sinha': ['Sarojani Devi', 'Harikant Singh']
	}

	for i in range(len(genealogy)):
		print(list(genealogy.keys())[i])
		person = list(genealogy.keys())[i]

		print(f"{'*'*10} ANCESTORS {'*'*10}")
		print(ancestors(genealogy, person))
		print(f"{'*'*10} CHILDREN {'*'*10}")
		print(children(genealogy, person))
		print('#'*50)
		print()