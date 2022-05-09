import './App.css';
import logo from '../logo.svg';
import Button from './../buttons/Button';
import IncrementButton from './../buttons/IncrementButton';

function AppPage() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>This is a React app! Dedicated to the Dune book series</h1>
        <p>Books are fun to read and can be very helpful for learning new stuff</p>
        <p>Rules of book reading are fairly self-explanatory</p>

        <Button
          buttonText = "Output Dune message"
          appendMessage = ". They're great!"
        />
        <IncrementButton />

        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

export default AppPage;
