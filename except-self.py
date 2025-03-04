import math

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cp_list=[]
        out_list=[]

        for i in range(len(nums)):
  
           cp_list.extend(nums)
           cp_list.pop(i)
           out_list.append(math.prod(cp_list))
           cp_list=[]
       
        
        result_string = out_list
        
        return result_string
        

        
x = Solution()

a1 = [-1,1,0,-3,3]

print(x.productExceptSelf(a1))
