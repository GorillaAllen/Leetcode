# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(l1, l2):
        if len(l1) > len(l2):
            while len(l1) != len(l2):
                l2.append(0)
        if len(l2) > len(l1):
            while len(l1) != len(l2):
                l1.append(0)
        l3 = []
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
        for i in range(len(l3)-1):
            if l3[i] >= 10:
                l3[i] = l3[i] - 10
                l3[i+1] = l3[i+1] + 1
            if l3[-1] >= 10:
                l3[-1] = l3[-1] - 10
                l3.append(1)
        return l3
        