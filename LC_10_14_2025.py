"""

3350. Adjacent Increasing Subarrays Detection II

Medium

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

"""


# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         def hasIncreasingSubarrays(nums: List[int], k: int) -> bool:
#             if k == 1:
#                 return True

#             def isIncreasing(start):
#                 for i in range(start, start+k-1):
#                     if nums[i+1] <= nums[i]:
#                         return False
#                 return True

#             i = 0
#             while i+k+k <= len(nums):
#                 if isIncreasing(i) and isIncreasing(i+k):
#                     return True
#                 i+=1
#             return False
        
#         left = 1
#         right = len(nums)//2
#         res = 1
#         while left <= right:
#             mid = (left + right)// 2
#             if hasIncreasingSubarrays(nums,mid):
#                 res = max(res, mid)
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return res


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans