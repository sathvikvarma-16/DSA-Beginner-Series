class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        ans=[]*len(nums)
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        e = 0
        o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(even[e])
                e += 1
            else:
                ans.append(odd[o])
                o += 1
        return ans