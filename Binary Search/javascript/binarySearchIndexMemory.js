// This is an alternative approach to binary search (index)
// that aims to save space.
// The return value will be the position of the target

function binarySearchIndex(array, target, low=0, high=array.length - 1) {
  if (low === high) {
    if (array[low] === target) {
      return low;
    } else {
      return -1;
    }
  }

  const midIdx = Math.floor((low + high) / 2);

  if (target > array[midIdx]) {
    return binarySearchIndex(array, target, midIdx+1, high);
  } else if (target < array[midIdx]) {
      return binarySearchIndex(array, target, low, midIdx);
  } else {
    return midIdx;
  }
}

// Test Cases
console.log(binarySearchIndex([1,2,3,4,5,6,7,8], 8) === 7)
console.log(binarySearchIndex([1,2,3,4,5,6,7,8], 9) === -1)
console.log(binarySearchIndex([1,2,3,4], 2) === 1)
console.log(binarySearchIndex([1], 2) === -1)
console.log(binarySearchIndex([1], 1) === 0)
console.log(binarySearchIndex([1,2,3,4,5,7], 5) === 4)