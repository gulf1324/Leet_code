##################################################################
# Time limit exceeded
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e","i","o","u"]
        num_vowels_max = 0
        for i in range(len(s)-k+1):
            current_window = s[i:i+k]
            num_vowels = 0
            for char in current_window:
                if char in vowels:
                    num_vowels += 1
                num_vowels_max = max(num_vowels_max,num_vowels)
        return num_vowels_max
##################################################################
# Answer
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # vowels =  {'a', 'e', 'i', 'o', 'u'}
        vowels = "aeiou"
        current_window = s[:k]
        num_vowels = 0
        for char in current_window:
            if char in vowels:
                num_vowels += 1
        num_vowels_max = num_vowels
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                num_vowels +=1
            if s[i-k] in vowels:
                num_vowels -=1
            num_vowels_max = max(num_vowels_max, num_vowels)

        return num_vowels_max
##################################################################
# More Comprehensive (similar speed)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        num_vowels = sum(s[i] in vowels for i in range(k))
        num_vowels_max = num_vowels
        
        for i in range(k, len(s)):
            num_vowels += (s[i] in vowels) - (s[i-k] in vowels)
            num_vowels_max = max(num_vowels_max, num_vowels)

        return num_vowels_max
##################################################################
s = Solution()
print(s.maxVowels(s = "abciiidef", k = 3))


##################################################################
# performance test for ```in``` operation
# hash vs string (O(1) vs O(n))

import timeit

# Generate large datasets
large_string = ''.join(chr(i % 256) for i in range(10**7))  # 10 million characters
large_set = set(large_string)  # Unique characters from the string

# Test membership for a character that exists and one that doesn't
str_test = """
'x' in large_string
"""
set_test = """
'x' in large_set
"""

# Timing the two operations
time_str = timeit.timeit(str_test, globals=globals(), number=100000)
time_set = timeit.timeit(set_test, globals=globals(), number=100000)

# Print results
print("String Lookup Time:", time_str)
print("Set Lookup Time:", time_set)
print("Difference (Set - String):", time_set - time_str)

# String Lookup Time: 0.010848599999917496
# Set Lookup Time: 0.012067499999830034
# Difference (Set - String): 0.0012188999999125372