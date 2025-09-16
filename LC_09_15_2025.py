"""

2197. Replace Non-Coprime Numbers in Array

Hard

You are given an array of integers nums. Perform the following steps:

Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

 

Example 1:

Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]
Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.
Example 2:

Input: nums = [2,2,1,1,3,3,3]
Output: [2,1,1,3]
Explanation: 
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
- (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [2,1,1,3].
Note that there are other ways to obtain the same resultant array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
The test cases are generated such that the values in the final array are less than or equal to 108.

"""


import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # solution 1 - passes 69/71 test cases
        # brute force
        # if len(nums) == 1:
        #     return nums

        
        # nums.sort(reverse = True)
        # change = True
        # while change:
        #     change = False
        #     left = 0
        #     res = []
        #     while left < len(nums)-1:
        #         right = left + 1
        #         n1 = nums[left]
        #         n2 = nums[right]
        #         if math.gcd(n1,n2) == 1:
        #             res.append(n1)
        #             left += 1
        #         else:
        #             change = True
        #             nums[right] = math.lcm(n1,n2)
        #             left+=1

        #     if left < len(nums):
        #         n1 = nums[left]
        #         if not res:
        #             res.append(n1)
        #         else:
        #             n2 = res[-1]
        #             if math.gcd(n1,n2) == 1:
        #                     res.append(n1)
        #             else:
        #                 res[-1] = math.lcm(n1,n2)
        #     nums = res
        # return res

        # solution2 - using stacks

        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                # num = math.lcm(stock.pop(), num)
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack

