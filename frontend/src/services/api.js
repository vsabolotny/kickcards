const API_URL = 'http://localhost:5000';

export async function login(email, password) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  return response.json();
}

export async function fetchCards(filter) {
  const query = filter ? `?player=${encodeURIComponent(filter)}` : '';
  const response = await fetch(`${API_URL}/cards${query}`);
  return response.json();
}

export async function saveCard(card) {
  const response = await fetch(`${API_URL}/cards`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(card),
  });
  return response.json();
}
