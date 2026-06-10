const target = 10;
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function twoSum(nums: number[], target: number): number[] {
  let prevMap = new Map();
  for (let index = 0; index < nums.length; index++) {
    const element = nums[index];
    let diff = target - element;

    if (prevMap.has(diff)) {
      return [prevMap.get(diff), index];
    } else {
      prevMap.set(element, index);
    }
  }
  return [];
}

console.log(twoSum(nums, target));
