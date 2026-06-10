function removeDups(nums) {
  if (nums.length === 0) {
    return 0;
  }

  let k = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[k - 1]) {
      nums[k] = nums[i];
      k++;
    }
  }

  return k;
}

// Example usage:
const nums = [1, 1, 2, 2, 3, 4, 4];
const newLength = removeDups(nums);
console.log(`New length: ${newLength}`);
