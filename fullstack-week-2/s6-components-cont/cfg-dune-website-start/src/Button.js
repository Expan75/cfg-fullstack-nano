import './Button.css';

function Button() {
  
  function whenButtomPressed() {

    const characters = ['Paul', 'Tieto', 'Baron Harkonen']
    const validChar = characters.filter(char => char === 'Paul')

    console.log(`${validChar} is of house Atredies!`)
  }

  return (
    <>
      <button 
        className="duneButton"
        onClick={whenButtomPressed}
        >Click Me!
      </button>
    </>
  );
}

export default Button;
