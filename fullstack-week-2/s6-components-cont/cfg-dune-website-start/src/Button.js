import './Button.css';

function Button(props) {

  let idx = 0;
  let msg = props.buttonText

  function whenButtomPressed() {  
    idx++
    if (idx === props.messages.length) {
      idx = 0
    }
    msg = props.messages[idx]
    console.log(msg)
  }

  return (
    <>
      <button 
        className="duneButton"
        onClick={whenButtomPressed}
        >{msg}
      </button>
    </>
  );
}


export default Button;
