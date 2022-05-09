import { createStore } from 'redux';


const quoteReducer = (state, action) => {
    console.log('event emitted', state, action)

    switch (action.type) {
        case 'increment': return { counterValue: state.counterValue + 1 }
        default: return state
    }
}

let store = createStore(quoteReducer, { counterValue: 0 })
export default store;
