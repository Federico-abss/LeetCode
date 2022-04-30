class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not sum(nums):
            return '0'
        
        def compare(str1: str, str2: str) -> int:
            n1 = int(str1)
            n2 = int(str2)
            if len(str2) == len(str1):
                if n1 > n2:
                    return -1
                elif n2 > n1:
                    return 1
                else:
                    return 0
            
            idx = 0
            while idx < min(len(str2), len(str1)):
                if str2[idx] > str1[idx]:
                    return 1
                elif str2[idx] < str1[idx]:
                    return -1
                idx += 1
            
            if len(str2) > len(str1):
                return compare(str1, str2[idx:])
            else:
                return compare(str1[idx:], str2)
        
        comparefunc = cmp_to_key(compare)
        return "".join(map(str, sorted(map(str, nums), key = comparefunc)))
            
            