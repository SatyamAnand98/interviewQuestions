# 2) Array rotation by n

def rightRotation(arr, n):
	if n==0:
		return arr
	return rightRotation([arr[-1]]+arr[:-1], n-1)

def leftRotation(arr, n):
	if n==0:
		return arr
	return leftRotation(arr[1:]+[arr[0]], n-1)

if __name__ == '__main__':
	
	arr = [0,1,6,1,8,8,7,8,8]
	n = 9
	l = len(arr)
	print(rightRotation(arr, n%l))
	print(leftRotation(arr, n%l))