class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        nums = []
        arr.sort()
        n = len(arr)

        for i in range(n - 2):

            if i > 0 and arr[i] == arr[i - 1]:
                continue

            low = i + 1
            high = n - 1
            target = -arr[i]

            while low < high:
                s = arr[low] + arr[high]

                if s == target:
                    nums.append([arr[i], arr[low], arr[high]])

                    low += 1
                    high -= 1

                    while low < high and arr[low] == arr[low - 1]:
                        low += 1

                    while low < high and arr[high] == arr[high + 1]:
                        high -= 1

                elif s > target:
                    high -= 1

                else:
                    low += 1

        return nums