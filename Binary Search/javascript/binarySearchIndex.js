// This is the original approach to binary search (index)
// The return value will be the position of the target

function binarySearchIndex(array, target) {
  if (array.length === 0) return -1;

  const midIdx = Math.floor(array.length / 2);
  const left = array.slice(0, midIdx);
  const right = array.slice(midIdx + 1);

  if (target === array[midIdx]) {
      return midIdx;
  } else if (target < array[midIdx]) {
      return binarySearchIndex(left, target);
  } else {
      const result = binarySearchIndex(right, target);

      if (result === -1) {
          return -1;
      } else {
          return result + midIdx + 1;
      }
  }
}

// Test Cases
console.log(binarySearchIndex([1,2,3,4,5,6,7,8], 8) === 7)
console.log(binarySearchIndex([1,2,3,4,5,6,7,8], 9) === -1)
console.log(binarySearchIndex([1,2,3,4], 2) === 1)
console.log(binarySearchIndex([1], 2) === -1)
console.log(binarySearchIndex([1], 1) === 0)
console.log(binarySearchIndex([1,2,3,4,5,7], 5) === 4)