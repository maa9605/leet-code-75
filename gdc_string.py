from math import gcd 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
            
	#gcd function
        gcd_length = gcd(len(str1), len(str2))
        print(gcd_length)

        return str1[:gcd_length]  

x = Solution()

print(x.gcdOfStrings("ABAB", "ABABABAB"))
