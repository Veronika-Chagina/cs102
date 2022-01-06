from copy import deepcopy

import pygame
from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 20, speed: int = 10) -> None:
        super().__init__(life)
        self.width = 640
        self.height = 480
        self.cell_size = cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
        self.paused = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for y in range(0, self.height, self.cell_size):
            for x in range(0, self.width, self.cell_size):
                color = pygame.Color(
                    "white"
                    if self.life.curr_generation[y // self.cell_size][x // self.cell_size] == 0
                    else "green"
                )
                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

    def change_grid(self, coord) -> None:
        x, y = coord[0] // self.cell_size, coord[1] // self.cell_size
        self.life.curr_generation[y][x] = 0 if self.life.curr_generation[y][x] == 1 else 1
        color = pygame.Color("white" if self.life.curr_generation[y][x] == 0 else "green")
        pygame.draw.rect(
            self.screen,
            color,
            (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
        )

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        self.life.curr_generation = self.life.create_grid(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                    and self.paused is False
                ):
                    self.paused = True
                    first = True
                elif (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                    and self.paused is True
                ):
                    self.paused = False
                elif self.paused is True and event.type == pygame.MOUSEBUTTONDOWN:
                    if first is True:
                        self.life.curr_generation = deepcopy(self.life.prev_generation)
                        first = False
                    self.change_grid(event.pos)
                    self.draw_lines()
                    pygame.display.flip()
            if not self.paused:
                self.draw_grid()
                self.draw_lines()
                self.life.step()
                pygame.display.flip()
                clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    life0 = GameOfLife((24, 80), max_generations=50)
    game = GUI(life0)
    game.run()
