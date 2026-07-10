class Solution:
  def countDigit(self,n):

    count = 0
    while n>0:
      n=n//10
      count += 1
    return count

obj = Solution()
ans = obj.countDigit(int(input("Enter the number: ")))
print(ans)
