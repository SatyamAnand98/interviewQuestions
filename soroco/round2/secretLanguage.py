def solution(sm, wl):
	result = {}
	for i in wl:
		string = ""
		for j in i.upper():
			string += sm[ord(j)-ord('A')]
		result[string] = string

	return len(result)

if __name__ == '__main__':
	secret_mapping = ["b", "b", "d", "d", "f", "f", "f", "h", "j", "j", "l", "l", "n", "n", "p", "p", "r", "r", "t", "t", "v", "v", "x", "x", "z", "z"]
	word_list = ["food", "good", "zap", "yap"]

	print(solution(secret_mapping, word_list))