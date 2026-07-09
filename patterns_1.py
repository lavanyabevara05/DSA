# -----------------------
# Pattern 1
# ****
# ****
# ****
# ****

n = int(input(" "))
for i in range(n):
  for j in range(n):
    print("*" , end = "")
  print( "" )

# ---------------------

# pattern 2

# *
# **
# ***
# ****
# *****
# ******


n= int(input(" "))
for i in range(n):
  for j in range(i+1):
    print("*" , end = "")
  print( "" )


#------------------
#pattern 3

n= int(input(" "))
# i=1
# j=1 # you dont need this for loop automatically assign i,j = 0
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j , end = "")
  print( "" )

#  # two gives same output

for i in range(n):
  for j in range(i+1):
    print(j+1 , end = "")
  print( "" )

#-----------------------
#pattern 4
# 1
# 22
# 333
# 4444
# 55555


n= int(input(""))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(i,end="")
  print("")

#------------------
# pattern 5

# *****
# ****
# ***
# **
# *

n= int(input(""))
for i in range(n):
  for j in range(n-i):
    print("*",end="")
  print("")

#----------------
#pattern 6
# 12345
# 1234
# 123
# 12
# 1

n= int(input(""))
for i in range(n):
  for j in range(n-i):
    print(j+1,end="")
  print("")

#--------------
#pattern 7

#     *
#    ***
#   *****
#  *******
# *********

class Solution:
    def pattern7(self, n):
        for i in range(n):
            for sp_1 in range(n-i-1):
                print(" ",end="")  #You want to print spaces, not new lines.
            for star in range(2*i+1):
                print("*", end="")
            for sp_2 in range(n-i-1):
                print(" ",end="")
            print("")

a=Solution()
# a.pattern7(5)


#--------------------------
#pattern8
# *********
#  *******
#   *****
#    ***
#     *



class Solution:
    def pattern8(self, n):
        for i in range(n):
            for sp_1 in range(i):
                print(" ",end="")  #You want to print spaces, not new lines.
            for star in range(2*n-(2*i+1)):
                print("*", end="")
            for sp_2 in range(i):
                print(" ",end="")
            print("")

a=Solution()
# a.pattern8(5)

class Solution:
    def pattern9(self, n):
        for i in range(n):
            for sp_1 in range(n-i-1):
                print(" ",end="")  #You want to print spaces, not new lines.
            for star in range(2*i+1):
                print("*", end="")
            for sp_2 in range(n-i-1):
                print(" ",end="")
            print("")

        for i in range(n):
            for sp_1 in range(i):
                print(" ",end="")  #You want to print spaces, not new lines.
            for star in range(2*n-(2*i+1)):
                print("*", end="")
            for sp_2 in range(i):
                print(" ",end="")
            print("")

a=Solution()
# a.pattern9(5)

class Solution:
    def pattern10(self,n):

        for i in range(n):
            for star in range(i+1):
                print("*",end="")
            for space in range(n-i-1):
                print("",end="")
            print("")
        for i in range(n):
            for star in range(n-i-1):
                print("*",end="")
            for space in range(i+1):
                print("",end="")
            print("")

a= Solution()
a.pattern10(5)
