
class Solution:
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def padList(self, head, padding):
        for _ in range(padding):
            new_node = Node(0)
            new_node.next = head
            head = new_node
        return head

    def isGreaterOrEqual(self, head1, head2):
        while head1 and head2:
            if head1.data > head2.data:
                return True
            elif head1.data < head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        return True  # They are equal

    def subtractHelper(self, head1, head2):
        if not head1:
            return None, 0
        result_next, borrow = self.subtractHelper(head1.next, head2.next)
        diff = head1.data - head2.data - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result = Node(diff)
        result.next = result_next
        return result, borrow

    def removeLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head if head else Node(0)

    def subLinkedList(self, head1, head2):
        # Step 1: Calculate lengths and pad the shorter list with zeros
        len1 = self.getLength(head1)
        len2 = self.getLength(head2)
        
        if len1 > len2:
            head2 = self.padList(head2, len1 - len2)
        elif len2 > len1:
            head1 = self.padList(head1, len2 - len1)
        
        # Step 2: Ensure we subtract the smaller number from the larger number
        if self.isGreaterOrEqual(head1, head2):
            result, _ = self.subtractHelper(head1, head2)
        else:
            result, _ = self.subtractHelper(head2, head1)
        
        # Step 3: Remove leading zeros from the result
        result = self.removeLeadingZeros(result)
        return result
