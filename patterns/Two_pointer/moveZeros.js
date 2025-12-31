// Move all zeros to the end of the array while maintaining order of non-zero elements.
// pattern:write pointer

function moveZeroes(nums) {
  let insertPos = 0;

  for (let num of nums) {
    if (num !== 0) {
      nums[insertPos++] = num;
    }
  }

  while (insertPos < nums.length) {
    nums[insertPos++] = 0;
  }
}
