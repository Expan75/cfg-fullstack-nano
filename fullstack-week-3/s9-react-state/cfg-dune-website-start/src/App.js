import './App.css';
import logo from './logo.svg';

// old with inadequate state handling
import Button from './Button.js';
import ClassButton from './ClassButton.js';

// both styles correct state handling
import StatefulButtonClass from './StatefulClassButton';
import StatefulFunctionButton from './StatefulFunctionButton';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>This is a React app! Dedicated to the Dune book series</h1>
        <p>Books are fun to read and can be very helpful for learning new stuff</p>
        <p>Rules of book reading are fairly self-explanatory</p>

        {/* A JSX comment */}
        {/* <Button */}
        {/* <ClassButton */}
        {/* <StatefulClassButton */}
        {/* <StatefulFunctionButton */}
        <StatefulFunctionButton
          buttonText = "Output Dune message" 
          quotes = {[
            'He who controls the spice controls the whole universe!',
            'The spice must flow',
            'Feat is the mind-killer']}
        />
        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

export default App;
