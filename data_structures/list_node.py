# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(array: List) -> ListNode:
        head = None
        current = None
        for val in array:
            if not head:
                head = ListNode(val)
                current = head
            else:
                current.next = ListNode(val)
                current = current.next
        return head
    
    @staticmethod
    def toList(node: ListNode) -> List:
        array = []
        while node:
            array.append(node.val)
            node = node.next
        return array
