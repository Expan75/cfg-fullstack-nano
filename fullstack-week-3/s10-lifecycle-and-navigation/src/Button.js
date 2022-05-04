import './Button.css';
import React, { useState, useEffect} from 'react';

function Button(props) {
  const [currMessage, setCurrMessage] = useState("N/A");
  const [currMessageIndexSelector, setCurrMessageIndexSelector] = useState(0);

  function whenButtonPressed() {
    setCurrMessageIndexSelector(currMessageIndexSelector + 1);

    if (currMessageIndexSelector == 2){
      setCurrMessageIndexSelector(0);
    }
  }

  useEffect(() => {
    console.log("Hello World");
  }, []);

  useEffect(() => {
    const randomMessage = [
      "He who controls the spice controls the whole universe!",
      "The spice must flow",
      "Fear is the mind-killer",
    ]

    setCurrMessage(randomMessage[currMessageIndexSelector]);
  }, [currMessageIndexSelector]);

  return (
    <>
      <button
        className="duneButton"
        onClick = {whenButtonPressed}
      >
        {props.buttonText + props.appendMessage}
      </button>

      <h1>{currMessage}</h1>
    </>
  );
}

export default Button;
