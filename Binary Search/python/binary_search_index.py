# This is the original approach to binary search (index)
# The return value will be the position of the target

import math

def binary_search_index(array, target):
  if len(array) == 0:
    return None
  
  mid_index = math.floor(len(array) / 2)
  left = array[0:mid_index]
  right = array[mid_index+1:]

  if target == array[mid_index]:
    return mid_index
  elif target < array[mid_index]:
    return binary_search_index(left, target)
  else: #target > array[mid_index]
    result = binary_search_index(right, target)

    if result == None:
      return None
    else:
      return result + mid_index + 1

# Test cases
print(binary_search_index([1,2,3,4,5,6,7,8], 8) == 7)
print(binary_search_index([1,2,3,4,5,6,7,8], 9) == None)
print(binary_search_index([1,2,3,4], 2) == 1)
print(binary_search_index([1], 2) == None)
print(binary_search_index([1], 1) == 0)
print(binary_search_index([1,2,3,4,5,7], 5) == 4)