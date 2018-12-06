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

class Solution1():
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        indexByChar = {}
        ans = 0
        while j < len(s):
            ch = s[j]
            if ch in indexByChar:
                ans = max(ans, j - i)
                i = max(i, indexByChar[ch] + 1)
            indexByChar[ch] = j
            j += 1
        return max(ans, j - i)

def test_empty():
    assert Solution1().lengthOfLongestSubstring(" ") == 1

def test_abcabcbb():
    assert Solution1().lengthOfLongestSubstring("abcabcbb") == 3

def test_bbbbb():
    assert Solution1().lengthOfLongestSubstring("bbbbb") == 1

def test_pwwkew():
    assert Solution1().lengthOfLongestSubstring("pwwkew") == 3

def test_dvdf():
    assert Solution1().lengthOfLongestSubstring("dvdf") == 3

def test_advdfe():
    assert Solution1().lengthOfLongestSubstring("advdfe") == 4

def test_dvdf():
    assert Solution1().lengthOfLongestSubstring("dvdf") == 3

def test_bpfbhmipx():
    assert Solution1().lengthOfLongestSubstring("bpfbhmipx") == 7

