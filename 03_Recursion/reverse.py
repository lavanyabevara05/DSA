class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def f(arr, l, r):
            if l >= r:
                return
            arr[l], arr[r] = arr[r], arr[l]
            f(arr, l + 1, r - 1)
        f(arr, 0, n - 1)


a = Solution()
arr = [1, 2, 3, 4, 5]
a.reverse(arr, 5)
print(arr)
