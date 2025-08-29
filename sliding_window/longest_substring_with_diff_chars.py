class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        n = len(s)
        sett = set()
        max_size = 0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            curr_size = (r-l) + 1
            max_size = max(curr_size, max_size)
            sett.add(s[r])
        return max_size
