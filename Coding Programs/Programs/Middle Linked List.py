# Middle of linked list

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

lst = [1,2,3,4,5,6]
x = Solution()
print(x.middleNode(lst))




