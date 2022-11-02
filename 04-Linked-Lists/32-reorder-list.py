# https://leetcode.com/problems/reorder-list/


'''
Basic approach:-
	* use dictionary and construct head - O(n) time and space
 
Efficient approach:-
	* If head is None, terminate
	* Find middle of the list with Hare and Tortoise algorithm (https://youtu.be/gBTe7lFR3vc?t=360)
	* If head == middle, return head
	* find and store reversed middle
	* Set middle.next as None
	* So, final answer is obtained by merging head and reversed middle
	* This takes O(n) time and space (efficient)
'''


from typing import Optional
import os
import sys

sys.path.insert(1, os.getcwd()) # to make imports work

from ListNode import ListNode


# Also called as Floyd's Tortoise and Hare algorithm
def get_middle_of_list(head: Optional[ListNode]) -> Optional[ListNode]:
	fast, slow = head.next, head

	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
	return slow


def reverse_list(head: Optional[ListNode], prev=None) -> Optional[ListNode]:
	if not head:
		return None
	prev = ListNode(head.val)
	while head := head.next:
		prev = ListNode(head.val, prev)
	return prev


def reorder_list(head: Optional[ListNode]) -> None:
	"""
	Do not return anything, modify head in-place instead.
	"""

	if not head or not head.next:
		return

	middle = get_middle_of_list(head)
	right = reverse_list(middle.next)
	middle.next = None  # sets tail of first half to None

	while head and right:
		new_right = right.next
		right.next, head.next = head.next, right
		head, right = right.next, new_right


def main():
	nums = list(map(int, input().split()))
	head = ListNode.from_list(nums)
	print(reorder_list(head))


if __name__ == '__main__':
	main()
