import { render, screen } from '@testing-library/react';
import IncrementButton from './IncrementButton';

describe('Test incrementButton user journey (short one but still)', () => {
    
    // setup, similar to Python SetUp method
    let component;

    beforeEach(() => {
        component = new IncrementButton()
        component.setState = jest.fn()
    })

    test('handle button click', () => {
        expect(component.state.counterValue).toBe(0);
        component.whenButtonPressed();
        expect(component.state.counterValue).toBe(0);
        expect(component.setState).toHaveBeenCalled();
    });
});



