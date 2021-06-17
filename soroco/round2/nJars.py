def solution(jars):
	if jars == []:
		return 0
	include = jars[0]
	exclude = 0
	exclNew = 0

	for i in range(1, len(jars)):
		exclNew = max(include,exclude)
		include = exclude+jars[i]
		exclude = exclNew

	return max(include, exclude)

if __name__ == '__main__':

	# jars = list(map(int, input().split())) or [27, 12, 19, 13, 11]
	jars = [10, 34, 2, 1, 27]
	
	print(solution(jars))