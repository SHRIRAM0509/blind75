# https://leetcode.com/problems/container-with-most-water/

'''
* Area increases when height difference is less or width is more
* So, have to find end points that are far off and have similar heights.
* Brute force algorithm takes O(n^2) time
* For optimal solution, using sliding window technique (double pointers) with i at first index and j at last index.
* Compute area and move the pointer with the shorter height one step.
* Final solution takes O(n) time to compute.
'''

from typing import List


def area_of_container(h1, h2, i, j):
	width = j - i
	height = min(h1, h2)
	return width * height


def get_max_area(heights: List[int]) -> int:
	i, j = 0, len(heights) - 1
	max_area = 0

	while i >= j:
		h1 = heights[i]
		h2 = heights[j]
		curr_area = area_of_container(h1, h2, i, j)
		max_area = max(max_area, curr_area)

		# move pointer if it's height is shorter
		if (h1 >= h2):
			j -= 1
		else:
			i += 1
	return max_area


def main():
	nums: List[int] = list(map(int, input().split()))
	print(get_max_area(nums))


if __name__ == '__main__':
	main()
