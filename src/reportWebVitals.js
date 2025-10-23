const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && typeof onPerfEntry === 'function') {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      const metrics = [getCLS, getFID, getFCP, getLCP, getTTFB];
      metrics.forEach((metricFn) => {
        metricFn((metric) => {
          // Tag metric for SIQNet observability
          metric.app = 'SIQNet';
          metric.environment = process.env.NODE_ENV || 'development';

          // Send to custom analytics endpoint or log
          if (process.env.NODE_ENV === 'production') {
            // Example: send to your backend or analytics service
            // fetch('/api/metrics', {
            //   method: 'POST',
            //   headers: { 'Content-Type': 'application/json' },
            //   body: JSON.stringify(metric),
            // });

            console.log('📊 SIQNet metric:', metric);
          }

          // Optional: pass to external handler
          onPerfEntry(metric);
        });
      });
    });
  }
};

export default reportWebVitals;
