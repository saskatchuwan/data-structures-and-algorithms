# This algorithm will return a boolean value indicating
# whether the target is within the array

import math

def binary_search(array, target):
  if len(array) == 0:
    return False
  
  mid_index = math.floor(len(array) / 2)
  left = array[0:mid_index]
  right = array[mid_index+1:]

  if target > array[mid_index]:
    return binary_search(right, target)
  elif target < array[mid_index]:
    return binary_search(left, target)
  else:
    return True
    
# Test cases
print(binary_search([1,2,3,4,5,6,7,8], 8) == True)
print(binary_search([1,2,3,4,5,6,7,8], 9) == False)
print(binary_search([1,2,3,4], 2) == True)
print(binary_search([1], 2) == False)
print(binary_search([1], 1) == True)
print(binary_search([1,2,3,4,5,7], 5) == True)