class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return ispalindrome(left,right-1) or ispalindrome(left+1,right)
        return True
        