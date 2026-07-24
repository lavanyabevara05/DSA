class Solution:
    def factorial(self, n):
        def f(n):
            if (n<1):
                return 1
            return n * f(n-1)
        return f(n)
a = Solution()
x= a.factorial(5)
print(x)

