# https://leetcode.com/problems/climbing-stairs/

'''
* See below pattern:-
	0 -> 1 (ways to climb stairs with 0 steps is 1)
	1 -> 1
	2 -> 1,1; 2
	3 -> 1,2 | 1,1,1; 2,1
	4 -> 1,1,2; 2,2 | 1,1,1,1; 1,2,1; 1,2,1
* We can see 4's results = (2 steps from 2) + (1 step from 3)
* So, at any point, ways[i] = ways[i-1] + ways[i-2]
'''


def find_num_ways_to_climb_stairs(n: int) -> int:
	num_ways_to_climb = [0]*(n+1)
	num_ways_to_climb[0] = 1
	num_ways_to_climb[1] = 1
	for i in range(2, n+1):
		num_ways_to_climb[i] = num_ways_to_climb[i-1] + num_ways_to_climb[i-2]
	return num_ways_to_climb[n]


def main():
	n = int(input())
	print(find_num_ways_to_climb_stairs(n))


if __name__ == '__main__':
	main()
