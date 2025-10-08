"""
2300. Successful Pairs of Spells and Potions
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

"""


# class Solution:
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#         res = []
#         potions.sort()
#         l = len(potions)
#         for i,sp in enumerate(spells):
#             if sp == 0:
#                 res.append(0)
#             else:
#                 for j,pt in enumerate(potions):
#                     if pt * sp >= success:
#                         res.append(l-j)
#                         break
                
#                 # print(i, len(res))
#                 if len(res) != i+1:
#                     res.append(0)
#         return res    



class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potion_count = len(potions)
        result = []
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                result.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            result.append(potion_count - index)
        return result
        