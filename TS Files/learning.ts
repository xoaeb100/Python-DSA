function a1() {
  for (let i = 0; i < 1001; i++) {
    setTimeout(() => {
      console.log(i);
    }, 1000 * i); // Increase delay with each iteration
  }
}
function a2() {
  console.log("hello");
}
a1();
a2();
