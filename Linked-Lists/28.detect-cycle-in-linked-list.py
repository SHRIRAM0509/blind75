# https://leetcode.com/problems/linked-list-cycle/


'''
* id(node) gives the address in which a variable is stored
* Maintain a dictionary with id(node) as key
* If the key is seen again, then there is cycle
* If the next node is None at some point, then cycle is not there
'''


from collections import defaultdict
from typing import Optional

from ListNode import ListNode


def has_cycle(self, head: Optional[ListNode]) -> bool:
	nodes = defaultdict(lambda: False)
	nodes[id(head)] = True
	while head:
		head = head.next
		key = id(head)
		if key in nodes:
			return True
		nodes[key] = True
	return False


def main():
	nums = list(map(int, input().split()))
	head = ListNode.from_list(nums)
	pos = int(input())
	head_with_cycle = head.create_cycle(pos)
	print(has_cycle(head_with_cycle))


if __name__ == '__main__':
	main()

