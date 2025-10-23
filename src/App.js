import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="SIQNet Logo" />
        <h1>Welcome to SIQNet</h1>
        <p>
          Africa’s sovereign civic-tech operating system. Verified identity. Emotional intelligence. Community-powered governance.
        </p>
        <a
          className="App-link"
          href="https://siqnet.tech"
          target="_blank"
          rel="noopener noreferrer"
        >
          Explore the SIQNet Ecosystem →
        </a>
        <div style={{ marginTop: '2rem' }}>
          <button className="cta-button" onClick={() => alert('Coming soon: Civic Profile Creation')}>
            Create Your Civic Profile
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;
