import pygame


class SudokuSolver:
    def __init__(self, width, height, caption, font_size, grid):
        pygame.init()
        self.WIDTH, self.HEIGHT = width, height
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(caption)
        self.FONT = pygame.font.SysFont("comicsans", font_size)
        self.grid = grid

    def valid_move(self, grid, row, column, number):
        if number in grid[row]:
            return False

        for x in range(9):
            if grid[x][column] == number:
                return False

        top_left_corner_row = row - (row % 3)
        bottom_right_corner_column = column - (column % 3)

        for x in range(3):
            for y in range(3):
                if grid[top_left_corner_row + x][bottom_right_corner_column + y] == number:
                    return False
        return True

    def solving(self, grid, row, column):
        if column == 9:
            if row == 8:
                return True
            else:
                row += 1
                column = 0

        if grid[row][column] > 0:
            return self.solving(grid, row, column + 1)

        for number in range(1, 10):
            if self.valid_move(grid, row, column, number):
                grid[row][column] = number

                if self.solving(grid, row, column + 1):
                    return True

            grid[row][column] = 0

        return False

    def draw_grid(self):
        gap = self.WIDTH // 9
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.WIN, (0, 0, 0), (0, i * gap), (self.WIDTH, i * gap), thickness)
            pygame.draw.line(self.WIN, (0, 0, 0), (i * gap, 0), (i * gap, self.HEIGHT), thickness)

    def draw_numbers(self):
        gap = self.WIDTH // 9
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    text = self.FONT.render(str(self.grid[i][j]), 1, (0, 0, 0))
                    self.WIN.blit(text, (j * gap + (gap // 2 - text.get_width() // 2), i * gap + (gap // 2 - text.get_height() // 2)))

    def main(self):
        self.solving(self.grid, 0, 0)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.WIN.fill((255, 255, 255))
            self.draw_grid()
            self.draw_numbers()
            pygame.display.update()

        pygame.quit()
