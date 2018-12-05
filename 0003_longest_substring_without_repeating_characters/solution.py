class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexByChar = {}
        maxLen = 0
        for i, c in enumerate(s):
            if maxLen < len(indexByChar):
                maxLen = len(indexByChar)
            index = indexByChar.get(c)
            while index != None:
               indexByChar.pop(s[index])
               if index == 0:
                   index = None
               else:
                   next = indexByChar.get(s[index - 1])
                   if next != None and next < index:
                       index = next
                   else:
                       index = None
            indexByChar[c] = i
        return max(maxLen, len(indexByChar))

def test_empty():
    assert Solution().lengthOfLongestSubstring(" ") == 1

def test_abcabcbb():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test_bbbbb():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

def test_pwwkew():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3

def test_dvdf():
    assert Solution().lengthOfLongestSubstring("dvdf") == 3

def test_advdfe():
    assert Solution().lengthOfLongestSubstring("advdfe") == 4

def test_dvdf():
    assert Solution().lengthOfLongestSubstring("dvdf") == 3

def test_bpfbhmipx():
    assert Solution().lengthOfLongestSubstring("bpfbhmipx") == 7

