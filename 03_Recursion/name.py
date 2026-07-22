# def function(parameters):

#     # 1. Base case
#     if stopping_condition:
#         return

#     # 2. Work to do
#     ...

#     # 3. Recursive call
#     function(updated_parameters)

def name(n):
  if (n == 0):
    return
  print("Lav")
  name( n-1)

name(5)

# time complexity = O(n)
# stack space = O(n)
# f(1,5)
# |
# |
# f(2,5)
# |
# |
# f(3,5)
# |
# |
# f(4,5)
# |
# |
# f(5,5)
# |
# |
# f(6,5)
# |
# |
# Return
