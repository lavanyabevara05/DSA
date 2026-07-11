class Solution:
    def divisors(self, n):
      div = []
      for i in range(1,n+1):
        if (n % i == 0):
            div . append(i)
      return div

obj = Solution()
x = obj.divisors(12)
print(x)
