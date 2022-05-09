import { render, screen } from '@testing-library/react';
import AppPage from './AppPage';


describe('app page component tests', () => {
  
  test('renders learn react link', () => {
    render(<AppPage />);
    const header = screen.getByText(/This is a React app! Dedicated to the Dune book series/i);
    expect(header).toBeInTheDocument();
  });
})