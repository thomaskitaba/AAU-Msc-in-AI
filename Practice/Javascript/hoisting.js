#!/usr/bin/node

// Note
// Normal functions and var will be hosted
// Hoisting var  will result in undefined but it can be hoisted
console.log(a)
var a = 2

// Hoising function 

console.log(hello("  Thomas"))

function hello(name) {
    return "hoisted by" + name
}

//  NOTE: this has diffrent meaning inside    arrow function and normal function
console.log("====this inside arrow and normal function")
class functions {
    constructor(name) {
        this.name = name 
    }
    arrowFunction = () => {
        console.log("Arrow Funtion:- " + this.name)
        // setTimeout(() => { console.log("Arrow Function:- " + this.name)}, 100)
        
    }
    normalFunction() {
        console.log("Normal Funtion:- " + this.name) // this is correct and defined
        // setTimeout (functions, interval)
        setTimeout(function(){   console.log("Normal Funtion Nested:- " + this.name)} , 1)// this is undefined when nested, here the context of this changes
        setTimeout(function(){   console.log("solution to Nested Normal Funtion using Bind:- " + this.name)}.bind(this) , 1)// this is undefined when nested, here the context of this changes
      
    }
   
}

const obj = new functions("Thomas")
obj.arrowFunction()
obj.normalFunction()

// console.dir(functions.__proto__) // this is the prototype of the class
// console.dir(functions.prototype);
// console.table(Object.getOwnPropertyDescriptors(functions.__proto__));

