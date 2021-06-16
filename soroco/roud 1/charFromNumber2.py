global mem
mem = {}

def solve(num):
	if num>0 and num<=26:
		if num-1 in mem.keys():
			return mem[num-1]
		else:
			mem[num-1] = arr[num-1]
	
	if num<=0:
		return

	solve(num%10)
	solve(num//10)

def solution(num):
	length = len(str(num))
	count = 0
	while(count<=length):
		solve(num%(10**count))
		solve(num//(10**count))
		count += 1


if __name__ == '__main__':
	global arr
	arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	num = 12516
	
	solution(num)
	
	for i in mem.keys():
		print(mem[i])