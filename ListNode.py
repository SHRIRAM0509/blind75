# Definition for singly-linked list.
from __future__ import annotations
from typing import Any, List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(self, nums: List[Any]) -> Optional[ListNode]:
        if not nums:
            return None
        head = ListNode(nums[0])
        node = head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next
        return head

    def __repr__(self) -> str:
        arr = []
        head = self
        while head:
            arr.append(str(head.val))
            head = head.next
        arr.append("None")
        return " -> ".join(arr)


# node = ListNode(1)
# obj = ListNode.from_list([1, 2, 3, 4])
