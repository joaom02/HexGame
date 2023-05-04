from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.game_simulator import GameSimulator


class HexSimulator(GameSimulator):

    def __init__(self, player1: HexPlayer, player2: HexPlayer, tamanho:int = 4):
        super(HexSimulator, self).__init__([player1, player2])
        
        self.__tamanho = tamanho
    def init_game(self):
        return HexState(self.__tamanho)

    def before_end_game(self, state: HexState):
        # ignored for this simulator
        pass

    def end_game(self, state: HexState):
        # ignored for this simulator
        pass
