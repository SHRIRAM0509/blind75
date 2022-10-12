# https://leetcode.com/problems/maximum-product-subarray/
# https://www.youtube.com/watch?v=lXVy6YWFcRM

'''
* Brute force takes O(n^3)
* Some thoughts:-
	1. Multiplying two negative nos is a positive number.
	2. 0 is chosen over negative nos.
* Cases:-
	1. [1, 2, 3] -> 6
	2. [2, -5, -2, -4, 3] -> 24
	3. [1, -2, -3] -> 6
	4. [-1, 0, -3] -> 0
	5. [1, 3, -1, 0, 4, 2] -> 8
	6. [-1, -2, -3] -> 6
* Tried using an approach similar to sub array sum. Did not work. 
* Idea was to store max_prod_so_far and min_prod_so_far both. 
* See case 6,
	at i = 3, 
 	1. multiple of all nos so far would have been -6
	2. min so far = -2
	3. max_so_far = 2
	If we dint store min so far, we can't do -2 * -3 = 6
* Because every step depends on it's previous step. This a DP problem
* Final solution takes O(n) to run	
'''

from typing import List

def max_product_array(nums: List[int]) -> int:
	max_prod = max(nums)
	max_prod_so_far = min_prod_so_far = 1

	for num in nums:
		if num == 0: # when num is 0, we set variables back as 1
			max_prod_so_far = min_prod_so_far = 1
			continue
		
		temp1, temp2 = max_prod_so_far * num, min_prod_so_far * num
		max_prod_so_far = max(num, temp1, temp2)
		min_prod_so_far = min(num, temp1, temp2)
		max_prod = max(max_prod_so_far, max_prod)
	return max_prod


def main():
    nums: List[int] = list(map(int, input().split()))
    print(max_product_array(nums))
    
if __name__ == '__main__':
    main()
