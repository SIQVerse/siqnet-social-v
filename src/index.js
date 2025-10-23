import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Optional: Error boundary wrapper
function ErrorBoundary({ children }) {
  return (
    <React.StrictMode>
      {children}
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
);

// 🌐 Performance monitoring
reportWebVitals((metric) => {
  if (process.env.NODE_ENV === 'production') {
    // Send metrics to an analytics endpoint or observability tool
    // Example: fetch('/analytics', { method: 'POST', body: JSON.stringify(metric) });
    console.log('SIQNet metric:', metric);
  }
});
