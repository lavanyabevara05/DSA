#------pattern 11-----
# 1
# 01
# 101
# 0101
# 10101

class Solution:
  def pattern11(self,n):
    for i in range(1,n+1):
      for j in range(1,i+1):
        if(i+j)%2==0:
          print(1,end="")
        else:
          print(0,end="")
      print("")

a = Solution()
# a.pattern11(5)


#-----pattern 12 ----------
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

class Solution:
  def pattern12(self,n):
    space = 2*n-1
    for i in range(1,n+1):
      for num_1 in range(1,i+1):
        print(num_1,end="")
      for sp in range(1,space):
        print(" " ,end="")
      for num_2 in range(i,0,-1):
        print(num_2,end="")
      print("")
      space -= 2

a = Solution()
# a.pattern12(5)


#--pattern 13------

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

class Solution:
  def pattern13(self,n):
    num=1
    for i in range(n):
      for j in range(i+1):
        print(num,end=" ")
        num+=1
      print("")
a = Solution()
# a.pattern13(5)


#-----pattern 14 --------
# print(ord("A"))
# print(chr(68))
class Solution:
  def pattern14(self,n):
    for i in range(n):
      for ch in range(65,65+i+1):
        print(chr(ch),end="")
      print("")
a = Solution()
# a.pattern14(5)

#------ pattern15----------
# ABCDE
# ABCD
# ABC
# AB
# A

class Solution:
  def pattern15(self,n):
    for i in range(n):
      for ch in range(65,65+n-i):
        print(chr(ch),end="")
      print("")
a = Solution()
# a.pattern15(5)

#------pattern16-----
# A
# BB
# CCC
# DDDD
# EEEEE
# #
class Solution:
    def pattern16(self, n):
        for i in range(n):
            ch = chr(ord('A') + i)
            for j in range(i + 1):
                print(ch, end="")
            print()

a = Solution()
# a.pattern16(5)

#------pattern17---------
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
class Solution:
    def pattern17(self, n):
        for i in range(n): # for rows
          for j in range(n-i-1): # for spaces
            print(" ",end="")
          for j in range(i+1): #for Increasing letters ABC
            print(chr(ord("A")+j),end="")
          for j in range(i-1,-1,-1): # for decreasing BC
            print(chr(ord("A")+j),end="")
          print("")

a = Solution()
# a.pattern17(5)

#---------pattern18--------
# E
# DE
# CDE
# BCDE
# ABCDE

class Solution:
    def pattern18(self, n):
        for i in range(1,n+1): # for rows
          for j in range(1,i+1):
            print(chr(ord("A")+n-i),end="")
            i-=1
          for j in range(n-i):
            print(" ",end="")
          print("")

a = Solution()
# a.pattern18(5)

#------pattern19--------
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
class Solution:
    def pattern19(self, n):
      for i in range(n):
        for j  in range(n-i):
          print("*",end="")
        for j in range(2*i):
          print(" ",end= "")
        for j  in range(n-i):
          print("*",end="")
        print("")

      for i in range(n):
        for j  in range(i+1):
          print("*",end="")
        for j in range(2 * (n - i-1)):
          print(" ", end="")
        for j in range(i + 1):
          print("*", end="")
        print("")

a = Solution()
# a.pattern19(5)

#------pattern20----------
class Solution:
    def pattern20(self, n):

        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")

            for j in range(2 * (n - i)):
                print(" ", end="")

            for j in range(i):
                print("*", end="")

            print()

        for i in range(n - 1, 0, -1):

            for j in range(i):
                print("*", end="")

            for j in range(2 * (n - i)):
                print(" ", end="")

            for j in range(i):
                print("*", end="")

            print()
a = Solution()
# a.pattern20(5)

#--------pattern21--------
# In this we have to print square means only boundaaries we have to print i.e where i=0,j=0,i=n-1 and j=n-1

class Solution:
    def pattern21(self, n):
      for i in range(n):
        for j  in range(n):
          if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
          else:
            print(" ",end=" ")
        print("")

a= Solution()
# a.pattern21(10)

