# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.
# two sum problem
# method1- two pointer solution

# TC=O(nlogn)
# SC=O(n) or O(1) depending on the sorting used


# def two_sum(arr, sum):
#     # sort the array
#     arr.sort()
#     n = len(arr)
#     left = 0
#     right = n - 1
#     while (left < right):
#         if (arr[left] + arr[right]) == sum:
#             return True
#         elif (arr[left] + arr[right]) > sum:
#             right -= 1
#
#         else:
#             left += 1
#     return False
#
#
# arr = [4, 7, 1, -3, 2]
# sum = 5
# print(two_sum(arr, sum))


# method 2 -by hashing(best method)
# TC=O(n) to traverse the array once
# SC=O(n) to store in hash-map
def two_sum(arr,sum):
    #create an empty hash set
    s=set()
    n=len(arr)
    for i in range(n):
        req = sum-arr[i]
        if req in s:
            return True
        else:
            s.add(arr[i])
    return False


arr = [4, 7, 6, -3, 2]
sum = 5
print(two_sum(arr, sum))

