from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       
       tmplist = []
       output = []
       tmplist.extend(candies)
       tmplist.sort()
       
       for i in range(len(candies)):
          if candies[i] + extraCandies >= tmplist[len(tmplist)-1]:      
             output.append(True)
          else: 
             output.append(False)  
       return output

x = Solution()

candies = [2,3,5,1,3]
xtr_candies = 3

print(x.kidsWithCandies(candies,xtr_candies))
