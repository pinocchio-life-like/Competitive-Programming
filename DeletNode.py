# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=None 
    
        
class Solution(object):
    def deleteNode(self,node):
        node.val=node.next.val
        node.next=node.next.next