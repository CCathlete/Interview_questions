// Can you explain closures in JavaScript and give an example?
/**
 * A closure is a function that is defined inside another function so it has
 * access to variables from the parent function and can reference them even
 * after the parent function had finished.
 *
 * As long as the closure is referenced somewhere in the code it won't be
 * garbage collected and would prevent the parent functions scope from being
 * garbage collected.
 *
 * The scope of a module is a singleton, meaning that the closure would get
 * created and allocated only once and would be shared across all imports.
 *
 * Example:
 */

export let addOne: CallableFunction;

const outerFunc = (): void => {
  let x: number = 10;
  const innerFunc = (): void => {
    x += 1;
  };

  addOne = innerFunc;
};

// The closure would get created here the moment something from this module
// gets imported (it would cause the entire module to get executed and its
// scope to be created and allocated).
outerFunc();
