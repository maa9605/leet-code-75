class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        '''
        This is the solution that Leetcode accepted.  The issue is with the problem description in which they reference a 
        consecutive subset {i,j,k}, but then are really looking for a subset of any three number and idices
        If you encounter in a interview check with the interviewer if it is a "consecutive" subset
        '''
        first = second = float('inf')
       
        for n in nums:
          if n <= first:
             first = n
          elif n <= second:
             second = n
          else:
             return True
        
        return False
              
        
        '''
        for i in range(len(nums)): 
           if i < len(nums)-2:
              if nums[i]<nums[i+1]<nums[i+2]:
                 return True
                 i+=2

        return False
        '''
x = Solution()

z = [20,100,10,12,5,13]

print(x.increasingTriplet(z))
