class Solution:
    def strStr(self, haystack: str, needle: str) -> int:   
        idx = 0
        needleIdx = 0
        
        while idx <= len(haystack) - len(needle):
            
            while haystack[idx + needleIdx] == needle[needleIdx]:
                needleIdx += 1
                if needleIdx == len(needle):
                    return idx
            else:
                needleIdx = 0
            
            idx += 1
                
        return -1
            