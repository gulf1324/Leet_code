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
        
        # pointer 가 남아있으면
        #   남은 word의 pointer 오른쪽 부분을 전부 append
        if i < len(word1):
            result.append(word1[i:])
        if j < len(word2):
            result.append(word2[j:])

        return ''.join(result)
    
merge = Solution()

a = merge.mergeAlternately("abcd","pqr")
print(a)
# apbqcrd
