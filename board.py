import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
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
            self.board[pos[1]][pos[0]] = int(not (self.board[pos[1]][pos[0]]))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, pos):
        if pos[0] < self.left or pos[1] < self.top or \
                pos[0] > self.left + self.width * self.cell_size or \
                pos[1] > self.top + self.height * self.cell_size:
            return None
        return (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    board = Board(100, 100)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()