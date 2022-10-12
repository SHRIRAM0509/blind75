# https://leetcode.com/problems/reverse-bits/

'''
* Given 32 length bit string
* Expected 32 bit reversed string
* Idea:
	* Last bit can be found by and-ing num with 1
	* Update num for next iteration by right shifting it by 1
	* Left shift reversed_num every time before doing the above steps
	* Example (thought process in decimal notation)
		1. 23 reversed is 32. We do 23 modulo 10 to get 3
		2. Update by doing 23 // 10 => 2
		3. In next iter, we add this 2 to (3 * 10)
	* Equivalent steps in binary
		1. Last digit can be found by using & 1.
		2. Update by right shift
		3. Add by using 'or' and for moving one step left use left shift
* Solution is a constant time algorithm (32 time units).
'''


def reverse_bits(num: int, default_bit_length=32) -> int:
	reversed_num = 0
	for _ in range(default_bit_length):
		reversed_num <<= 1
		reversed_num |= num & 1
		num >>= 1
	return reversed_num


def main():
	input_bit_string = input()
	n = int(input_bit_string, 2)
	reversed_num = reverse_bits(n)
	print(f"Original:- {n} ({input_bit_string})")
	print(f"Reversed:- {reversed_num} ({bin(reversed_num)[2:]})")


if __name__ == '__main__':
	main()
