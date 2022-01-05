import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border("|", "|", "-", "-", "+", "+", "+", "+")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for y, row in enumerate(self.life.curr_generation):
            for x, cell in enumerate(row):
                symbol = "*" if cell == 1 else " "
                screen.addch(y + 1, x + 1, symbol)
    
    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        screen.clear()
        for y in range(1, self.life.rows + 1):
            for x in range(1, self.life.cols + 1):
                screen.addstr(y, x, " " if self.life.curr_generation[y - 1][x - 1] == 0 else "*")

    def run(self) -> None:
        screen = curses.initscr()
        running = True
        while running:
            self.draw_grid(screen)
            self.draw_borders(screen)
            self.life.step()
            screen.refresh()
            curses.napms(100)
        curses.endwin()


if __name__ == "__main__":
    life0 = GameOfLife((24, 80), max_generations=50)
    ui = Console(life0)
    ui.run()
