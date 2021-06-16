# {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

def leaderElement(arr, size):
    # write your code here
    result = []
    maxNum = arr[size-1]
    result.append(maxNum)
    for i in range(size-2, -1, -1):
        if maxNum<arr[i]:
            result.append(arr[i])
            maxNum = arr[i]
    return result

if __name__ == '__main__':
    arr = list(map(int, input().split(', ')))
    size = len(arr)
    print(leaderElement(arr, size))