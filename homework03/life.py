import pathlib
import random
import typing as tp
from copy import deepcopy
from pprint import pprint as pp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = [[0]]
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_gens = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for i in range(self.rows):
            current = []
            for j in range(self.cols):
                current.append(random.randint(0, 1) if randomize else 0)
            grid.append(current)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        cells = []
        x = cell[0]
        y = cell[1]
        if x - 1 >= 0:
            if y - 1 >= 0:
                cells.append(self.curr_generation[x - 1][y - 1])
            cells.append(self.curr_generation[x - 1][y])
            if y + 1 < self.cols:
                cells.append(self.curr_generation[x - 1][y + 1])
        if y - 1 >= 0:
            cells.append(self.curr_generation[x][y - 1])
        if y + 1 < self.cols:
            cells.append(self.curr_generation[x][y + 1])
        if x + 1 < self.rows:
            if y - 1 >= 0:
                cells.append(self.curr_generation[x + 1][y - 1])
            cells.append(self.curr_generation[x + 1][y])
            if y + 1 < self.cols:
                cells.append(self.curr_generation[x + 1][y + 1])
        return cells

    def get_next_generation(self) -> Grid:
        new_grid = []
        for x in range(0, self.rows):
            row = []
            for y in range(0, self.cols):
                row.append(
                    1
                    if sum(self.get_neighbours((x, y))) == 3
                    or self.curr_generation[x][y] == 1
                    and sum(self.get_neighbours((x, y))) == 2
                    else 0
                )
            new_grid.append(row)
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if not self.is_max_generations_exceeded and self.is_changing:
            self.prev_generation = deepcopy(self.curr_generation)
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_gens if self.max_gens is not None else False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        curr_gen = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if len(line) > 1:
                    curr_gen.append(list(map(int, line[0:-1])))
        life = GameOfLife((len(curr_gen), len(curr_gen[0])))
        life.curr_generation = curr_gen
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding="utf-8") as f:
            for i, rows in enumerate(self.curr_generation):
                for j, elem in enumerate(rows):
                    f.write(str(elem))
                f.write("\n")


if __name__ == "__main__":
    life0 = GameOfLife.from_file(pathlib.Path("glider.txt"))
    pp(life0.curr_generation)
    for _ in range(4):
        pp(life0.prev_generation)
        pp(life0.curr_generation)
        life0.step()
