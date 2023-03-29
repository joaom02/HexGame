from random import choice
from games.hex.action import HexAction
from games.hex.player import HexPlayer
from games.hex.state import HexState
from games.state import State


class GreedyDHexPlayer(HexPlayer):

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

                if grid[row][col] == self.get_current_pos():
                    count += 1
                if row > 0 and col > 0:
                    if grid[row- 1][col - 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if row < state.get_num_rows() -1  and col < state.get_num_cols() -1:
                    if grid[row + 1][col + 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if row > 0 and col < state.get_num_cols()-1:
                    if grid[row - 1][col + 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if col < state.get_num_cols()-1:
                    if grid[row][col + 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if col > 0:
                    if grid[row][col - 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if row < state.get_num_rows()-1 and col > 0:
                    if grid[row+ 1][col - 1] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if row < state.get_num_rows()-1:
                    if grid[row+ 1][col] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1
                if row > 0:
                    if grid[row- 1][col] != (state.get_acting_player() and state.EMPTY_CELL):
                        count += 1


            # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if selected_col is None or selected_row is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_col = col
                    selected_row = row
                    max_count = count

        if selected_col is None:
            raise Exception("There is no valid action")

        return HexAction(selected_col, selected_row)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
