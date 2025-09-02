class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Use sorted word as key
            key = tuple(sorted(word))
            groups[key].append(word)

        return list(groups.values())
