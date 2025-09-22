"""

3005. Count Elements With Maximum Frequency

Easy

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""



# from collections import defaultdict
# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         freq = defaultdict(int)
#         max_freq = 1
#         for i in nums:
#             freq[i] += 1
#             max_freq = max(max_freq, freq[i])
#         res = 0
#         for i in freq:
#             if freq[i] == max_freq:
#                 res += max_freq
        
#         return res

from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums):
        frequencies = defaultdict(int)
        max_frequency = 0
        total_frequencies = 0

        # Find the frequency of each element
        # Determine the maximum frequency
        # Calculate the total frequencies of elements with the maximum frequency
        for num in nums:
            frequencies[num] = frequencies[num] + 1
            frequency = frequencies[num]

            # If we discover a higher frequency element
            # Update max_frequency
            # Re-set totalFrequencies to the new max frequency
            if frequency > max_frequency:
                max_frequency = frequency
                total_frequencies = frequency
            # If we find an element with the max frequency, add it to the total
            elif frequency == max_frequency:
                total_frequencies += frequency

        return total_frequencies