// print(twoSum([2,7,11,15],9))
console.log(twoSumWithMap([2, 7, 11, 15], 17));
function twoSum(arrayOfNumbers: number[], totalSum: number) {
  for (let i = 0; i < arrayOfNumbers.length - 1; i++) {
    for (let j = i + 1; j < arrayOfNumbers.length; j++) {
      if (arrayOfNumbers[i] + arrayOfNumbers[j] === totalSum) {
        console.info("🚀 ~ twoSum ~ arrayOfNumbers[i] :", arrayOfNumbers[i]);

        console.info("🚀 ~ twoSum ~ arrayOfNumbers[j] :", arrayOfNumbers[j]);
      }
    }
  }
}

function twoSumWithMap(arrayOfNumbers: number[], totalSum: number) {
  const myMap = new Map<number, number>();
  let complement = 0;
  for (let i = 0; i < arrayOfNumbers.length; i++) {
    complement = totalSum - arrayOfNumbers[i];

    if (myMap.has(complement)) {
      return [myMap.get(complement)!, i];
    } else {
      myMap.set(arrayOfNumbers[i], i);
    }
  }
}
