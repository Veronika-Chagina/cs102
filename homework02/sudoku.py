import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "" for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    return [values[i : i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    return [grid[i][pos[1]] for i in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    zero = [0, 0]
    zero[0] = 0 if pos[0] < 3 else 3 if 2 < pos[0] < 6 else 6
    zero[1] = 0 if pos[1] < 3 else 3 if 2 < pos[1] < 6 else 6
    values = [grid[i][j] for i in range(zero[0], zero[0] + 3) for j in range(zero[1], zero[1] + 3)]
    return values


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                return (i, j)
    return (-1, -1)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    values = set(i for i in "123456789")
    for i, number in enumerate(get_row(grid, pos)):
        values.discard(number)
    for i, number in enumerate(get_col(grid, pos)):
        values.discard(number)
    for i, number in enumerate(get_block(grid, pos)):
        values.discard(number)
    return values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_positions(grid)
    if pos == (-1, -1):
        return grid
    values = find_possible_values(grid, pos)
    for i, option in enumerate(values):
        grid[pos[0]][pos[1]] = option
        if solve(grid) is not None:
            return solve(grid)
    grid[pos[0]][pos[1]] = "."
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    for i in range(len(solution)):
        for j in range(len(solution)):
            a = get_row(solution, (i, j))
            b = get_col(solution, (i, j))
            c = get_block(solution, (i, j))
            if (
                len(set(a)) != len(a)
                or len(set(b)) != len(b)
                or len(set(c)) != len(c)
                or solution[i][j] == "."
            ):
                return False
    return True


def generate_sudoku(n: int) -> tp.Optional[tp.List[tp.List[str]]]:
    """Генерация судоку заполненного на N элементов"""
    init = [["." for j in range(9)] for i in range(9)]
    gen = solve(init)
    if gen:
        n = min(n, 81)
        while 81 - n != 0:
            for i in range(len(gen)):
                for j in range(len(gen[i])):
                    if 81 - n != 0 and gen[i][j] != ".":
                        m = random.choice("123456789.")
                        if m == ".":
                            gen[i][j] = "."
                            n += 1
    return gen


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
