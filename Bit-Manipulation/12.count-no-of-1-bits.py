# https://leetcode.com/problems/number-of-1-bits/

'''
* If a bit is one or not can be found by and-ing the bit with 1.
* Run a loop and keep updating the count. Update n by right shifting it.
* Final solution in O(n)
'''


def no_of_1_bits(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count


def main():
    n = int(input(), 2)  # converting str to binary here itself
    print(no_of_1_bits(n))


if __name__ == '__main__':
    main()
