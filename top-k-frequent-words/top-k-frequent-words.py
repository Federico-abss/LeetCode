class Word:
    def __init__(self, word: str):
        self.word = word
        self.amount = 1
        
    def __gt__(self, other):
        return self.amount < other.amount
​
​
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
​
        result = []
        hmap = {}
        
        for word in words:
            if word in hmap:
                hmap[word].amount += 1
            else:
                hmap[word] = Word(word)
        
        values = list(hmap.values())
        heapify(values)
        
        counter = 0
        frequencies = defaultdict(list)
        while values:
            counter += 1
            
            cur = heappop(values)
            amount = cur.amount
            if counter > k:
                if amount not in frequencies:
                    break
            frequencies[cur.amount].append(cur.word)   
                
        remaining = k          
        for words in frequencies.values():
            result += sorted(words)[:remaining]
            remaining = k - len(result)
            if not remaining:            
                return result
