import './IncrementButton.css';
import React from "react"

class IncrementButton extends React.Component {
  constructor(props) {
    super(props);

    this.state = {counterValue: 0};

    this.whenButtonPressed = this.whenButtonPressed.bind(this);
  }

  whenButtonPressed() {
    this.setState({
      counterValue: this.state.counterValue + 1
    });
  }

  componentDidMount(){
    console.log("The component now successfully exists!")
  }

  componentDidUpdate(){
    console.log("The new value is: " + this.state.counterValue)
  }

  render() {
    return (
      <>
        <button
          className="incrementButton"
          onClick = {this.whenButtonPressed}
        >
          {this.state.counterValue}
        </button>
      </>
    );
  }
}

export default IncrementButton;
