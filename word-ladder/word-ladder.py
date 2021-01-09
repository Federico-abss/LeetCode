class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        words = defaultdict(list)
        hmap = defaultdict(list)
        end = False
        
        wordList.append(beginWord)
        for word in wordList:                
            
            if not end:
                end = word == endWord
            for i in range(len(word)):
                    
                temp = word[:i] + '*' + word[i+1:]
                hmap[temp].append(word)
                words[word].append(temp)
                
        
        if not end:
            return 0
        
        seenInt = set()
        seenWords = set()
        dq = deque([beginWord, None])
        moves = 1
        
        while dq and (dq[0] != None or dq[-1] != None):
            
            cur = dq.popleft()
                    
            if not cur:
                moves += 1
                dq.append(None)
                continue
                    
            if cur == endWord:
                return moves
            
            for intermediate in words[cur]:
                if intermediate in seenInt:
                    continue
                
                for word in hmap[intermediate]:
