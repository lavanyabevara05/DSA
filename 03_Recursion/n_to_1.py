def function(n):
  if(n==0):
    return
  print(n)
  function(n-1)
a= int(input("Enter the number:"))
function(a)

