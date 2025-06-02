from datetime import datetime

class Card:
    def __init__(self, id, name, image_front, image_back):
        self.id = id
        self.name = name
        self.image_front = image_front
        self.image_back = image_back
        self.date = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'imageFront': self.image_front,
            'imageBack': self.image_back,
            'date': self.date.isoformat()
        }