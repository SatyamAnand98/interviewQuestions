def solve(num):
	if (num<26 and num>0):
		return arr[num-1]


if __name__ == '__main__':
	global arr
	arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	num = "125"
	length = len(num)
	num = int(num)
	count = 1
	result = []
	while(count<length):
		checksum = 10**count
		print(f"num%checksum = {num%checksum}")
		print(f"checksum = {checksum}")
		print(f"count = {count}")
		print()
		count += 1
		result.append(solve(num%checksum))

	print(result)