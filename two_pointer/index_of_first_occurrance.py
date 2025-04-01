class Solution(object):
    def strStr(self, haystack, needle): # Time complexity O(N) - Temporal Complexity O(1)
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        left = 0
        str_size = len(needle)

        while left <= len(haystack) - 1:
            if haystack[left: (left + str_size)] == needle:
                return left
            elif haystack[0] == needle:
                return 0
            else:
                left += 1
        return -1
