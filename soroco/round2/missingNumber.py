# 2. Find the missing numbers and some questions on time complexity?

def total(n):
	return ((n*(n+1))//2)

def solution(li):
	return total(len(li)+1)-sum(li)

if __name__ == '__main__':
	li = [[1, 2, 4, 6, 3, 7, 8], [1, 2, 3, 5]]
	for i in li:
		print(solution(i))