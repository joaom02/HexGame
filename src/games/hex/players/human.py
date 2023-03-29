from games.hex.action import HexAction
from games.hex.player import HexPlayer
from games.hex.state import HexState


class HumanHexPlayer(HexPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: HexState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                return HexAction(col, row)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: HexState):
        # ignore
        pass

    def event_end_game(self, final_state: HexState):
        # ignore
        pass
