# "uau", "ssx"
# >>> False
# "aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"
# >>> False
##################################################################
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dic = {}
        word2_dic = {}
        for i in word1:
            word1_dic[i] = word1_dic.get(i, 0) +1
        for i in word2:
            word2_dic[i] = word2_dic.get(i, 0) +1
        # print(set(word1_dic), set(word2_dic))
        # print(word1_dic.values(), word2_dic.values())
        return (
            set(word1_dic)==set(word2_dic) and 
        sorted(word1_dic.values())==sorted(word2_dic.values())
        )
##################################################################        
# In order to be close, 2 strings must have:
# same original chars
# same frequency
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1, s2 = set(word1), set(word2)
        if s1 != s2: 
            return False
        freq1 = sorted(word1.count(char) for char in s1)
        freq2 = sorted(word2.count(char) for char in s2)        
        # print(freq1, freq2)
        return freq1 == freq2
##################################################################
# from collections import Counter
# already imported in Leet code's runtime environment
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return sorted(freq1.values()) == sorted(freq2.values())
##################################################################    
s = Solution()
print(s.closeStrings("abc","bca"))