"""
Sort a linked list in O(n log n) time using constant space complexity.
===========
In order to get O(n log n) performance, we need to adapt divide and conquer algorithm
That is, we can apply quicksort, heapsort and merge sort.
In the code below, I used merge sort. The idea is :
    (1) Break the list into 2 sublist with size N/2 
    (2) Recursively sort the sublist
    (3) Merge the sublists and return final sorted list

Hence, T(N) = 2*T(N/2) + N (merging) for N>1 
            = 2* (2*T(N/4)+N/2) + N = 4* T(N/4) + 2N
            = ... = N* T(N/N) + N(log2 N)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head==None:
            return None
        length = 0
        node = head
        while node!= None:
            node = node.next
            length+=1
        return self.sort(head,length)
    
    def sort(self, head, length):
        # recursively break the linked list into n/2 sublist and sort
        
        # base case
        if length==1:
            return head
        
        list2 =head
        for _ in range(length/2):
            list2 = list2.next
        
        len1 = length/2
        len2 = length-length/2
        list1 = self.sort(head,len1)
        list2 = self.sort(list2, len2)
        
        return self.merge(list1,list2,len1,len2)

    def merge(self,list1,list2,len1,len2):
        node=ListNode(0)
        finalList = node
        i=0
        j=0
        while i<len1 and j<len2:
            if list1.val < list2.val:
                finalList.next = list1
                list1 = list1.next
                i+=1
            else: #list2 < list1
                finalList.next = list2
                list2=list2.next
                j+=1
            finalList = finalList.next
        while j<len2:
            finalList.next = list2
            list2=list2.next
            finalList = finalList.next
            j+=1
        while i<len1:
            finalList.next = list1
            list1=list1.next
            finalList = finalList.next
            i+=1
        finalList.next = None
        
        return node.next
            
 
