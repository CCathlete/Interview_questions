/**
 * Describe how you manage state in a React application and the
 * differences between local and global state management.
 *
 * First, the two fundamental attributes of react components are the
 * component's state and properties (props).
 * Props are read only (immutable) values passed from parent
 * components to child component. They are usually passed as
 * arguments to the function that create the component.
 * Basically, the use of props is to provide data that is used during
 * the creation of the component.
 * NOTE: A component can't change its props, they are controlled by
 * the parent component.
 *
 * The component's state is a group of values that are mutable and
 * the component has the ability to change them using a set function
 * that is created when a variable is registered as a state variable
 * Local states are modified by the component itself.
 * Global state is state information that is managed by a global
 * function (from libraries like Redux or Context API).
 *
 */

import React, { useCallback, useEffect, useState } from "react";

/**
 * Props example:
 */

interface Props
{
  name: string;
}

const firstProps: Props = { name: "Ken" };

const FirstComponent = ( props: Props ): React.ReactNode =>
{
  return <div>{ props.name }</div>;
};

// Parent component.
let App = (): React.ReactNode =>
{
  // Parent creates the child component with given props.
  return <FirstComponent { ...firstProps } />;
};

/**
 * State example:
 * Here, we define a state variable inside the functional component.
 */

const SecondComponent = (): React.ReactNode =>
{
  const [count, setCount] = useState( 0 );

  const increment = useEffect(
    (): void => setCount( count + 1 ), []
  );



  return (
    <div>
      <p>Number of times rendered: { count }</p>
    </div>
  );
};

App = (): React.ReactNode =>
{
  return (
    <SecondComponent />
  );
};

export default App;