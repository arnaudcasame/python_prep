from typing import Optional
from data_structures.list_node import ListNode


def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    cumul: int = 0
    bucket: dict[int, ListNode] = {}
    tmp: ListNode = ListNode(0, head)
    bucket[0] = tmp

    while head != None:
        cumul = cumul + head.val

        if cumul in bucket:
            tmpCumul = cumul
            tmpRemove = bucket[cumul].next

            while tmpRemove != head:
                tmpCumul += tmpRemove.val
                bucket.pop(tmpCumul)
                tmpRemove = tmpRemove.next
            bucket[cumul].next = head.next
        else:
            bucket[cumul] = head

        head = head.next
    return tmp.next