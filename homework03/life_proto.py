import random
import typing as tp

import pygame

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid_ = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        self.grid = self.create_grid(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid_:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = []
        for i in range(self.cell_height):
            current = []
            for j in range(self.cell_width):
                current.append(random.randint(0, 1) if randomize else 0)
            grid.append(current)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for y in range(0, self.height, self.cell_size):
            for x in range(0, self.width, self.cell_size):
                color = pygame.Color(
                    "white" if self.grid[y // self.cell_size][x // self.cell_size] == 0 else "green"
                )
                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        cells = []
        x = cell[0] // self.cell_size
        y = cell[1] // self.cell_size
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.grid[x - 1][y - 1])
            cells.append(self.grid[x - 1][y])
            if y + 1 < self.cell_width:
                cells.append(self.grid[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.grid[x][y - 1])
        if y + 1 < self.cell_width:
            cells.append(self.grid[x][y + 1])
        if x + 1 < self.cell_height:
            if y - 1 >= 0:
                cells.append(self.grid[x + 1][y - 1])
            cells.append(self.grid[x + 1][y])
            if y + 1 < self.cell_width:
                cells.append(self.grid[x + 1][y + 1])
        return cells

    def get_next_generation(self) -> Grid_:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = []
        for x in range(0, self.height, self.cell_size):
            row = []
            for y in range(0, self.width, self.cell_size):
                row.append(
                    1
                    if sum(self.get_neighbours((x, y))) == 3
                    or self.grid[x // self.cell_size][y // self.cell_size] == 1
                    and sum(self.get_neighbours((x, y))) == 2
                    else 0
                )
            new_grid.append(row)
        return new_grid


if __name__ == "__main__":
    game = GameOfLife()
    game.run()
