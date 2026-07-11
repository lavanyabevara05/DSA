class Solution:
    def armStrongNumber(self, n):
        original = n
        length = len(str(n))
        num = 0

        while n > 0:
            rem = n % 10
            num += rem ** length
            n //= 10

        # return original == num


        if (original == num):
          return True
        else:
          return False


obj = Solution()
x= obj.armStrongNumber(153)
print(x)
