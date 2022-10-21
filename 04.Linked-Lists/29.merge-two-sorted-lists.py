# https://leetcode.com/problems/merge-two-sorted-lists/


'''
* If left <= right, then f(left.next, right), else f(left, right.next).
* Terminate when left or right is empty and return non-empty list.
'''


from typing import Optional

from ListNode import ListNode


def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	if not list1:
		return list2

	if not list2:
		return list1

	if list1.val < list2.val:
		return ListNode(list1.val, self.merge_two_lists(list1.next, list2))

	return ListNode(list2.val, self.merge_two_lists(list1, list2.next))


def main():
	list1 = list(map(int, input().split()))
	list1_head = ListNode.from_list(list1)

	list2 = list(map(int, input().split()))
	list2_head = ListNode.from_list(list2)

	print(merge_two_lists(list1_head, list2_head))


if __name__ == '__main__':
	main()
