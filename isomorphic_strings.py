class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}

        for cs, ct in zip(s, t):
            if cs in map_s_t:
                if map_s_t[cs] != ct:
                    return False
            else:
                map_s_t[cs] = ct

            if ct in map_t_s:
                if map_t_s[ct] != cs:
                    return False
            else:
                map_t_s[ct] = cs

        return True