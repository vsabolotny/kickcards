import React from 'react';

export default function CardItem({ card }) {
  return (
    <div className="card-item">
      <img src={card.imageUrl} alt={card.player} width={100} />
      <div>
        <h3>{card.player}</h3>
        <p>{card.team}</p>
      </div>
    </div>
  );
}
