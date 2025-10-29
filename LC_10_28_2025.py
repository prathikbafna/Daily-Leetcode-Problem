"""
3370. Smallest Number With All Set Bits

Easy

You are given a positive number n.

Return the smallest number x greater than or equal to n, such that 
the binary representation of x contains only set bits

"""


import math

class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1

        v = ceil(log(n,2))
        if v == log(n,2):
            v+=1
        return (2**v) - 1