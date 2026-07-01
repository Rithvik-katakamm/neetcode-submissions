class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #define the pointers (2 pointer)
        left = 0
        right = len(s) - 1 

        #loop though list using while, time: O(n), space: O(n)
        #s=["n","e","e","t"]

        while left < right:
            #classic pythonian swap
            s[left], s[right] = s[right], s[left]

            #increase left to next index, decrease right to next index
            left += 1
            right -= 1




        


        