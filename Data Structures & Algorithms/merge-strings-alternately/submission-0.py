class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        low1 = 0
        low2 = 0
        while low1 < len(word1) and low2 < len(word2):
            s+=word1[low1]
            low1+=1
            s+=word2[low2]
            low2+=1

        while low1 < len(word1):
            s+=word1[low1]
            low1+=1
        
        while low2 < len(word2):
            s+=word2[low2]
            low2+=1

        return s

