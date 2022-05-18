class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedStrs = defaultdict(list)
        
        for string in strs:
            sortedStr = "".join(sorted(string))
            sortedStrs[sortedStr].append(string)
            
        return sortedStrs.values()
        
        