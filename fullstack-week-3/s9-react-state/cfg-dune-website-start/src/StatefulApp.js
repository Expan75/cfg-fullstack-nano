import './App.css';
import logo from './logo.svg';
import StatefulFunctionButton from './StatefulFunctionButton';

function StatefulApp() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>This is a React app! Dedicated to the Dune book series</h1>
        <p>Books are fun to read and can be very helpful for learning new stuff</p>
        <p>Rules of book reading are fairly self-explanatory</p>

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

export default StatefulApp;
