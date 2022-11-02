# Definition for singly-linked list.
from __future__ import annotations
from copy import deepcopy
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

	def create_cycle(self, pos: int) -> ListNode:
		head, i, pointer_to_pos = deepcopy(self), 0, None
		curr_node = head
		while curr_node.next:
			i += 1
			if i == pos:
				pointer_to_pos = curr_node
			curr_node = curr_node.next
		curr_node.next = pointer_to_pos
		return head


# node = ListNode(1)
# obj = ListNode.from_list([1, 2, 3, 4])
# node_with_cycle = obj.create_cycle(1)
