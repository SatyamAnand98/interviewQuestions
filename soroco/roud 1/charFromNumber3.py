def subString(Str, n):
	numList = []
	for Len in range(1, n+1):
		for i in range(n-Len+1):
			string = ""
			j = i+Len-1
			for k in range(i, j+1):
				string += Str[k]
			numList.append(int(string))
	return numList

def solution(li):
	for i in li:
		if i>0 and i<=26:
			print(arr[i-1])


if __name__ == '__main__':
	global arr
	arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	num = str(125)
	solution(subString(num, len(num)))
