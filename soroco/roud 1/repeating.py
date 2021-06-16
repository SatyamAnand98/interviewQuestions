s = 'soroco'

result = {}

for i in s:
	if i not in result.keys():
		result[i] = 1
	elif i in result.keys():
		result[i] += 1


print(''.join(list(result.keys())))