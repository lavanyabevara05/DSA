class Solution:
    def printNumbers(self, n):
        # Your code goes here
        def f(i,n):
            print(n)
            if(n==i):
                return
            f(i,n-1)
        f(1,5)
a = Solution ()
a.printNumbers(5)

