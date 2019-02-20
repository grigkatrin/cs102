from typing import List, Tuple, Optional, Dict, Any


def shape(maze: List):
    """
    Функция возвращает размер лабиринта

    :param: maze: Лабиринт
    :return: Число строк, число столбцов
    """
    assert maze, "maze can't be empty"
    return len(maze), len(maze[0])


def neighbours(maze: List, pos: Tuple) -> List:
    """
    Функция возвращает возможные направления движения в лабиринте
    относительно текущей позиции

    :param maze: Лабиринт
    :param pos: Текущая позиция в лабиринте (строка, столбец)
    :return: Список возможных позиций
    """
    rows, cols = shape(maze)
    variations = []
    if maze[pos[0] - 1][pos[1]]: variations.append('up')
    if maze[pos[0] + 1][pos[1]]: variations.append('down')
    if maze[pos[0]][pos[1] - 1]: variations.append('left')
    if maze[pos[0]][pos[1] + 1]: variations.append('right')
    return variations


def possible_paths(maze: List, pos: Tuple, short: Dict={}, path: Dict={}, count: int=0):
    path[pos] = count
    if maze[pos[0]][pos[1]] is None:
        end = pos
        return path, short, end
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for step in steps:
        if maze[pos[0] + step[0]][pos[1] + step[1]] and (
                0 < pos[0] + step[0] < len(maze) and 0 < pos[1] + step[1] < len(maze[0])):
            check = path.get((pos[0] + step[0], pos[1] + step[1]))
            if check is not None and check > count:
                path[
                    (pos[0] + step[0], pos[1] + step[1])] = count
                short[(pos[0] + step[0], pos[1] + step[1])] = (pos[0], pos[1])
                possible_paths(maze, (pos[0] + step[0], pos[1] + step[1]), short, path, count + 1)

            else:
                if (pos[0] + step[0], pos[1] + step[1]) not in path.keys():
                    short[(pos[0] + step[0], pos[1] + step[1])] = (pos[0], pos[1])
                    possible_paths(maze, (pos[0] + step[0], pos[1] + step[1]), short, path, count + 1)
    end = None
    return path, short, end


def short_path(maze, path=[], start=(3, 1), end=(3, 7)):
    if len(path) == 0:
        path.append(end)
    path.append(maze[end])
    if maze[end] == start:
        return path
    else:
        short_path(maze, path, start, maze[end])
    return path


def find_route(maze: List, initial: Tuple):
    """
    Поиск выхода из лабиринта.

    Функция возвращает кратчайший путь до выхода из лабиринта.

    :param maze: Лабирнит
    :param pos: Текущая позиция в лабиринте (строка, столбец)
    :return: Кратчайший путь до выхода
    """
    path, short, end = possible_paths(maze, initial)
    if end:
        final_path = short_path(maze, start=initial, end=end)
        return final_path
    else:
        return None


def print_maze(maze: List, pos: Tuple):
    """
    Функция выводит лабиринт и текущее положение в нем.

    Возможные ходы должны отмечаться '.', текущее положение '☺',
    стена '☒', а выход '☼'.

    Пример:
    ☒☒☒☒☒☒☒
    ☒☺.☒.☼☒
    ☒☒.☒.☒☒
    ☒..☒..☒
    ☒.☒☒☒.☒
    ☒.....☒
    ☒☒☒☒☒☒☒

    :param maze: Лабиринт
    :param pos: Текущая позиция в лабиринте (строка, столбец)
    """
    rows, cols = shape(maze)
    for row in range(rows):
        for col in range(cols):
            if row == pos[0] and col == pos[1]:
                print('☺', end='')
                continue
            if maze[row][col]:
                print('.', end='')
            if maze[row][col] is False:
                print('☒', end='')
            if maze[row][col] is None:
                print('☼', end='')
        print('\n')


def escape(maze: List, initial):
    """
    Вывести последовательно путь до выхода из лабиринта

    :param maze: Лабиринт
    :param pos: Текущая позиция в лабиринте (строка, столбец)
    """
    final_path = find_route(maze, initial)
    if final_path:
        for step in final_path:
            print_maze(maze, step)
    else:
        print('Нет выхода')


maze = [
    [False, False, False, False, False, False, False],
    [False, True, True, False, True, None, False],
    [False, False, True, False, True, False, False],
    [False, True, True, False, True, True, False],
    [False, True, False, False, False, True, False],
    [False, True, True, True, True, True, False],
    [False, False, False, False, False, False, False]
]

print(print_maze(maze, (1,1)))
print(neighbours(maze, (1,1)))