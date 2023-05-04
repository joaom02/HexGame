from random import randint

from games.hex.action import HexAction
from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.state import State


class RandomHexPlayer(HexPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: HexState):
        col = randint(0, state.get_num_cols() - 1)
        row = randint(0, state.get_num_cols() - 1)
        return HexAction(col, row)                       

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
