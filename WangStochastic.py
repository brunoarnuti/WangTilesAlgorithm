import pygame
import random

# Pygame setup
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Stochastic Wang Tiles")

# Tiles and colors
all_tiles = [{'tile': 'A', 'top': 'red', 'right': 'green', 'bottom': 'blue', 'left': 'yellow'},
             {'tile': 'B', 'top': 'yellow', 'right': 'red', 'bottom': 'green', 'left': 'blue'},
             {'tile': 'C', 'top': 'blue', 'right': 'yellow', 'bottom': 'red', 'left': 'green'},
             {'tile': 'D', 'top': 'green', 'right': 'blue', 'bottom': 'yellow', 'left': 'red'},
             {'tile': 'A', 'top': 'yellow', 'right': 'red', 'bottom': 'green', 'left': 'blue'},
             {'tile': 'B', 'top': 'blue', 'right': 'yellow', 'bottom': 'red', 'left': 'green'},
             {'tile': 'C', 'top': 'green', 'right': 'blue', 'bottom': 'yellow', 'left': 'red'},
             {'tile': 'D', 'top': 'red', 'right': 'green', 'bottom': 'blue', 'left': 'yellow'}]

colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0)}
font = pygame.font.Font(None, 24)

def wang_tiles_rules(grid, position, tile):
    x, y = position
    # Allow occasional repeating tiles and 2x2 squares
    if random.random() < 0.05: return True
    if y > 0 and grid[y-1][x] is not None and tile['top'] != grid[y-1][x]['bottom']:
        return False
    if x > 0 and grid[y][x-1] is not None and tile['left'] != grid[y][x-1]['right']:
        return False
    return True

def place_tiles(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            random.shuffle(all_tiles)
            for tile in all_tiles:
                if wang_tiles_rules(grid, (x, y), tile):
                    grid[y][x] = tile
                    break
            # If no tile fits, place a random tile
            if grid[y][x] is None:
                grid[y][x] = random.choice(all_tiles)

def draw_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pygame.draw.rect(win, (255, 255, 255), (x*50, y*50, 50, 50), 0)
            pygame.draw.rect(win, (0, 0, 0), (x*50, y*50, 50, 50), 2)
            if grid[y][x] is not None:
                text = font.render(grid[y][x]['tile'], True, (0, 0, 0))
                win.blit(text, (x*50+22, y*50+15))
                pygame.draw.line(win, colors[grid[y][x]['top']], (x*50, y*50+10), (x*50+50, y*50+10), 2)
                pygame.draw.line(win, colors[grid[y][x]['right']], (x*50+40, y*50), (x*50+40, y*50+50), 2)
                pygame.draw.line(win, colors[grid[y][x]['bottom']], (x*50, y*50+40), (x*50+50, y*50+40), 2)
                pygame.draw.line(win, colors[grid[y][x]['left']], (x*50+10, y*50), (x*50+10, y*50+50), 2)

grid = [[None]*10 for _ in range(10)]
place_tiles(grid)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255))
    draw_grid(grid)
    pygame.display.update()

pygame.quit()
