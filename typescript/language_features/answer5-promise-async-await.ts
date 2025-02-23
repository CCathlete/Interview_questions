/**
 * Can you explain the concept of Promises and async/await?
 *
 * An async function is a function that returns a promise. When the event loop
 * sees a promise it knows that it can ignore the promise until it's resolved.
 * The promise has a .then method that defines what to do when the promise is
 * resolved and a .catch method that defines what to do when the promise is
 * rejected.
 * The event loop puts the references to these methods of the promise in the
 * task queue and runs them when the promise is resolved or rejected.
 *
 * The async/await keywords are syntactic sugar for chaining promises with
 * promise.then.then.the....catch. This basically means that a chain of promises
 * keeps being ignored by the event loop until the last one is resolved.
 *
 * Promise is implemented using a class with methods then, catch, finally and
 * attributes state, value and reason and arrays of callbacks in order to
 * execute multiple functions when each promise is resolved or rejected.
 *
 * A promise has the following properties:
 * - state: pending, fulfilled, rejected.
 * - methods: then, catch, finally.
 *    - then: executes a function when the promise is fulfilled.
 *    - catch: executes a function when the promise is rejected.
 *    - finally: executes a function whether the promise is fulfilled or
 *      rejected.
 *
 * A general description of a promise looks something like this:
 */

class PromiseExample<T> {
  private state: "pending" | "fulfilled" | "rejected";
  private value: T | null;
  private reason: any;
  private thenCallbacks: ((value: T) => void)[] = [];
  private catchCallbacks: ((reason: any) => void)[] = [];

  constructor(
    executor: (
      resolve: (value: T) => void,
      reject: (reason: any) => void
    ) => void
  ) {
    this.state = "pending";
    this.value = null;
    this.reason = null;
    this.resolve = this.resolve.bind(this);
    this.reject = this.reject.bind(this);
    this.then = this.then.bind(this);

    try {
      executor(this.resolve, this.reject);
    } catch (error) {
      this.reject(error);
    }
  }

  private resolve(value: T): void {
    if (this.state === "pending") {
      this.state = "fulfilled";
      this.value = value;
      // Executing each of our callbacks in the case of a fulfilled promise.
      this.thenCallbacks.forEach((callback: CallableFunction) =>
        callback(value)
      );
    }
  }

  private reject(reason: any): void {
    if (this.state === "pending") {
      this.state = "rejected";
      this.reason = reason;
      // Executing each of our callbacks in the case of a rejected promise.
      this.catchCallbacks.forEach((callback: CallableFunction) =>
        callback(reason)
      );
    }
  }

  // When this is triggered the constructor is called with the executor we
  // define.
  // A new promise is returned to allow async promise chaining (?).
  public then(onFulfilled: (value: T) => void): PromiseExample<T> {
    return new PromiseExample<T>((resolve): void => {
      if (this.state === "fulfilled" && this.value !== null) {
        onFulfilled(this.value);
        resolve(this.value);
      } else {
        this.thenCallbacks.push(onFulfilled);
      }
    });
  }
  public catch(onRejected: (reason: unknown) => void): PromiseExample<T> {
    return new PromiseExample<T>((_, reject) => {
      if (this.state === "rejected" && this.reason !== undefined) {
        onRejected(this.reason);
        reject(this.reason);
      } else {
        this.catchCallbacks.push(onRejected);
      }
    });
  }
}
