from typing import Optional

from games.hex.action import HexAction
from games.hex.result import HexResult
from games.state import State

from games.hex.player import HexPlayer

class HexState(State):
    EMPTY_CELL = -1

    def __init__(self, tamanho: int = 4):
        super().__init__()

        if tamanho < 4:
            raise Exception("the number of rows must be 11 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = tamanho
        self.__num_cols = tamanho
        self.__tamanho = tamanho

        """
        the grid
        """
        self.__grid = [[HexState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def check_win4(self, player):
        row = 0
        col = 0
        if player == 0:
            print("player:" + str(player))
            while True:
                print("row: " + str(row)+ "col: " + str(col))
                if row == 4:
                    return True
                elif self.__grid[row][col] ==0:
                    col = col
                    row = row + 1
                elif col != 3 and self.__grid[row][col+1] == 0:
                    col = col +1
                    row = row + 1
                elif self.__grid[row][col-1] == 0:
                    col = col -1
                    row = row + 1
                else:
                    break
                

        elif player == 1:
            for row in range(self.__tamanho-1):
                if (self.__grid[row][0] == 1 or self.__grid[row + 1][0] == 1 or self.__grid[row - 1][0] == 1) and \
                    (self.__grid[row][1] == 1 or self.__grid[row + 1][1] == 1 or self.__grid[row - 1][1] == 1) and \
                    (self.__grid[row][2] == 1 or self.__grid[row + 1][2] == 1 or self.__grid[row - 1][2] == 1) and \
                    (self.__grid[row][3] == 1 or self.__grid[row + 1][3] == 1 or self.__grid[row - 1][3] == 1):
                    return True

    def check_win11(self, player):
        if player == 0:
            for col in range(self.__tamanho-1):
                if (self.__grid[0][col] == 0 or self.__grid[0][col + 1] == 0 or self.__grid[0][col - 1] == 0) and \
                    (self.__grid[1][col] == 0 or self.__grid[1][col + 1] == 0 or self.__grid[1][col - 1] == 0) and \
                    (self.__grid[2][col] == 0 or self.__grid[2][col + 1] == 0 or self.__grid[2][col - 1] == 0) and \
                    (self.__grid[3][col] == 0 or self.__grid[3][col + 1] == 0 or self.__grid[3][col - 1] == 0) and \
                    (self.__grid[4][col] == 0 or self.__grid[4][col + 1] == 0 or self.__grid[4][col - 1] == 0) and \
                    (self.__grid[5][col] == 0 or self.__grid[5][col + 1] == 0 or self.__grid[5][col - 1] == 0) and \
                    (self.__grid[6][col] == 0 or self.__grid[6][col + 1] == 0 or self.__grid[6][col - 1] == 0) and \
                    (self.__grid[7][col] == 0 or self.__grid[7][col + 1] == 0 or self.__grid[7][col - 1] == 0) and \
                    (self.__grid[8][col] == 0 or self.__grid[8][col + 1] == 0 or self.__grid[8][col - 1] == 0) and \
                    (self.__grid[9][col] == 0 or self.__grid[9][col + 1] == 0 or self.__grid[9][col - 1] == 0) and \
                    (self.__grid[10][col] == 0 or self.__grid[10][col + 1] == 0 or self.__grid[10][col - 1] == 0):
                    return True

        elif player == 1:
            for row in range(self.__tamanho-1):
                if (self.__grid[row][0] == 1 or self.__grid[row + 1][0] == 1 or self.__grid[row - 1][0] == 1) and \
                    (self.__grid[row][1] == 1 or self.__grid[row + 1][1] == 1 or self.__grid[row - 1][1] == 1) and \
                    (self.__grid[row][2] == 1 or self.__grid[row + 1][2] == 1 or self.__grid[row - 1][2] == 1) and \
                    (self.__grid[row][3] == 1 or self.__grid[row + 1][3] == 1 or self.__grid[row - 1][3] == 1) and \
                    (self.__grid[row][4] == 1 or self.__grid[row + 1][4] == 1 or self.__grid[row - 1][4] == 1) and \
                    (self.__grid[row][5] == 1 or self.__grid[row + 1][5] == 1 or self.__grid[row - 1][5] == 1) and \
                    (self.__grid[row][6] == 1 or self.__grid[row + 1][6] == 1 or self.__grid[row - 1][6] == 1) and \
                    (self.__grid[row][7] == 1 or self.__grid[row + 1][7] == 1 or self.__grid[row - 1][7] == 1) and \
                    (self.__grid[row][8] == 1 or self.__grid[row + 1][8] == 1 or self.__grid[row - 1][8] == 1) and \
                    (self.__grid[row][9] == 1 or self.__grid[row + 1][9] == 1 or self.__grid[row - 1][9] == 1) and \
                    (self.__grid[row][10] == 1 or self.__grid[row + 1][10] == 1 or self.__grid[row - 1][10] == 1):
                    return True

    def __check_winner(self, player):
        if self.__tamanho == 4:
            return self.check_win4(player)
        elif self.__tamanho == 11:
            return self.check_win4(player)
        else:
            return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: HexAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        player = self.__acting_player 
        cols = self.__num_cols - 1
        rows = self.__num_rows - 1
        print("Player: " + str(player))
        print(self.__num_cols)
        print(self.__num_rows)
        print(col)
        print(row)

        if col >= 0 and col <= cols and  row >= 0 and row <= rows and self.__grid[row][col] == HexState.EMPTY_CELL:
            return True
        else:
            return False


    def update(self, action: HexAction):
        col = action.get_col()
        row = action.get_row()

        # drop the checker
        self.__grid[row][col] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'O',
                  1: 'X',
                  HexState.EMPTY_CELL: '_'
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 11:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("---", end="")
        print("--")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__tamanho):
            print(" " * (row + 1), end="")
            for col in range(0, self.__tamanho):
                self.__display_cell(row, col)
                print(" ", end="")
            print("|" + str(row))
        self.__display_separator()
        print(" " * (self.__tamanho - 1), end="")
        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = HexState(self.__tamanho)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[HexResult]:
        if self.__has_winner:
            return HexResult.LOOSE if pos == self.__acting_player else HexResult.WIN
        if self.__is_full():
            return HexResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        actions = []
        for i in range(0,self.__num_rows):
            for j in range(0,self.__num_cols):
                action = HexAction(i,j)
                if self.validate_action(action):
                    actions.append(action)
        return actions
    
    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
