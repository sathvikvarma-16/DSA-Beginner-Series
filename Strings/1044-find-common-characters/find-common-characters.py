class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}
        for ch in words[0]:
            freq[ch]=freq.get(ch,0)+1
        
        for i in range(1,len(words)):
            curr_freq = {}
            for ch in words[i]:
                curr_freq[ch]=curr_freq.get(ch,0)+1

            # updating mimimum frequency
            for ch in freq:
                if ch in curr_freq:
                    freq[ch]=min(freq[ch],curr_freq[ch])
                else:
                    freq[ch]=0

        # build result
        result = []
        for ch, count in freq.items():
            result.extend([ch]*count)
        return result