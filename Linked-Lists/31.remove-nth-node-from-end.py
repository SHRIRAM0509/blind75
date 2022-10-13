# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


'''
* Run a loop to maintain dict
* Then, nodes[i-n-1].next = nodes[i-n+1]
* O(n) space and O(n) time solution
* See, if space can be improved
'''

from collections import defaultdict
from typing import Optional

from ListNode import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
	nodes, i, curr_node = defaultdict(lambda: None), 1, head.next
	nodes[0] = head
	while curr_node:
		nodes[i] = curr_node
		i += 1
		curr_node = curr_node.next

	if n == i:
		return nodes[1]

	nodes[i-n-1].next = nodes[i-n+1]

	return head


def main():
	nums = list(map(int, input().split()))
	head = ListNode.from_list(nums)
	n = int(input())
	print(remove_nth_from_end(head, n))


if __name__ == '__main__':
	main()
