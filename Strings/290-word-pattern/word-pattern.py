class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1 = list(pattern)
        list2 = s.split()
        len1 = len(list1)
        len2 = len(list2)
        if len1!=len2:
            return False
        map_s_t = {}
        map_t_s = {}
        for i in range(len(list1)):
            c1=list1[i]
            c2=list2[i]
            if ((c1 in map_s_t and map_s_t[c1]!=c2) or (c2 in map_t_s and map_t_s[c2]!=c1)):
                return False
            map_s_t[c1]=c2
            map_t_s[c2]=c1
        return True