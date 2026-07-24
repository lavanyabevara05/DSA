class Solution:
    def palindromeCheck(self, s):
        def palindrome(arr, l, r):
            if l >= r:
                return True
            if arr[l] != arr[r]:
                return False
            return palindrome(arr, l + 1, r - 1)
        return palindrome(s, 0, len(s) - 1)


a = Solution()
print(a.palindromeCheck("1221"))
