class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=""
        for x in s:
            if x.isalnum():
                clean+=x.lower()
        rev_clean=clean[::-1] #reverse 

        return clean == rev_clean