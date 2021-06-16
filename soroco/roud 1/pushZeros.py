# 2) Given an array with positive and negative elements, push all the zero elements to back of array
def pushZerosToEnd(arr, length):
    count = 0
    result = []

    for i in arr:
        if i!=0:
            result.append(i)
            count += 1
    
    while length>=count:
        result.append(0)
        count += 1

    return result

if __name__ == '__main__':
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    arr = pushZerosToEnd(arr, n)
    print("Array after pushing all zeros to end of array:")
    print(arr)
