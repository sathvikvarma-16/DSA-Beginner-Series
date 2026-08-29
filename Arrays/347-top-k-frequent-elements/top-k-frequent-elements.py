class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = {}
        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # Sort by frequency
        arr = sorted(freq, key=freq.get, reverse=True)
        # Take first k elements
        for i in range(k):
            result.append(arr[i])
        return result
           