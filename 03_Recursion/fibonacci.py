# By adding before 2 numbers we get the next number
def fib(n):
  if(n<=1):
    return n
  return fib(n-2)+fib(n-1)
x = fib(5)
print(x)

