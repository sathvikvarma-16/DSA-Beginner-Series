class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s_t = {}
        map_t_s = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if ((c1 in map_s_t and map_s_t[c1]!=c2) or (c2 in map_t_s and map_t_s[c2]!=c1)):
                return False
            map_s_t[c1]=c2
            map_t_s[c2]=c1
        return True 
            