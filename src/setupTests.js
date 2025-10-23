// ✅ Extended matchers for DOM assertions
import '@testing-library/jest-dom/extend-expect';

// ✅ Simulate user interactions
import '@testing-library/user-event';

// ✅ Optional: log test environment info
console.info('🧪 SIQNet test environment initialized');

// ✅ Optional: global mock setup (e.g. fetch, localStorage)
// global.fetch = jest.fn(() => Promise.resolve({ json: () => ({}) }));

// ✅ Optional: silence console errors in tests
// jest.spyOn(global.console, 'error').mockImplementation(() => {});
