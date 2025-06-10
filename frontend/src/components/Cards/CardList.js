import React from 'react';
import CardItem from './CardItem';

export default function CardList({ cards }) {
  return (
    <div>
      {cards.map((card) => (
        <CardItem key={card.id} card={card} />
      ))}
    </div>
  );
}
