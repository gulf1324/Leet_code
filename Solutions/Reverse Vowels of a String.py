class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        # store  index, vowel
        index = []
        vowel = []
        for i, v in enumerate(s):
            if v.lower() in vowels:
                index.append(i)
                vowel.append(v)
        # reverse index
        index = index[::-1]
        s_list = list(s)
        
        # assign vowel with reversed index
        for reverse_i, v in zip(index, vowel):
            s_list[reverse_i] = v

        return "".join(s_list)

                

aa = Solution()
print(aa.reverseVowels("IceCreAm"))