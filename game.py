from player import *

class game:
    PlayerList = []


class demo_game(game):
    def __init__(self, PlayerNum) -> None:
        super().__init__()
        for i in range(PlayerNum):
            self.PlayerList.append(player(i))

    def show_player(self):
        status = ""
        for i in self.PlayerList:
            status += i.show_status()
            status += "\n"
        return status




