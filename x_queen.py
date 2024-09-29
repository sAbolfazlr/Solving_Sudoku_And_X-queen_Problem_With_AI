import random as rnd
import pygame
import sys


class XQueen:
    def __init__(self, population_s, number_queen, mutation_rate, epoch):
        self.p_s = population_s
        self.n = number_queen
        self.m_r = mutation_rate
        self.epoch = epoch

    def init_population(self, population_size, n):
        population_list = []
        for i in range(population_size):
            new_member = []
            for j in range(n):
                new_member.append(rnd.randint(1, n))
            new_member.append(0)
            population_list.append(new_member)
        return population_list

    def cross_over(self, population_list, population):
        for i in range(0, len(population_list), 2):
            child1 = population_list[i][:len(population[0]) // 2] + population[i + 1][
                                                                    len(population[0]) // 2:len(population[0]) - 1] + [
                         0]
            child2 = population[i + 1][:len(population[0]) // 2] + population[i][
                                                                   len(population[0]) // 2: len(population[0]) - 1] + [
                         0]
            population_list.append(child1)
            population_list.append(child2)

        return population_list

    def mutation(self, population_list, mutation_rate, n):
        chosen_ones = [i for i in range(len(population_list) // 2, len(population_list))]
        for i in range(len(population_list) // 2):
            new_random = rnd.randint(0, len(population_list) // 2 - 1)
            chosen_ones[new_random], chosen_ones[i] = chosen_ones[i], chosen_ones[new_random]
        chosen_ones = chosen_ones[:int(len(chosen_ones) * mutation_rate)]
        for i in chosen_ones:
            new_ch = rnd.randint(0, n - 1)
            new_value = rnd.randint(1, n)
            population_list[i][new_ch] = new_value
        return population_list

    def fitness(self, population_list, n):
        i = 0
        conflict = 0
        lenght = len(population_list)
        while i < lenght:
            j = 0
            conflict = 0
            while j < n:
                l = j + 1

                while l < n:
                    if population_list[i][j] == population_list[i][l]:
                        conflict += 1
                    if abs(j - l) == abs(population_list[i][j] - population_list[i][l]):
                        conflict += 1
                    l += 1
                j += 1
            population_list[i][len(population_list[j]) - 1] = conflict
            i += 1

        for i in range(len(population_list)):
            min = i
            for j in range(i, len(population_list)):
                if population_list[j][n] < population_list[min][n]:
                    min = j
            temp = population_list[i]
            population_list[i] = population_list[min]
            population_list[min] = temp

        return population_list

    def run(self):
        population = self.init_population(self.p_s, self.n)
        population = self.fitness(population, self.n)
        solution = None
        if population[0][self.n] == 0:
            print(f'Solution found in initial population: {population[0][0:self.n]}')
        else:
            for i in range(self.epoch):
                population = self.cross_over(population, population)
                population = self.mutation(population, self.m_r, self.n)
                population = self.fitness(population, self.n)
                population = population[:len(population) // 2]
                if population[0][self.n] == 0:
                    print(f'solution found: {population[0][0:self.n]}')
                    solution = population[0][:self.n]
                    return solution
                else:
                    print(f'# {i + 1} ---> best Solution so far: {population[0]}')
            solution = population[0][:self.n]
            return solution


class ShowXQueen:
    def __init__(self, n_size, screen_size, white, black, red):
        self.N_SIZE = n_size
        self.SCREEN_SIZE = screen_size
        self.SQUARE_SIZE = self.SCREEN_SIZE // self.N_SIZE
        self.WHITE = white
        self.BLACK = black
        self.Red = red

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))
        pygame.display.set_caption('8 Queens Solution')

    def draw_board(self):
        colors = [self.WHITE, self.BLACK]
        for row in range(self.N_SIZE):
            for col in range(self.N_SIZE):
                color = colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def draw_queens(self, positions):
        for row in range(len(positions)):
            col = positions[row] - 1
            pygame.draw.circle(self.screen, self.Red,
                               (col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                               self.SQUARE_SIZE // 3)

    def run(self, solution):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_board()
            if solution:
                self.draw_queens(solution)
            pygame.display.flip()
