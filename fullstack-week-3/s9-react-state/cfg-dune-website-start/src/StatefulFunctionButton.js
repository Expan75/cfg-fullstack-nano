import './Button.css';
import React, { useState } from 'react';

function StatefulFunctionButton(props) {

  const [quoteIdx, setQuoteIndex] = useState(0)

  function whenButtomPressed() {
    if (quoteIdx === props.quotes.length - 1) {
      setQuoteIndex(0)
    } else {
      setQuoteIndex(quoteIdx + 1)
    }
  }

  return (
    <>
      <button 
        className="duneButton"
        onClick={whenButtomPressed}
        >{props.buttonText}
      </button>
      <p>Quote: "{props.quotes[quoteIdx]}" - Some dude</p>
    </>
  );
}


export default StatefulFunctionButton;
