// Determine if any three numbers add up to a target.
// pattern: fixone + two pointers

function threeSumExists(nums, target) {
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === target) return true;
      if (sum < target) left++;
      else right--;
    }
  }

  return false;
}
