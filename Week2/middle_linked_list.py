# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self): 
        self.head = None
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A=[head]
        while(A[-1].next):
            A.append(A[-1].next)
        return A[len(A)//2].val
  
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    ll = Solution() 
  
    ll.head = Node(1) 
    second = Node(2) 
    third = Node(3)
    four = Node(4)
    five = Node(5) 
  
    ll.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node 
    third.next = four
    four.next = five
  
    ans=ll.middleNode(ll.head)
    print(ans) 
