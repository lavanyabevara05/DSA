class Solution:
  def reverseNumber(self,n): # any time func should be in camel case
      rev = 0
      while n>0:
        rem = n%10
        n= n//10
        rev = rev * 10 +  rem # rev * 10 is for place digits first rev=5,after that if we add rem = 4 it
        # gets the number 5+4 = 9 so if we multiply with it is 50 and add 4 is 54 so here 20 is used
      return rev
obj = Solution()
x=obj.reverseNumber(3476362563)
print(x)

