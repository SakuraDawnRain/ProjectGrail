class player:
    ID = 0
    HP = 10
    MP = 10
    Attack = 1
    Defense = 1
    Cards = []
    
    def __init__(self, ID) -> None:
        self.ID = ID

    def show_status(self):
        return "ID:" + str(self.ID) + "HP:" + str(self.HP) + "MP:" + str(self.MP)

    
