import React from 'react';

export default function CardScanner({ onScan }) {
  // Placeholder for scanning functionality
  return (
    <div>
      <button onClick={() => onScan && onScan({ id: Date.now() })}>
        Scan Card
      </button>
    </div>
  );
}
