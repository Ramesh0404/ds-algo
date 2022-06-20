class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])


s='a good   example'
r=Solution()
print(r.reverseWords(s))
