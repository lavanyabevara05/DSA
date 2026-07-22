# class  Solution():
#   def printnum(self,i,n):
#     def printnumm(i,n):
#       if(i<1):
#         return
#       printnumm(i-1,n)
#       print(i)
# obj = Solution()
# x = obj.printnum(3,3)
# print(x)

def printnumm(i,n):
      if(i<1):
        return
      printnumm(i-1,n)
      print(i)
printnumm(5,5)
