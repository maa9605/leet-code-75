class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        My solution
        '''
        slist = s.split()
        rev_list = s.split()
        
        for i in range(len(slist)):
           rev_list[i] = slist[(len(slist)-1)-i].strip()
           
        
        #result_string = rev_list

        result_string = ' '.join(rev_list)
        
        return result_string
        
        '''
        Better Solution
        
        words = s.split()
        return ' '.join(reversed(words))
        '''
        
x = Solution()

s1 = "a good   example"

print(x.reverseWords(s1))
