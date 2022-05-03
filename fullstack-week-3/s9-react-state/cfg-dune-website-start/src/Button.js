import './Button.css';

function Button(props) {
  let quoteIdx = 0
  let msg = ''

  function whenButtomPressed() {
    msg = props.messages[quoteIdx]
    console.log(msg)
    
    quoteIdx++
    if (quoteIdx === props.messages.length) {
      quoteIdx = 0
    }
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
