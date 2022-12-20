import copy
import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 30

    def render(self, surface):
        self.surface = surface
        bottom = self.top + self.height * self.cell_size
        right = self.left + self.width * self.cell_size
        for i in range(self.left, right, self.cell_size):
            for j in range(self.top, bottom, self.cell_size):
                coord = self.get_cell((i + 5, j + 5))
                if self.board[coord[1]][coord[0]]:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     (i, j, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     (i, j, self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, pos):
        if pos:
            self.board[pos[1]][pos[0]] = 0 if self.board[pos[1]][pos[0]] else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, pos):
        if pos[0] < self.left or pos[1] < self.top or \
                pos[0] > self.left + self.width * self.cell_size or \
                pos[1] > self.top + self.height * self.cell_size:
            return None
        return (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.next_generation = copy.deepcopy(self.board)

    def render(self, surface):
        self.surface = surface
        bottom = self.top + self.height * self.cell_size
        right = self.left + self.width * self.cell_size
        for i in range(self.left, right, self.cell_size):
            for j in range(self.top, bottom, self.cell_size):
                coord = self.get_cell((i + 5, j + 5))
                if self.board[coord[1]][coord[0]]:
                    pygame.draw.rect(surface, (0, 255, 0),
                                     (i + 1, j + 1, self.cell_size - 1, self.cell_size - 1))
                    pygame.draw.rect(surface, (255, 255, 255),
                                     (i, j, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     (i, j, self.cell_size, self.cell_size), 1)

    def next_move(self):
        self.next_generation = copy.deepcopy(self.board)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                count_of_neighbor = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        pos_x = (i + x) % self.height if i + x >= self.height else i + x
                        pos_y = (j + y) % self.width if j + y >= self.width else j + y
                        count_of_neighbor += 1 if self.board[pos_x][pos_y] == 1 else 0
                if count_of_neighbor == 3 and self.board[i][j] == 0:
                    self.next_generation[i][j] = 1
                elif count_of_neighbor in [3, 2] and self.board[i][j] == 1:
                    continue
                else:
                    self.next_generation[i][j] = 0
        self.board = copy.deepcopy(self.next_generation)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жизнь на Торе')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    board = Life(18, 18)
    running = True
    fps = 10
    clock = pygame.time.Clock()
    run_generation = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                run_generation = not run_generation
            elif event.type == pygame.MOUSEWHEEL:
                if (5 < fps < 60) or (fps == 5 and event.y > 0) or (fps == 60 and event.y < 0):
                    fps += 5 * abs(event.y) // event.y
        if run_generation:
            board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
