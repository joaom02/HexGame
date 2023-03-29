from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.game_simulator import GameSimulator


class HexSimulator(GameSimulator):

    def __init__(self, player1: HexPlayer, player2: HexPlayer, tamanho:int =5):
        super(HexSimulator, self).__init__([player1, player2])
        tamanho = int(input("Size of board: "))
        """
        the number of rows and cols from the connect4 grid
        """
        self.__tamanho = tamanho
    def init_game(self):
        return HexState(self.__tamanho)

    def before_end_game(self, state: HexState):
        # ignored for this simulator
        pass

    def end_game(self, state: HexState):
        # ignored for this simulator
        pass
