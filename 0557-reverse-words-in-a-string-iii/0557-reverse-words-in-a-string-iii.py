class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        ans = []

        for word in words:
            ans.append(word[::-1])

        return " ".join(ans)