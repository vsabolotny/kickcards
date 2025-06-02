from flask import jsonify
from app.models.card import Card

class CardService:
    def __init__(self):
        self.cards = []

    def add_card(self, card_data):
        card = Card(
            id=len(self.cards) + 1,
            name=card_data.get('name', 'Unknown'),
            imageFront=card_data.get('imageFront'),
            imageBack=card_data.get('imageBack'),
            date=card_data.get('date')
        )
        self.cards.append(card)
        return card

    def get_all_cards(self, filters=None):
        # Example implementation: Apply filters to retrieve cards
        if filters:
            # Apply filtering logic based on filters (e.g., date, player name)
            pass
        # Return all cards (or filtered cards)
        return []

    def filter_cards(self, name=None, date=None):
        filtered_cards = self.cards
        if name:
            filtered_cards = [card for card in filtered_cards if name.lower() in card.name.lower()]
        if date:
            filtered_cards = [card for card in filtered_cards if card.date == date]
        return filtered_cards

    def get_card_by_id(self, card_id):
        for card in self.cards:
            if card.id == card_id:
                return card
        return None