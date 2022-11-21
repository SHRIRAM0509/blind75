# https://leetcode.com/problems/find-median-from-data-stream/


'''
* A basic, really quick solution:
	* Keep appending the elements to a list in add_num function
	* In find_median, sort the list if it is first time called in O(nlogn) time
	* If array is sorted use bisect.insort to insert element into a sorted array in O(logn) time
	* Because the array is sorted, the median can be found in O(1) time subsequently

* Two heaps approach:
	* This is the proper algorithmic approach
	* Refer: https://www.youtube.com/watch?v=itmhHWaHupI
	* Idea is to have two heaps - a max heap and a min heap
	* Assuming the list is sorted, say [1, 2, 3, 4, 5, 6] -> [1, 2, 3] will be in max heap and [4, 5, 6] in min heap.
	* So, root of max heap is 3 and for min heap it's 4. This makes finding median easy
	* If the number of elements is odd, one of these heaps will have an extra element. This balancing of elements needs to be handled.
	* Python only supports min heap by default. To implement a max heap, multiply the number with -1.
	* Always insert to max heap
	* If the root of max heap > root of min heap, move root to the min heap.
	* If the size difference is > 1, balance the heaps by moving the root to the other heap.
'''


from bisect import insort
from heapq import heappush, heappop


class MedianFinderWithoutHeap:

	def __init__(self):
		self.arr = []
		self.is_sorted = False

	def add_num(self, num: int) -> None:
		if self.is_sorted:
			insort(self.arr, num)
		else:
			self.arr.append(num)

	def find_median(self) -> float:
		if not self.is_sorted:
			self.arr.sort()
			self.is_sorted = True

		mid = len(self.arr)//2
		if len(self.arr) & 1:
			return float(self.arr[mid])

		return (self.arr[mid-1] + self.arr[mid]) / 2


class MedianFinder:

	def __init__(self):
		self.max_heap = []  # smaller numbers
		self.min_heap = []  # larger numbers

	def _balance_heaps(self):
		if len(self.max_heap) - len(self.min_heap) > 1:
			num = -1 * heappop(self.max_heap)
			heappush(self.min_heap, num)

		if len(self.min_heap) - len(self.max_heap) > 1:
			num = heappop(self.min_heap)
			heappush(self.max_heap, -1 * num)

	def add_num(self, num: int) -> None:
		heappush(self.max_heap, -1 * num)

		# check if max heap root > min heap root
		if self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0]:
			num = -1 * heappop(self.max_heap)
			heappush(self.min_heap, num)

		self._balance_heaps()

	def find_median(self) -> float:

		if len(self.max_heap) == len(self.min_heap):
			return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2

		return (-1 * self.max_heap[0]) if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
