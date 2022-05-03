import './Button.css';
import React from 'react';

class ButtonClass extends React.Component {
    constructor(props) {
        super(props);
        this.state = { quoteIdx: 0 }
        this.whenButtomPressed = this.whenButtomPressed.bind(this);
    }

    whenButtomPressed() {
        console.log(this.props.quotes[this.state.quoteIdx])
        if (this.state.quoteIdx === this.props.quotes.length - 1) {
            this.state.quoteIdx = 0
        } else {
            this.state.quoteIdx++
        }
    }

    render() {
        return (
            <>
              <button 
                className="duneButton"
                onClick={this.whenButtomPressed}
                >{ this.props.buttonText }
              </button>
            </>
          );
    }
}

export default ButtonClass;