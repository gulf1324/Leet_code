######################################################################################
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = []
        # 동시에 만족하는 경우까지만 append
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i +=1
            j +=1
        
        # pointer가 남아있으면
        #   남은 word의 pointer 오른쪽 부분을 전부 append
        if i < len(word1):
            result.append(word1[i:])
        if j < len(word2):
            result.append(word2[j:])

        return ''.join(result)
######################################################################################
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # zip을 사용해서 동시에 join
        merged = ''.join(a + b for a, b in zip(word1, word2))
        # 남은 str을 오른쪽에 더하기
        return merged + word1[len(word2):] + word2[len(word1):]
######################################################################################
class Solution3:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return ''.join(result)
######################################################################################

# merge = Solution()
# a = merge.mergeAlternately("abcd","pqr")
# print(a)
# apbqcrd

merge = Solution2()
a = merge.mergeAlternately("ab","pqr")
print(a)
# apbqr