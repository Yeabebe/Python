from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        res = []

        for i in range(len(s) - 9):
            sub = s[i:i+10]
            seen[sub] += 1
            if seen[sub] == 2:   # add only once
                res.append(sub)

        return res
