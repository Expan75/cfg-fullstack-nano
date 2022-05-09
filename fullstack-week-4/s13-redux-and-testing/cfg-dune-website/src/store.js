import { createStore } from 'redux';


const quoteReducer = (state, action) => {
    switch (action.type) {
        case 'counterValue/increment':
            return { value: state.counterValue===2 ? state.counterValue + 1 : 0 }
        default: return state
    }
}

let store = createStore(quoteReducer, { counterValue: 0 })

export default store;
