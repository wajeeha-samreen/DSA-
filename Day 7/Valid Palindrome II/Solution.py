class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        count = 0
                    
        def isPalindrome(l, r, count):
            if count > 1:
                return False
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                if s[l] != s[r]:
                    if s[l+1] != s[r] and s[l] != s[r-1]:
                        return False
                    return isPalindrome(l+1, r, count+1) or isPalindrome(l, r-1, count+1)
					
            return True
        
        return isPalindrome(l, r, count)
