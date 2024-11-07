#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self, head):
        # Edge case: if the list is empty or has only one node, return it as is
        if not head or not head.next:
            return head
      
        prev = None
        temp = head
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        head = prev  
        
        max_num = head.data
        temp = head
        while temp and temp.next:
            if temp.next.data < max_num:
                temp.next = temp.next.next  
            else:
                max_num = temp.next.data 
                temp = temp.next
        
        
        prev = None
        temp = head
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        head = prev
        
        return head
        
