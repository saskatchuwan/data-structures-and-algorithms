# This is an alternative approach to binary search (index)
# that aims to save space.
# The return value will be the position of the target

import math

def binary_search_index(array, target, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low == high:
    if array[low] == target:
      return low
    else:
      return None
  
  mid_index = math.floor((low + high) / 2)

  if target > array[mid_index]:
    return binary_search_index(array, target, mid_index + 1, high)
  elif target < array[mid_index]:
    return binary_search_index(array, target, low, mid_index)
  else:
    return mid_index

# Test cases
print(binary_search_index([1,2,3,4,5,6,7,8], 8) == 7)
print(binary_search_index([1,2,3,4,5,6,7,8], 9) == None)
print(binary_search_index([1,2,3,4], 2) == 1)
print(binary_search_index([1], 2) == None)
print(binary_search_index([1], 1) == 0)
print(binary_search_index([1,2,3,4,5,7], 5) == 4)