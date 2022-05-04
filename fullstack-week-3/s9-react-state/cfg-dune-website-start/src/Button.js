import './Button.css';

function Button(props) {
  let quoteIdx = 0
  let quote = ''

  function whenButtomPressed() {
    quote = props.quotes[quoteIdx]
    console.log(quote)
    
    if (quoteIdx === props.quotes.length - 1) {
      quoteIdx = 0
    } else {
      quoteIdx++
    }
  }

  return (
    <>
      <button 
        className="duneButton"
        onClick={whenButtomPressed}
        >{props.buttonText}
      </button>
      <p>Quote: {quote}</p>
    </>
  );
}


export default Button;
