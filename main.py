import sys
from x_queen import XQueen, ShowXQueen
from Sudoku import SudokuSolver
from config import *


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [X-Queen|Sudoku]")
        return

    option = sys.argv[1]

    if option == 'x-queen':
        print("Option X-Queen is selected.")
        x_queen = XQueen(INITIAL_POPULATION, NUMBER_QUEEN_CHESS, MUTATION_RATE, EPOCH)
        solution = x_queen.run()
        show = ShowXQueen(NUMBER_QUEEN_CHESS, SCREEN_SIZE, WHITE, BLACK, RED)
        show.run(solution)

    elif option == 'sudoku':
        print("Option Sudoku is selected.")
        sudoku_solver = SudokuSolver(WIDTH, HEIGHT, CAPTION, FONT_SIZE, GRID)
        sudoku_solver.main()
    else:
        print("Invalid option. Please choose 'x-queen' or 'sudoku'.")


if __name__ == "__main__":
    main()
