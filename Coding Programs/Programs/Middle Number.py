# List Middle Number


class Solution(object):
    new_lst = []
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos = (len(head)//2)
        neg = len(head)//2
        if len(head) % 2 == 0:
            self.new_lst = self.new_lst + head[pos:]            
        else:
            self.new_lst = self.new_lst + head[neg:]            

        return self.new_lst

lst = [1,2,3,4,5,6]
x = Solution()
print(x.middleNode(lst))
