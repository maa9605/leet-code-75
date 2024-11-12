class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed)-1): 
           if sum(flowerbed[i-1:i+2])==0 and n!=0:
              flowerbed[i] = 1
              n -= 1             
           
           if n == 0: 
              return True 
        
        return n<=0
        
x = Solution()

z = [1,0,0,0,1]
n = 1

print(x.canPlaceFlowers(z,n))
