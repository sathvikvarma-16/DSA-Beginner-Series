class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)] # to store the number and the original index at the same time
        # if nums = [5, 2, 6, 1] it stores [(5,0), (2,1), (6,2), (1,3)]
        ans = [0] * len(nums)
        # we use merge sort to efficiently know How many smaller elements are to the right ? as merge sort gives us two sorted halves
        """
Left  = [2,5] => sorted
Right = [1,6] => sorted
Now it's easy to count.
here 1 < 2, And because the right half is sorted, if several right elements are smaller, we can count them efficiently.
"""
    # merge sort creation - it justs divides the array
        def merge_sort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # after dividing we neeed to merge
            i = left # points to left half
            j = mid + 1 # points to right hal   f
            temp = []
            smaller = 0
            while i <= mid and j <= right:
                if arr[j][0] < arr[i][0]: # Is the right-side number smaller than the left-side number?
                    temp.append(arr[j])
                    j += 1 
                    smaller += 1 # Because we just found one smaller element on the right.
                else: # left number is smaller or equal
                    ans[arr[i][1]] += smaller 
                    temp.append(arr[i])
                    i += 1
            while i <= mid:
                ans[arr[i][1]] += smaller
                temp.append(arr[i])
                i += 1

            # Remaining right elements
            while j <= right:
                temp.append(arr[j])
                j += 1
            arr[left:right + 1] = temp
        merge_sort(0, n - 1)
        return ans
        
"""
Suppose:
LEFT  = [5]
RIGHT = [1, 2, 3, 6]
Start:
smaller = 0
Compare 5 and 1
1 < 5 ✅
Take 1.
smaller = 1
Compare 5 and 2
2 < 5 ✅
Take 2.
smaller = 2
Compare 5 and 3
3 < 5 ✅
Take 3.
smaller = 3
Now:
temp = [1,2,3]
smaller = 3
Compare 5 and 6
6 < 5 ❌
So else.
ans[arr[i][1]] += smaller
means:
answer for 5 += 3
Because:
1 < 5
2 < 5
3 < 5
So:
5 → 3
Then:
temp.append(arr[i])
gives:
temp = [1,2,3,5]  
And:
i += 1
moves to the next left element.  
"""

