#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # Write your code here
    arr.sort()
    size = len(arr)
    # odd
    if size % 2 != 0:
        median_index = int((size - 1) / 2)
        return arr[median_index]
    # even
    else:
        a = len(arr)/2
        b = a - 1
        return (arr[a] + arr[b]) / 2