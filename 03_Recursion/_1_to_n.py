class Solution:
    def printNumbers(self, n):
        i= 1
        def PrintNum(i,n):
            print (i)
            if i == n:
                return
            PrintNum(i+1,n)
        PrintNum(i,n)
a = Solution ()
a.printNumbers(5)
