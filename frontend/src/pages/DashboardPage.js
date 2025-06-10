import React, { useState, useEffect } from 'react';
import CardList from '../components/Cards/CardList';
import CardFilter from '../components/Cards/CardFilter';
import { fetchCards } from '../services/api';

export default function DashboardPage() {
  const [cards, setCards] = useState([]);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    async function loadCards() {
      const data = await fetchCards(filter);
      setCards(data);
    }
    loadCards();
  }, [filter]);

  return (
    <div>
      <h1>Dashboard</h1>
      <CardFilter onFilter={setFilter} />
      <CardList cards={cards} />
    </div>
  );
}
