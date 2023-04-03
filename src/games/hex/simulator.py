from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.game_simulator import GameSimulator


class HexSimulator(GameSimulator):

    def __init__(self, player1: HexPlayer, player2: HexPlayer, tamanho:int = 3):
        super(HexSimulator, self).__init__([player1, player2])
        while tamanho != 4 and tamanho != 11:
            try:
                tamanho = int(input("Size of board (4 or 11): "))
                if tamanho != 4 and tamanho != 11:
                    print("Invalid size. Please enter 4 or 11.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        self.__tamanho = tamanho
    def init_game(self):
        print(self.__tamanho)
        return HexState(self.__tamanho)

    def before_end_game(self, state: HexState):
        # ignored for this simulator
        pass

    def end_game(self, state: HexState):
        # ignored for this simulator
        pass
