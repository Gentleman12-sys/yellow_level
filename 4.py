class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        g = [0]
        for i in range(len(s)):
            a = []
            for j in s[i::]:
                if j not in a:
                    a.append(j)
                else:
                    break
            g.append(len(a))
        return max(g)
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))