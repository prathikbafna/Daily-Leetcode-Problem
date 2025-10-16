"""

2598. Smallest Missing Non-negative Integer After Operations

Medium

Hint
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

"""


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = Counter(x % value for x in nums)
        ptr = 0
        while mp[ptr % value] > 0:
            mp[ptr%value] -= 1
            ptr+=1
        return ptr