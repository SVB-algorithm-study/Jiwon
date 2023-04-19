#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    q, r = divmod(len(arr), 2)
    # if the length of the array is even
    if r == 0:
        return (arr[q] + arr[q - 1]) // 2
    # else - the length of the array is odd
    else:
        return arr[q]
