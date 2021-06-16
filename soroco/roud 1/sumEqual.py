# arr = [16, 17, 4, 3, 5, 2]

def sumEqual(arr):
    # write your code here
    result = []
    total = sum(arr)
    for i in arr:
        if i==total-i:
            result.append(i)
    if result!=[]:
        return result
    else:
        return -1


if __name__ == '__main__':
    arr = list(map(int, input().split(', ')))
    print(sumEqual(arr))