import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const header = screen.getByText(/This is a React app! Dedicated to the Dune book series/i);
  expect(header).toBeInTheDocument();
});