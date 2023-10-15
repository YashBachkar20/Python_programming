# A Python3 program to find a peak element

# Find the peak element in the array
def findPeak(arr, n) :

	# first or last element is peak element
  if (n == 1) :
    return 0
  if (n== 2):
    if (arr[0]>=arr[1]):
        return 0
    else:
      return 1
  else:
    for i in range(1,n):
    #   print("arr[i-1]", arr[i-1])
    #   print("arr[i]", arr[i])
    #   print("arr[i+1]", arr[i+1])

      if (arr[i]>= arr[i-1]) and (arr[i]>=arr[i+1]):
        return i
     	
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))

# This code is contributed by divyeshrabadiya07
