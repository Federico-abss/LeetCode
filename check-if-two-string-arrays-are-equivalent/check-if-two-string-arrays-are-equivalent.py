class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    
        iteratorCount = len(word2) - 1
        iterator = iter(word2)
        
        wordIteratorCount = len(word2[0])
        wordIterator = iter(next(iterator))
        for word in word1:
            for ch in word:
                
                if not wordIteratorCount:
                    if not iteratorCount:
                        return False
                    iteratorCount -= 1
                    temp = next(iterator)
                    wordIteratorCount = len(temp)
                    wordIterator = iter(temp)
​
                if ch != next(wordIterator):
                    return False
                
                wordIteratorCount -= 1
                                
        return wordIteratorCount == iteratorCount == 0
                
                
                
