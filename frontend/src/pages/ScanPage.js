import React, { useState } from 'react';
import CardScanner from '../components/Scanner/CardScanner';
import { saveCard } from '../services/api';

export default function ScanPage() {
  const [card, setCard] = useState(null);

  const handleScan = async (scannedCard) => {
    setCard(scannedCard);
    await saveCard(scannedCard);
  };

  return (
    <div>
      <h1>Scan Card</h1>
      <CardScanner onScan={handleScan} />
      {card && <pre>{JSON.stringify(card, null, 2)}</pre>}
    </div>
  );
}
