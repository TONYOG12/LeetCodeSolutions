# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0, head)

        if not dummy:
            return head

        prev, cur = dummy, head


        while cur and cur.next:
            nextNode = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = nextNode 

            #dummy next pointing to new head
            prev.next = second

            prev = cur
            cur = nextNode

        return dummy.next
