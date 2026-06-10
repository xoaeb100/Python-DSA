let arr: number[] = [3, 7, 2, 9, 5];

function maxNumber(array: number[]) {
  let maxNo = array[0];
  for (const num of array) {
    if (num > maxNo) {
      maxNo = num;
    }
  }
  return maxNo;
}

// console.log(maxNumber(arr));

// could be solved like this

//  const maxNo = arr.reduce((acc, curr) => (curr > acc ? curr : acc), arr[0]);
//   return maxNo;

function sumOfArray(array: number[]) {
  let sum = 0;
  for (const num of array) {
    sum = sum + num;
  }
  return sum;
}
// console.log(sumOfArray(arr));

// return array.reduce((a, b) => a + b, 0);

function countEvenNumbers(array: number[]) {
  let count = 0;
  for (const num of array) {
    if (num % 2 == 0) {
      count = count + 1;
    }
  }
  return count;
}

// console.log(countEvenNumbers(arr));

function reverseanArray(array: number[]) {
  //   return array.reverse();
  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    [array[left], array[right]] = [array[right], array[left]];
    left++;
    right--;
  }
  return array;
}
// console.log(reverseanArray(arr));

function minimumNumber(array: number[]) {
  const minNo = array.reduce((curr, acc) => (curr < acc ? curr : acc));
  return minNo;
}
// console.log(minimumNumber(arr));

function largestStringLength(words: string[]) {
  // return words.reduce((max, word) => {
  //   return word.length > max ? word.length : max;
  // }, 0);
  let maxLength = 0;
  for (const word of words) {
    console.info("🚀 ~ largestStringLength ~ word:", word);
    if (maxLength < word.length) {
      maxLength = word.length;
    }
  }
  return maxLength;
}

// console.log(largestStringLength(["hi", "hello", "hey"]));

function doesNumberExists(array: number[], finder: number): boolean {
  if (array.includes(finder)) {
    return true;
  } else return false;
}
// console.log(doesNumberExists([54, 7, 1, 78, 2], 1));

function sumOfFirstN(inputNumber: number) {
  let sum = 0;
  if (inputNumber <= 0) return 0;
  while (inputNumber != 0) {
    sum = sum + inputNumber;
    inputNumber--;
  }
  return sum;
}
// console.log(sumOfFirstN(5));

function reverseString(word: string) {
  let reversedString = "";
  for (let index = word.length - 1; index >= 0; index--) {
    const element = word[index];
    reversedString = reversedString + element;
  }
  return reversedString;
}
// console.log(reverseString("shoaib"));

function getFreq(array: number[]) {
  let frequencyMap = new Map<number, number>();

  for (const num of array) {
    const currentCount = frequencyMap.get(num) ?? 0;
    frequencyMap.set(num, currentCount + 1);
  }

  // Formatting the output exactly as requested
  frequencyMap.forEach((count, num) => {
    console.log(`${num} → ${count}`);
  });
}

// getFreq([1, 1, 2, 3, 3, 3]);

function secondLargest(array: number[]) {
  let maxNo = array[0];
  let secondMax = array[1];

  for (const num of array) {
    if (num > maxNo) {
      secondMax = maxNo;
      maxNo = num;
    } else if (num > secondMax && num !== maxNo) {
      secondMax = num;
    }
  }
  return secondMax;
}

// console.log(secondLargest([1, 1, 2, 3, 3, 3]));

//[1,2,4,5] → 3
function findMissingNumber(array: number[]) {
  let n = array.length + 1;

  let expectedSum = (n * (n + 1)) / 2;

  let actualSum = 0;
  for (const num of array) {
    actualSum += num;
  }

  return expectedSum - actualSum;
}

console.log(findMissingNumber([1, 2, 4, 5]));
