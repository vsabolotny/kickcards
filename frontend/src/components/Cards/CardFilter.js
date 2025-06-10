import React from 'react';

export default function CardFilter({ onFilter }) {
  return (
    <div>
      <input
        type="text"
        placeholder="Filter by player"
        onChange={(e) => onFilter(e.target.value)}
      />
    </div>
  );
}
