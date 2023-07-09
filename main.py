import pygame
import sys
import random

# Constants
TILE_SIZE = 50
GRID_SIZE = 10
WINDOW_WIDTH = TILE_SIZE * GRID_SIZE
WINDOW_HEIGHT = TILE_SIZE * GRID_SIZE
FPS = 60

# Colors
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Wang tile rules
TILE_RULES = ['AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'BA', 'CA', 'DA', 'CB', 'DB', 'DC']


class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.tile_type = tile_type

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.draw.line(win, COLORS[0], (self.x * TILE_SIZE, self.y * TILE_SIZE),
                         (self.x * TILE_SIZE + TILE_SIZE, self.y * TILE_SIZE), 5)
        pygame.draw.line(win, COLORS[1], (self.x * TILE_SIZE + TILE_SIZE, self.y * TILE_SIZE),
                         (self.x * TILE_SIZE + TILE_SIZE, self.y * TILE_SIZE + TILE_SIZE), 5)
        pygame.draw.line(win, COLORS[2], (self.x * TILE_SIZE, self.y * TILE_SIZE + TILE_SIZE),
                         (self.x * TILE_SIZE + TILE_SIZE, self.y * TILE_SIZE + TILE_SIZE), 5)
        pygame.draw.line(win, COLORS[3], (self.x * TILE_SIZE, self.y * TILE_SIZE),
                         (self.x * TILE_SIZE, self.y * TILE_SIZE + TILE_SIZE), 5)

        font = pygame.font.Font(None, TILE_SIZE // 2)
        text = font.render(self.tile_type[0], True, (0, 0, 0))
        win.blit(text, (self.x * TILE_SIZE + TILE_SIZE // 2 - text.get_width() // 2,
                        self.y * TILE_SIZE + TILE_SIZE // 2 - text.get_height() // 2))


def generate_grid():
    while True:
        grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if x == 0 and y == 0:
                    tile = random.choice(TILE_RULES)
                else:
                    possible_tiles = get_possible_tiles(grid, x, y)
                    tile = random.choice(possible_tiles)
                grid[y][x] = tile

        if is_valid_grid(grid):
            add_square_tiles(grid)
            return grid


def get_possible_tiles(grid, x, y):
    possible_tiles = []
    last_tile = grid[y][x - 1] if x > 0 else grid[y - 1][GRID_SIZE - 1]
    for tile in TILE_RULES:
        if tile[0] != last_tile[1] and tile[1] != last_tile[1]:
            if not has_consecutive_tiles(grid, x, y, tile[0], 'horizontal') and not has_consecutive_tiles(grid, x, y,
                                                                                                           tile[0],
                                                                                                           'vertical'):
                possible_tiles.append(tile)
    return possible_tiles


def has_consecutive_tiles(grid, x, y, tile_type, direction):
    count = 0
    if direction == 'horizontal':
        for i in range(x - 1, max(x - 3, -1), -1):
            if i >= 0 and grid[y][i] == tile_type:
                count += 1
                if count >= 2:
                    return True
            else:
                count = 0
    elif direction == 'vertical':
        for i in range(y - 1, max(y - 3, -1), -1):
            if i >= 0 and grid[i][x] == tile_type:
                count += 1
                if count >= 2:
                    return True
            else:
                count = 0
    return False


def is_valid_grid(grid):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if has_consecutive_tiles(grid, x, y, grid[y][x][0], 'horizontal') or has_consecutive_tiles(grid, x, y,
                                                                                                     grid[y][x][0],
                                                                                                     'vertical'):
                return False
    return True


def add_square_tiles(grid):
    for _ in range(4):  # Add 4 squares
        letter = random.choice('ABCD')
        x = random.randint(0, GRID_SIZE - 2)
        y = random.randint(0, GRID_SIZE - 2)

        # Replace the tiles with a square of four tiles of the same letter
        grid[y][x] = letter + grid[y][x + 1][1]
        grid[y][x + 1] = letter + grid[y][x + 1][1]
        grid[y + 1][x] = letter + grid[y + 1][x][1]
        grid[y + 1][x + 1] = letter + grid[y + 1][x + 1][1]


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Set the window
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    grid = generate_grid()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw the grid
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                tile = Tile(x, y, grid[y][x])
                tile.draw(win)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
