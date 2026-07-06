from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        longest = 0

        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])

        return longest