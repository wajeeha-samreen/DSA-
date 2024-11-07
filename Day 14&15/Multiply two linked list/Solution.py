class Solution:
    
    MOD = 1000000007

    def to_number(self, head):
        num = 0
        while head:
            num = (num * 10 + head.data) % self.MOD
            head = head.next
        return num
        
    def multiply_two_lists(self, first, second):
        num1 = self.to_number(first)
        num2 = self.to_number(second)
        return (num1 * num2) % self.MOD
      
