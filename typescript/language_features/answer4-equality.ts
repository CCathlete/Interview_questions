/**
 * What is the difference between == and === in JavaScript?
 *
 * == is a loose equality operator that checks if the values are the same
 * even if the types are not the same.
 *
 * === is a strict equality operator that checks if the values are the same and
 * the types are the same.
 *
 * NOTE! This is not true in TypeScript because of static typing.
 * TS will always check that the types are the same so using == and ===
 * are the same (unless we're bypassing the type checking).
 *
 * Example:
 */

let expr: boolean = 5 == ("5" as unknown);
console.log(expr); // true
