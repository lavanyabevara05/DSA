class Solution:
    def isPrime(self, n):
      count = 0
      for i in range(1,n+1):
        if (n % i == 0):
          count +=1
      if count == 2 :
        return True
      else:
        return False

obj = Solution()
x = obj.isPrime(2)
print(x)
