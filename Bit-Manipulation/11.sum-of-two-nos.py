#https://leetcode.com/problems/sum-of-two-integers/

'''
* Basic algorithm:-
	while b > 0:
		sum_ab = a ^ b
		carry = a & b
		a, b = sum_ab, carry << 1
	return a
* xor does summing without carry
* carry has to be updated every single time and left shifted (because carry is applied one place left in addition)
* Python doesn't have a fixed integer size. So, usage of negative numbers causes problems.
* https://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python
* 32 bit unsigned integers are 0 to 4294967295 (0xffffffff in hexadecimal)
* So, we shift negative nos or nos greater than 4294967295 by and-ing (acts as a modulo operator)
* Eg. -2 & 4294967295 = 4294967294 (within the limit)
* We keep checking if b & mask is 0 to prevent infinite loop
''' 

def get_sum(a: int, b: int) -> int:
	mask = 0xffffffff
	while b & mask:
		a, b = a ^ b, (a & b) << 1
	return a & mask if b > 0 else a


def main():
	a, b = map(int, input().split())
	print(get_sum(a, b))


if __name__ == '__main__':
	main()
