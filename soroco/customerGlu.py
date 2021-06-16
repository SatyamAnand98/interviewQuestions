def check(shots, ch, length):
    return (length-shots[::-1].index(ch, 0, length))

def Shots(shots, lis):
    result = {}
    maximum = 0
    length = len(shots)
    if length==0:
        return 0
    status = check(shots, shots[0], length)
    
    for i in range(0, status):
        result[shots[i]] = shots[i]

    for i in result.keys():
        present = check(shots, i, length)
        if present>maximum:
            maximum = present


    for i in range(0, maximum):
        result[shots[i]] = shots[i]

    for i in result.keys():
        present = check(shots, i, length)
        if present>maximum:
            maximum = present
        
    lis.append(maximum)
    Shots(shots[maximum:], lis)
    return lis
    
    

if __name__=="__main__":
    shots = list(input().split()) or list("z z c b f c h z i h i k o d d n p o s v u y w j q x x".split())
    lis = []

    Shots(shots, lis)
    print([11, 1, 6, 1, 1, 1, 1, 1, 1, 1, 2]==lis)