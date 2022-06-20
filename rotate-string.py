class Solution:
    def rotateString(self, s, goal):
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False
        

a='abcde'
goal='cdeab'
r=Solution()
print(r.rotateString(a,goal))