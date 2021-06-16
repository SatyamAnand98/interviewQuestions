import time

def count2(arr, total, i):
	if total == 0:
		return 1
	elif total<0:
		return 0
	elif i<0:
		return 0
	else:
		return count(arr, total-arr[i], i-1, mem)+count(arr, total, i-1, mem)

def count(arr, total, i, mem):
	key = f"{total}:{i}"
	if key in mem.keys():
		return mem[key]
	if total == 0:
		return 1
	elif total<0:
		return 0
	elif i<0:
		return 0
	elif total<arr[i]:
		to_return = count(arr, total, i-1, mem)
	else:
		to_return = count(arr, total-arr[i], i-1, mem)+count(arr, total, i-1, mem)
	mem[key] = to_return
	return to_return

if __name__ == '__main__':
	t1 = time.time()
	mem = {}
	arr = [2,4,6,10]
	total = 16
	print(count(arr, total, len(arr)-1, mem))
	print(time.time()-t1)
	
	print()

	t1 = time.time()
	arr = [2,4,6,10]
	total = 16
	print(count2(arr, total, len(arr)-1))
	print(time.time()-t1)
