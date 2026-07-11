class Solution:
  def isPalindrome(self,n):
      original = n
      rev = 0
      count = 0
      while n>0:
        rem = n%10
        n= n//10
        rev = rev * 10 +  rem
      if original == rev:
        return "Its a palindrome Number"
      else:
        return "Its not a palindrome Number"

obj = Solution()
x=obj.isPalindrome(12321)
print(x)
