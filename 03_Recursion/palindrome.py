def palindrome(arr, l, r):
    if l >= r:
        return True

    if arr[l] != arr[r]:
        return False

    return palindrome(arr, l + 1, r - 1)


arr = list(map(int, input("Enter the number: ")))

a = palindrome(arr, 0, len(arr) - 1)

if a:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
