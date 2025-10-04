"""

11. Container With Most Water

Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



"""

class Solution:

    def maxArea(self, height: List[int]) -> int:
        res = 0
        start = 0
        end = len(height)-1
        while(start < end):
            h = min(height[start],height[end])
            w = end - start
            print(start,end,h,res)
            res = max(res,h*w)
            if height[start] < height[end]:
                start +=1
            else:
                end -=1
        return res
        

            
        