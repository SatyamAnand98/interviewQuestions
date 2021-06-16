class Node:
    def __init__(self):
        self.val = None
        self.next = None

def traversal(head):
    result = []
    while(head!=None):
        result.append(head.val)
        head = head.next
    return result

def addition(head1, head2):

    remainder = 0
    
    head = Node()
    cur = Node()

    while(head2!=None or head1!=None):
        sum = 0
        print(head2.val)
        if head2!=None:
            b = head2.val
            head2 = head2.next
        else:
            b = 0
        
        if head1 != None:
            a = head1.val
            head1 = head1.next
        else:
            a = 0

        sum = remainder+a+b

        remainder = sum//10
        sum = sum%10
        temp = Node()

        if head.val == None:
            head.val = sum
            cur = head
        elif head.next == None:
            temp.val = sum
            head.next = temp
            cur = temp
        else:
            temp.val = sum
            cur.next = temp
            cur = temp


    if remainder!=0:
        temp = Node()
        temp.val = remainder
        cur.next = temp
        cur = temp
        
    print(remainder, sum)
    print(f"SUM = {traversal(head)}")
    


if __name__ == '__main__':
    head1 = Node()
    head2 = Node()
    cur1 = Node()
    cur2 = Node()
    l1 = [5,6]
    l2 = [5,4,9]
    ll1 = list(map(int, input().split())) or l1
    ll2 = list(map(int, input().split())) or l2

    for i in ll1:
        temp1 = Node()
        
        if head1.val == None:
            head1.val = i
            cur1 = head1
        elif head1.next == None:
            temp1.val = i
            head1.next = temp1
            cur1 = temp1
        else:
            temp1.val = i
            cur1.next = temp1
            cur1 = temp1


    for j in ll2:
        temp2 = Node()
        if head2.val == None:
            head2.val = j
            cur2 = head2
        elif head2.next == None:
            temp2.val = j
            head2.next = temp2
            cur2 = temp2
        else:
            temp2.val = j
            cur2.next = temp2
            cur2 = temp2
    
    print(traversal(head1))
    print(traversal(head2))
    addition(head1, head2)
