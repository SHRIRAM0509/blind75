# https://leetcode.com/problems/merge-k-sorted-lists/


'''
* Brute force:
	- Let arr = [a1, a2, a3, ...] and each element in arr is a list
	- f(arr) = merge2(merge2(merge2(a1, a2), a3), a4) ...
	But this does unnecessary comparisons multiple times

* Divide and conquer:
	- Let arr = [a1, a2, a3, a4, ...] and each element in arr is a list
	- f(arr) = merge2(merge2(a1, a2), merge2(a3, a4), ...) ...
'''


from typing import List, Optional
import os
import sys

sys.path.insert(1, os.getcwd()) # to make imports work

from ListNode import ListNode


# refer ./29.merge-two-sorted-lists.py
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	if not list1:
		return list2

	if not list2:
		return list1

	if list1.val < list2.val:
		return ListNode(list1.val, merge_two_lists(list1.next, list2))

	return ListNode(list2.val, merge_two_lists(list1, list2.next))


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
	if not lists:
		return None

	while len(lists) > 1:
		if len(lists) & 1:
			lists.append(None)
		lists = [merge_two_lists(lists[i], lists[i+1])
                    for i in range(0, len(lists), 2)]
	return lists[0]


def get_lists():
    lists = []
    for _ in range(int(input())):
     temp = list(map(int, input().split()))
     node = ListNode.from_list(temp)
     lists.append(node)
    return lists


def main():
	lists = get_lists()
	print(merge_k_lists(lists))


if __name__ == '__main__':
	main()
