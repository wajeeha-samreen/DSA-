class Solution:
    
    def mergenode(self, node1, node2):
        ans = Node(-1)
        temp = ans
        while(node1!=None and node2 !=None):
            if(node1.data < node2.data):
                temp.bottom = node1
                node1 = node1.bottom
            else:
                temp.bottom = node2
                node2 = node2.bottom
            temp = temp.bottom
        
        if(node1!=None):
            temp.bottom = node1
        
        if(node2!=None):
            temp.bottom = node2
        
        return ans.bottom
    
    
    
    def flatten(self, root):
        cur = root
        root = root.next

        while(root!=None):
            # self.print_node(cur)
            cur = self.mergenode(cur,root)
            root = root.next
        
        return cur
