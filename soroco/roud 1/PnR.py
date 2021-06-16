# Given an input integer n, count natural numbers in range [1, n] whose all permutations are greater than or equal to the number itself.

def countNumber(n):
	
	result = 0
	stack = []

	for i in range(1, 10):
		if i<=n:
			stack.append(i)
			result += 1

			while len(stack)!=0:
				top = stack.pop()
				for j in range(top%10, 10):
					num = top*10+j
					if num<=n:
						stack.append(num)
						result += 1
	return result

if __name__ == '__main__':
	num = int(input())
	print(countNumber(num))