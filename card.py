class Card:
    type = 0

class Emblem(Card):
    def __init__(self) -> None:
        super().__init__()
        self.type = 1

class Weapon(Card):
    def __init__(self) -> None:
        super().__init__()
        self.type = 2

class Action(Card):
    def __init__(self) -> None:
        super().__init__()
        self.type = 3

class Container(Card):
    def __init__(self) -> None:
        super().__init__()
        self.type = 4