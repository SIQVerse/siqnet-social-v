import { render, screen } from '@testing-library/react';
import App from './App';

test('renders SIQNet welcome message', () => {
  render(<App />);
  const heading = screen.getByRole('heading', { name: /welcome to siqnet/i });
  expect(heading).toBeInTheDocument();
});

test('renders civic profile call-to-action', () => {
  render(<App />);
  const button = screen.getByRole('button', { name: /create your civic profile/i });
  expect(button).toBeInTheDocument();
});

test('renders ecosystem link', () => {
  render(<App />);
  const link = screen.getByRole('link', { name: /explore the siqnet ecosystem/i });
  expect(link).toBeInTheDocument();
});
