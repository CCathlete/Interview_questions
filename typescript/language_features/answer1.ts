/**
 * What are the differences between var, let, and const in JavaScript?
 *
 * var:
 * - Accessible anywhere in the function (also global?)
 * - "Hoisted" to the top of the function scope, meaning they're accessible in
 * lines that come before their declaration.
 * - Can be re-assigned (same with let, not with const).
 * - Can be re-declared within the same scope (let and const can't within the
 * same block but you can re declare in other blocks)
 *
 * let:
 * - Accessible only within the block it was declared in (loop, if etc.).
 * - Are considered "temporary dead" before the line of their declaration
 * but are known since the start of the block so they can't be declared twice.
 * NOTE: The areas in the block before the declaration line are called TDZ
 * (temporary dead zone).
 * - Can be re-assigned within the same block.
 *
 * const:
 * - Like let but can't be re-assigned.
 */

var x: number = 10;
console.log(x); // 10
x = 20;
console.log(x); // 20

let y: number = 10;
console.log(y); // 10
y = 20;
console.log(y); // 20

const z: number = 10;
console.log(z); // 10
// z = 20; // Error

// var is function scoped, let and const are block scoped.

const foo = () => {
  var a: number = 10;
  console.log(a); // 10
  console.log(x); // 20 because x was defined outside.
};
// console.log(a) // Error

const bar = () => {
  if (true) {
    let b: number = 10;
    const c: number = 10;
    console.log(`b: ${b}, c: ${c}`); // b: 10, c: 10
  }
  // console.log(`b: ${b}, c: ${c}`); // Error
};

// var can be redeclared, let can be reassigned but not redeclared, const can't
// be redeclared or reassigned.
// NOTE: This redeclaration is just theoretical because it has to be the same
// type as the previous redeclaration so it's identical to reassigning and
// exists only for historical reasons.

var k: number = 10;
console.log(`k: ${k}, type: ${typeof k}`); // k: 10, type: number
// var k: string = "hello"; // Error
var k: number = 20;
console.log(`k: ${k}, type: ${typeof k}`); // k: 20, type: number
