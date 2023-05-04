from random import choice
from games.hex.action import HexAction
from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.state import State

class GreedyOHexPlayer(HexPlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: HexState):
        grid = state.get_grid()
        selected_col = None
        selected_row = None
        max_count = 0

        for col in range(0, state.get_num_cols()):
            for row in range(0, state.get_num_rows()):
                count = 0
                if not state.validate_action(HexAction(col, row)):
                    continue

                if row + 1 < 4 and grid[row+1][col] == 0:
                    count += 1
                if row >= 0 and grid[row-1][col] == 0: 
                    count += 1
                if col+1<4 and grid[row][col+1] == 1:
                    count += 1
                if col >= 0 and grid[row][col-1] == 1: 
                    count += 1
                if selected_col is None or selected_row is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_col = col
                    selected_row = row
                    max_count = count
        if selected_col is None:
            raise Exception("There is no valid action")
        if selected_row is None:
            raise Exception("There is no valid action")

        return HexAction(selected_col, selected_row)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
