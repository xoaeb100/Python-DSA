function memoize(fn: (n: number) => number) {
    const cache: Record<number, number> = {};

    return function (n: number): number {
        if (n in cache) {
            console.log("Fetching from cache:", n);
            return cache[n];
        }
        console.log("Computing for", n);
        cache[n] = fn(n);
        return cache[n];
    };
}

// Function to be memoized
const square = (n: number) => n * n;

// Create a memoized version of `square`
const memoizedSquare = memoize(square);


console.time('first')
console.log(memoizedSquare(5)); // Computing for 5 → 25
console.timeEnd('first')

console.time('secondf')
console.log(memoizedSquare(5)); // Fetching from cache → 25
console.timeEnd('secondf')

console.time('third')
console.log(memoizedSquare(10)); // Computing for 10 → 100
console.timeEnd('third')


console.time('fourth')
console.log(memoizedSquare(10)); // Fetching from cache → 100
console.timeEnd('fourth')
