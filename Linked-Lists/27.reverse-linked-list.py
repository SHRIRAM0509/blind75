# https://leetcode.com/problems/reverse-linked-list/


'''
* Termination cases:
	1. if head is None
	2. head doesn't have a next
* Idea is to use recursion to make nth element as the head and n-1 as it's next
* So, we construct a ListNode from scratch
'''


from typing import Optional

from ListNode import ListNode


def reverse_list(head: Optional[ListNode], prev=None) -> Optional[ListNode]:
	if not head:
		return None

	if not head.next:
		return ListNode(head.val, prev)

	return reverse_list(head.next, ListNode(head.val, prev))


def main():
	nums = list(map(int, input().split()))
	head = ListNode.from_list(nums)
	print(reverse_list(head))


if __name__ == '__main__':
	main()
