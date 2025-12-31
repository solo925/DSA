// Given a sorted array, return a new array of squares in sorted order.
//patern:compare extremes

function sortedSquares(nums) {
  let left = 0;
  let right = nums.length - 1;
  const result = new Array(nums.length);
  let pos = nums.length - 1;

  while (left <= right) {
    if (Math.abs(nums[left]) > Math.abs(nums[right])) {
      result[pos--] = nums[left] ** 2;
      left++;
    } else {
      result[pos--] = nums[right] ** 2;
      right--;
    }
  }

  return result;
}
