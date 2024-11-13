class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"A","E","I","O","U"}
        slist = list(s)
        start = 0
        end = len(slist) - 1

        while start < end:
           if slist[start].upper() not in vowels:
              start += 1
              continue
              
           if slist[end].upper() not in vowels:
              end -= 1
              continue
        
           slist[start], slist[end] = slist[end], slist[start]
           start += 1
           end -= 1

        result_string = ''.join(slist)
        
        return result_string
        
x = Solution()

s1 = "leetcode"

print(x.reverseVowels(s1))
