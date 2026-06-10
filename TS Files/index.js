// const add = require("./sum");

// const summarion = add(3, 6);
// console.log(summarion);

// (function greet(name) {
//   console.log("Hellow", name);
// })("shoaib");

// const mySuperHEro = require("./superhero");

// console.log(mySuperHEro.getName());

// mySuperHEro.setName("Ironman");
// console.log(mySuperHEro.getName());

class Animal {
  constructor(name) {
    this.name = name;
  }

  makeSound() {
    console.log(`${this.name} is making a sound.`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Calls the parent class's constructor
    this.breed = breed;
  }

  makeSound() {
    super.makeSound(); // Calls the parent class's makeSound method
    console.log(`${this.name} is barking.`);
  }
}

const myDog = new Dog("Buddy", "Golden Retriever");
myDog.makeSound();
