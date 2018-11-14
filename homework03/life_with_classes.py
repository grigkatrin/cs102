import pygame
from pygame.locals import *
import random
from copy import deepcopy


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

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки,
        представленный в виде матрицы
        """
        for cell in clist:
            x = cell.col * self.cell_size
            y = cell.row * self.cell_size
            rect = (x, y, self.cell_size, self.cell_size)
            if cell.is_alive() == 1:
                cell_color = pygame.Color('green')
            else:
                cell_color = pygame.Color('white')
            pygame.draw.rect(self.screen, cell_color, rect)
        pass

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = CellList(self.cell_height, self.cell_width, randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_cell_list(self.clist)
            self.clist = self.clist.update()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row, col, state=False):
        self.row = row
        self.col = col
        self.state = state
        pass

    def is_alive(self):
        if self.state:
            return True
        return False


class CellList:
    def __init__(self, nrows, ncols, randomize=False, is_file=False, file_clist=[]):
        self.nrows = nrows
        self.ncols = ncols
        self.randomize = randomize
        self.clist = []

        if randomize:
            for i in range(self.nrows):
                self.clist.append([])
                for j in range(self.ncols):
                    self.clist[i].append(Cell(i, j, random.randint(0, 1)))
        else:
            for i in range(self.nrows):
                self.clist.append([])
                for j in range(self.ncols):
                    self.clist[i].append(Cell(i, j))

        if is_file:
            self.clist = file_clist

    def get_neighbours(self, cell):
        neighbours = []
        row = cell.row
        col = cell.col
        rows = [row - 1, row, row + 1]
        cols = [col - 1, col, col + 1]
        for row1 in rows:
            if 0 <= row1 < len(self.clist):
                for col1 in cols:
                    if col1 == col and row1 == row:
                        continue
                    if 0 <= col1 < len(self.clist[0]):
                        if self.clist[row1][col1].is_alive():
                            neighbours.append(Cell(row1, col1, True))
                        else:
                            neighbours.append(Cell(row1, col1, False))
        return neighbours

    def update(self):
        new_clist = deepcopy(self)
        for row in range(self.nrows):
            for col in range(self.ncols):
                neighbours = new_clist.get_neighbours(new_clist.clist[row][col])
                sum = 0
                for i in neighbours:
                    if i.is_alive() == 1:
                        sum += 1
                if new_clist.clist[row][col].is_alive() == 0 and sum == 3:
                    self.clist[row][col] = Cell(row, col, True)
                elif new_clist.clist[row][col].is_alive() == 1 and (sum == 2 or sum == 3):
                    self.clist[row][col] = Cell(row, col, True)
                else:
                    self.clist[row][col] = Cell(row, col, False)
        return self

    def __iter__(self):
        self.index_row = 0
        self.index_col = 0
        return self

    def __next__(self):
        if self.index_row < self.nrows:
            cell = self.clist[self.index_row][self.index_col]
            self.index_col += 1
            if self.index_col == self.ncols:
                self.index_col = 0
                self.index_row += 1
            return cell
        else:
            raise StopIteration

    def __str__(self):
        s = '[['
        for row in range(self.nrows):
            for col in range(self.ncols):
                s += str(int(self.clist[row][col].is_alive()))
                if col != self.ncols - 1:
                    s += ', '
            if row != self.nrows - 1:
                s += '], ['
        s += ']]'
        return s

    @classmethod
    def from_file(cls, filename):
        grid = [c for c in open(filename).read()]
        clist = [[]]
        c_row = 0
        c_col = 0
        ncol = 0
        nrow = 0
        for i in grid:
            if i == '\n':
                clist.append([])
                c_row += 1
                ncol = c_col
                c_col = 0
                continue
            if i == '1':
                clist[c_row].append(Cell(c_row, c_col, True))
            if i == '0':
                clist[c_row].append(Cell(c_row, c_col, False))
            c_col += 1
        nrow = c_row + 1
        return CellList(nrow, ncol, file_clist=clist, is_file=True)

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
