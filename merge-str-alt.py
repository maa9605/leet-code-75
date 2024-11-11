import itertools

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_list=list(word1)
        word2_list=list(word2)
        
        padded_lists = list(itertools.zip_longest(word1_list, word2_list, fillvalue=''))
        list1, list2 = zip(*padded_lists)
        
        list_out=[]
        for i in range(len(list1)):
           list_out.append(list1[i])
           list_out.append(list2[i])
                
        result_string = ''.join(list_out)
        
        return result_string


x = Solution()
print(x.mergeAlternately('abc','xyz'))


        
        
