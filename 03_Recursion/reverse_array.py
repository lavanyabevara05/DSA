def reverse(a,l,r):
  if(l>=r):
    return
  a[l],a[r] = a[r],a[l]
  reverse(a , l+1,r-1)

arr = [1,2,3,4,5]

reverse(arr,0,len(arr)-1)
print(arr)

## Another way

def f(arr, i , n ):
  if (i>=n/2):
    return
  arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

  f(arr , i+1 , n)

arr = [1,2,3,4,5]
f( arr, 0 , len(arr))
print(arr)



