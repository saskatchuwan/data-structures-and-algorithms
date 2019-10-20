import math

def binary_search(array, target):
  if len(array) == 1 and array[0] == target:
    return 0
  if len(array) == 1 and array[0] != target:
    return None
  
  mid_index = math.floor(len(array) / 2)
  left = array[0:mid_index]
  right = array[mid_index:]

  if target == array[mid_index]:
    return mid_index
  elif target < array[mid_index]:
    return binary_search(left, target)
  else: #target > array[mid_index]
    result = binary_search(right, target)

    if result == None:
      return None
    else:
      return result + mid_index
        # don't add a 1 here because we include the pivot in the right array
        # would need to add an extra 1 if we instead included the pivot in the left array


# Test cases
print(binary_search([1,2,3,4,5,6,7,8], 8) == 7)
print(binary_search([1,2,3,4,5,6,7,8], 9) == None)
print(binary_search([1,2,3,4], 2) == 1)
print(binary_search([1], 2) == None)
print(binary_search([1], 1) == 0)
print(binary_search([1,2,3,4,5,7], 5) == 4)