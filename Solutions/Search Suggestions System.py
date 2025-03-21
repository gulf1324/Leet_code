###############################################################################################
# 1st attempt, correct
class Solution:
    def searchWord_update(self, word, input: str) -> str:
        word += input
        return word
    
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        word = ''
        res = []
        products.sort()
        for char in searchWord:
            word = self.searchWord_update(word, char)
            tmp_list = []
            
            for product in products:
                if product.startswith(word):
                    if len(tmp_list) ==3:
                        break
                    tmp_list.append(product)
            res.append(tmp_list)
        return res
###############################################################################################
# more efficient
class Solution2:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        word = ''
        res = []
        products.sort()
        for char in searchWord:
            word += char
            tmp_list = []
            
            for product in products:
                if product.startswith(word):
                    if len(tmp_list) ==3:
                        break
                    tmp_list.append(product)
            res.append(tmp_list)
        return res
###############################################################################################    
# most efficient
"""
bisect.bisect_left(A, x) does one of two things:
=> bisect_left(list, element, starting index)

1. If x is in A, it returns the index of the first occurrence (leftmost position).
2. If x is not in A, it returns the index where x should be inserted while maintaining order
"""
import bisect
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        word = ''
        res = []
        i = 0
        products.sort()
        for char in searchWord:
            word += char
            i = bisect.bisect_left(products, word, i)
            res.append([product for product in products[i:i+3] if product.startswith(word)])
        return res
###############################################################################################    
s = Solution()
print(s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], 
                          searchWord = "mouse"))