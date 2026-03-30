class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        clean = ''.join(ch for ch in s if ch.isalnum())
        n = len(clean)
        i = 0
        j = n-1
        while i <= j:
            if clean[i] == clean[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        