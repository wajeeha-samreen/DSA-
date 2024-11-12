class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def zigZagList(head): 
    flag = True
    current = head 
    while current.next: 
        if flag:
            if current.data > current.next.data: 
                current.data, current.next.data = current.next.data, current.data
        else:
            if current.data < current.next.data: 
                current.data, current.next.data = current.next.data, current.data
        current = current.next
        flag = not flag
    return head 

def push(head, k): 
    tem = Node(k) 
    tem.next = head 
    head = tem 
    return head 

def display(head): 
    curr = head 
    while curr: 
        print(curr.data, "->", end=" ") 
        curr = curr.next
    print("None") 

head = None
head = push(head, 1) 
head = push(head, 2) 
head = push(head, 6) 
head = push(head, 8) 
head = push(head, 7) 
head = push(head, 3) 
head = push(head, 4) 

print("Given linked list:")
display(head) 

head = zigZagList(head) 
print("\nZig Zag Linked list:")
display(head) 
