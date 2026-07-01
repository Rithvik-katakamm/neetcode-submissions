class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lets use the 2 pointer approuch
        # init 2 pointer
        p1 = 0 
        p2 = len(s) - 1 
        # loop through s while p1 < p2
        # example 'aba'
        while p1 < p2: #(why not p1 <= p2?)
            # lets increment p1 as long as it is not alphanumerical
            while p1 < p2 and not self.isalphanum(s[p1]):
                p1 += 1
            # lets decrement p2 as long as it is not alphanumerical
            while p1 < p2 and not self.isalphanum(s[p2]):
                p2 -= 1
            # compare both chars the pointers point to, return false if not same
            if s[p1].lower() != s[p2].lower():
                return False
            # move the points inward
            p1 += 1
            p2 -= 1
        # return ture if we make it out
        return True 

    def isalphanum(self, char):
        return (ord('a') <= ord(char) <= ord('z') or 
                ord('A') <= ord(char) <= ord('Z') or 
                ord('0') <= ord(char) <= ord('9'))