import json
import sys

def solution(sentence_1, sentence_2, similarity) -> bool:
	#write your code here
	if len(sentence_1)!=len(sentence_2):
		return 0
	
	similar = dict()

	for x,y in similarity:
		if x not in similar.keys():
			similar[x] = [y]
		else:
			similar[x].append(y)
		if y not in similar.keys():
			similar[y] = [x]
		else:
			similar[y].append(x)

	# for key in similar.keys():
	# 	print(f"{key} = {similar[key]}")

	for i in range(len(sentence_1)):
		try:
			if sentence_2[i] in similar[sentence_1[i]] or sentence_1[i] in similar[sentence_2[i]] or sentence_1[i] in similar[similar[sentence_1[i]][0]]:
				pass
			else:
				return 0
		except KeyError:
			return 0

	return 1

if __name__ == '__main__':

	sample_inputs = json.loads(open('./input.json').read())

	for key in sample_inputs.keys():
		res = solution(sample_inputs[key]["sentence_1"], sample_inputs[key]["sentence_2"], sample_inputs[key]["similar_words"])
		if int(res) == int(sample_inputs[key]["result"]):
			print(f"PASSED TEST CASE {int(key)+1}")
			# print("\n"*50)
		else:
			print(f"FAILED TEST CASE {int(key)+1}")
			sys.exit(1)

	print("PASSED ALL TEST CASES")
		