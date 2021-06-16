class Node:
    def __init__(self):
        self.val = None
        self.next = None


def palindrome(head):
    # write your code here
    result = []
    temp = head
    pali = False
    while temp!=None:
        result.append(temp.val)
        temp = temp.next
        
    while head!=None:
        s = result.pop()
        if head.val == s:
            pali = True
        else:
            pali = False
        
        head = head.next
    return pali


if __name__ == '__main__':
    arr = list(input())
    
    head = Node()
    cur = Node()

    for i in arr:
        temp = Node()
        if head.val==None:
            head.val = i
            cur = head
        elif head.next==None:
            temp.val = i
            head.next = temp
            cur = temp
        else:
            temp.val = i
            cur.next = temp
            cur = temp

    print(palindrome(head))

