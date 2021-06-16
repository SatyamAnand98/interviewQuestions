# 1. Reverse the array without .reverse method ?

def solution(li, length):
	for i in range((length//2)+1):
		li[i], li[length-i-1] = li[length-i-1], li[i]

	return li

if __name__ == '__main__':
	li = [1,2,3,4,5,6,7,8]
	length = len(li)
	print(solution(li, length))