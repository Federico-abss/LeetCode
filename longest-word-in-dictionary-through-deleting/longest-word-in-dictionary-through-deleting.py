class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:            
        
        hmap = defaultdict(list)
        longest = ""
        
        for i,ch in enumerate(s):
            hmap[ch].append(i)
            
        for word in d:
            if len(word) < len(longest): continue
            current = -1
            for ch in word:
                if ch not in hmap:
                    break
                    
                for idx in hmap[ch]:
                    if idx > current:
                        current = idx
                        break
                else:
                    break
                    
            else:
                if len(word) > len(longest):
                    longest = word
                else:
                    longest = word if word < longest else longest 
                
        return longest
        
            