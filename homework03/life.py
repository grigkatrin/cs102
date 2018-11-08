import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        # PUT YOUR CODE HERE
        self.clist = self.cell_list(randomize = True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            self.draw_cell_list(self.clist)
            self.clist = self.update_cell_list(self.clist)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        if randomize:
            for row in range(self.cell_width):
                self.clist.append([random.randint(0, 1) for col in range(self.cell_height)])
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        x = 0
        y = 0
        for row in clist:
            for col in row:
                if col == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, self.cell_size, self.cell_size))
                    x += self.cell_size
                if col == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size))
                    x += self.cell_size
        x = 0
        y += self.cell_size
        pass

    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row, col = cell
        rows = [row - 1, row, row + 1]
        cols = [col - 1, col, col + 1]
        for row1 in rows:
            if 0 <= row1 < self.cell_height:
                for col1 in cols:
                    if col1 == col and row1 == row:
                        continue
                    if 0 <= col1 < self.cell_width:
                        neighbours.append(self.clist[row1][col1])
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = []
        for row in range(len(cell_list)):
            new_clist.append([])
            for col in range(len(cell_list[row])):
                neighbours = self.get_neighbours((row, col))
                sum = 0
                for i in neighbours:
                    if i == 1:
                        sum += 1
                if cell_list == 0 and sum == 3:
                    new_clist[row].append(1)
                elif cell_list == 1 and (sum == 2 or sum == 3):
                    new_clist[row].append(1)
                else:
                    new_clist[row].append(0)
        self.clist = new_clist
        return self.clist
