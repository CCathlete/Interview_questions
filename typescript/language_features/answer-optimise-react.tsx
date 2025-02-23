import React, { JSX, useMemo, useState, useCallback } from "react";
/**
 * How would you optimize a React application for performance?
 *
 * The main issues I'll focus on will be rendering and non rendering
 * issues.
 *
 */

/**
 * 1. Minimising re-renders:
 * Wrapping components that we don't need to re-render with
 * a react.memo() component.
 */

interface Props
{
  children: React.ReactNode;
}
const NonRenderedComponent: React.FC<Props> = React.memo(
  ( props: Props ): JSX.Element =>
  {
    return <div>{ props.children }</div>;
  }
);

/**
 * 2. Using useMemo to memorise calculations.
 */

const computeExpensiveValue = ( a: any, b: any ): Object =>
{
  return a + b;
};

const component1 = (): React.ReactNode =>
{
  // Needs to be inside a functional component.
  const [val, setValues] = useState( { a: {}, b: {} } );
  const memorisedValue: Object = useMemo(
    () => computeExpensiveValue( val.a, val.b ), [val]
  );

  // memorisedValues won't change since we didn't use setValues
  val.a = { first: 5 };

  // This time it will change since we used setValues.
  setValues(
    { a: { first: 5 }, b: { second: 10 } }
  );

  return (
    <div></div>
  );
};

/**
 * 3. Memorising callbacks.
 */

type Callback = () => void;
const Child: React.FC<{ onClick: Callback; }> = React.memo(
  ( ( { onClick }: { onClick: Callback; } ): React.ReactNode =>
  {
    console.log( "rendering child" );
    return <button onClick={ onClick }> Click </button>;
  } )
);

export const Parent = (): React.ReactNode =>
{
  const [count, setCount] = useState( 0 );

  // useCallback makes sure that the function doesn't change and it's
  // connected to the count state.
  // The function not changing means it's created only once and not
  // every time the component re renders.
  const handleClick = useCallback(
    (): void =>
    {
      setCount( count + 1 );
    }, [count]
  );

  return (
    <div>
      <Child onClick={ handleClick } />
      <div>Count: { count }</div>
    </div>
  );
};

/**
 * 4. Lazy loading.
 * Imports only when they are needed.
 */

// Default imports only.
// const LazyComponent = React.lazy(
//   () => import( "./answer3-closure.ts" )
// );