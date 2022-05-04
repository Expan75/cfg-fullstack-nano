import './Button.css';
import React from 'react';

class StatefulClassButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { quoteIdx: 0 }
        this.whenButtomPressed = this.whenButtomPressed.bind(this);
    }
    
    whenButtomPressed() {
        this.setState((state, props) => {
            console.log('logging state+props: ', state, props)
            if (state.quoteIdx === props.quotes.length - 1) {
                return { quoteIdx: 0 }
            } else {
                return { quoteIdx: state.quoteIdx + 1 }
            }
        });
    }

    render() {
        return (
            <>
              <button 
                className="duneButton"
                onClick={this.whenButtomPressed}
                >{ this.props.buttonText }
              </button>
              <p>Quote: { this.props.quotes[this.state.quoteIdx] } - Some dude</p>
            </>
          );
    }
}

export default StatefulClassButton;