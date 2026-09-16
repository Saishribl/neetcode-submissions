class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                freq[s[i]] = freq.get(s[i], 0) + 1
            
            for j in range(len(t)):
                if t[j] not in freq:
                    return False
                freq[t[j]]-=1
                
            for value in freq.values():
                if value!=0:
                    return False
        return True
