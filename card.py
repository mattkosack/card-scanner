from tools import get_info

class Card:
    def __init__(self, id):
        self.id = id
        self.info = get_info(id)
        # TODO: break down info into attributes