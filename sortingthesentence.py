class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        t = [''] * len(s)
        for i in s:
            t[int(i[-1]) - 1] = i[:len(i) - 1]
        return ' '.join(t)
