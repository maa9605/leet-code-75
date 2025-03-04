class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]
            print(prefix)
            
        print(res)
        postfix = 1
        for i in range(len(nums)-1 , -1  , -1):
            print(i)
            res[i]*=postfix
            postfix*=nums[i]
            print(postfix)
            print(res)

        return res 
        
x = Solution()

a1 = [1,2,3,4]

print(x.productExceptSelf(a1))
