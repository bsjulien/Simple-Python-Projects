# li = [9,3,2,1,4,7,5,9]
#
# li.sort()
#
# print(li)
#
# # passing in another variable
#
# sli = sorted(li)
#
# # descending order
#
# slirev = sorted(li, reverse= True)
# # or
# li.sort(reverse=True)

def closestNumbers(arr):
    # sorting the array if its not sorted
    arr.sort()

    diff = []
    newarr = []
    for i in range(1, len(arr)):
        # Testing if the elements are unique
        if arr[i - 1] == arr[i]:
            return "Elements not unique"

        diff.append(arr[i] - arr[i - 1])

    sdiff = min(diff)

    # Creating a new array with elements with the smallest differences
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) == sdiff:
            newarr.append(arr[i - 1])
            newarr.append(arr[i])

    return newarr


arr = [5, 4, 3, 2, 1]
print(sorted(arr))
print(closestNumbers(arr))
