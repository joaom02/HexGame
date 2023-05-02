from games.hex.players.greedyOffensive import GreedyOHexPlayer
from games.hex.players.minimaxO import MinimaxOHexPlayer
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

    num_iterations = 10
    
    print("Bem-Vindo ao jogo Hex")
    print("Que tipo de jogo quer realizar?")
    print("1-Jogador vs Jogador")
    print("2-Jogador vs Computador")
    print("3-Computador vs Computador")
    print("0-Sair do jogo")
    opecion = int(input("Escolha uma opção: "))
    if opecion == 1:
        run_simulation("Hex Simulator", HexSimulator(HumanHexPlayer("1"),HumanHexPlayer("0")),num_iterations)
    elif opecion == 2:
        print("Que nivel de dificuldade prentende jogar?")
        print("1-Facil")
        print("2-Medio")
        print("3-Dificil")
        nivel = int(input("Escolha uma opção: "))
        if nivel == 1:
            run_simulation("Hex Simulator", HexSimulator(RandomHexPlayer("1"),HumanHexPlayer("0")),num_iterations)
        elif nivel == 2:
            run_simulation("Hex Simulator", HexSimulator(GreedyOHexPlayer("1"),HumanHexPlayer("0")),num_iterations)
        elif nivel == 3:
            run_simulation("Hex Simulator", HexSimulator(MinimaxOHexPlayer("1"),HumanHexPlayer("0")),num_iterations)
    elif opecion == 3:
        print("1-Facil vs Facil")
        print("2-Facil vs Medio")
        print("3-Facil vs Dificil")
        print("4-Medio vs Dificil")
        ai = int(input("Escolha uma opção: "))
        if ai == 1:
            run_simulation("Hex Simulator", HexSimulator(RandomHexPlayer("1"),RandomHexPlayer("0")),num_iterations)
        elif ai == 2:
            run_simulation("Hex Simulator", HexSimulator(RandomHexPlayer("1"),GreedyOHexPlayer("0")),num_iterations)
        elif ai == 3:
            run_simulation("Hex Simulator", HexSimulator(RandomHexPlayer("1"),MinimaxOHexPlayer("0")),num_iterations)
        elif ai == 4:
            run_simulation("Hex Simulator", HexSimulator(GreedyOHexPlayer("1"),MinimaxOHexPlayer("0")),num_iterations)
    elif opecion == 0:
        print("Até a proxima")
        return
    
if __name__ == "__main__":
    main()
