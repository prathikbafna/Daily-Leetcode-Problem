"""

611. Valid Triangle Number

Medium

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        def binary_search(left, right, tar):
            while left < right and right < len(nums):
                mid = left + (right - left) // 2
                if nums[mid] > tar:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
            
        nums.sort() 
        l = len(nums)
        res = 0
        for i in range(l):
            for j in range(i+1,l):
               cur = nums[j]-nums[i]
               res+=i-binary_search(0,i,cur)
        
        return res