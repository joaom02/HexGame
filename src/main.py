from games.hex.players.greedyOffensive import GreedyOHexPlayer
from games.hex.players.greedyDeffensive import GreedyDHexPlayer
from games.hex.players.minimaxO import MinimaxOHexPlayer
from games.hex.players.minimaxD import MinimaxDHexPlayer
from games.hex.players.random import RandomHexPlayer
from games.hex.players.human import HumanHexPlayer
from games.hex.simulator import HexSimulator
from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1
    
    run_simulation("Hex Simulator", HexSimulator(RandomHexPlayer("1"), HumanHexPlayer("0")), num_iterations)


if __name__ == "__main__":
    main()
