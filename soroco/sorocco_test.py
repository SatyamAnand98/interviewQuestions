def remove_dup(st):
  # You code goes here 
  result = {}

  for i in st:
    if i.upper() not in result.keys() and i.lower() not in result.keys():
      result[i] = i
    
  print(''.join(result.keys()))

if __name__ == '__main__':
  sample = ["Beyourbest", "soroco"]
  for i in sample:
    remove_dup(i)

'''
# def leader(A):
#   # your code goes here
#   leader = A[::-1][0]
#   length = len(A)
#   stack = []
#   stack.append(leader)
#   for i in A[::-1][1:]:
#     if i >= leader:
#       stack.append(i)
#       leader = i
#   print(stack[::-1])

# if __name__ == '__main__':
#   sample = [[16,17,4,3,5,2], [1,2,3,4,0]]
#   for i in sample:
#     leader(i)

def sort(list):
  l = len(list)
  for i in range(l):
    for j in range(i):
      if list[i]>list[j]:
        list[i], list[j] = list[j], list[i]

  print(list)


if __name__ == '__main__':
  list = [16,17,4,3,5,2]
  sort(list)
'''