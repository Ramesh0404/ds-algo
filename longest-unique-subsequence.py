class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=0
        max_length=0
        unique_char=set()
        while end<len(s):
            if s[end] not in unique_char:
                unique_char.add(s[end])
                end+=1
                max_length = max(max_length,len(unique_char))
            else:
                unique_char.remove(s[start])
                start+=1
        return max_length
                
str = "bbbbbbb"
r=Solution()
print(r.lengthOfLongestSubstring(str))