# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=0
#         self.next=None     
class Solution(object):
    
    def deleteDuplicates(self,head):
        temp=newHead=ListNode(-101) 
        current=head
        while current:
            if current.val==temp.val:
                current=current.next 
            else:
                temp.next=ListNode(current.val)
                temp=temp.next 
                current=current.next 
        return(newHead.next)
