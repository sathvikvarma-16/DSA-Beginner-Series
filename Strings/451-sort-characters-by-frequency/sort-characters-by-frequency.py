class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}
        for i in range(len(s)):
            freq_map[s[i]]=freq_map.get(s[i],0)+1
        sorted_chars = sorted(freq_map.items(),key=lambda x:x[1],reverse=True)
        result = ""
        for char,count in sorted_chars:
            result+=char*count
        return result
        