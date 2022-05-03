import './Button.css';

function Button(props) {
  let quoteIdx = 0
  let quote = ''

  function whenButtomPressed() {
    
    quoteIdx++
    if (quoteIdx === props.quotes.length - 1) {
      quoteIdx = 0
    }
    
    quote = props.quotes[quoteIdx]
    console.log(quote)
  }

  return (
    <>
      <button 
        className="duneButton"
        onClick={whenButtomPressed}
        >{props.buttonText}
      </button>
    </>
  );
}


export default Button;
