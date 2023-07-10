import pygame
import random

# Pygame setup
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Stochastic Wang Tiles")

# Tiles and colors
tiles = ['A', 'B', 'C', 'D']
colors = {'A': (255, 0, 0), 'B': (0, 255, 0), 'C': (0, 0, 255), 'D': (255, 255, 0)}
font = pygame.font.Font(None, 24)

def can_place(tile, grid, x, y):
    if x > 0:
        left_tile = grid[y][x-1]
        if (tile == 'A' and left_tile == 'B') or (tile == 'B' and left_tile == 'A') or \
           (tile == 'C' and left_tile == 'D') or (tile == 'D' and left_tile == 'C'):
            return False
    if y > 0:
        top_tile = grid[y-1][x]
        if (tile == 'A' and top_tile == 'C') or (tile == 'B' and top_tile == 'D') or \
           (tile == 'C' and top_tile == 'A') or (tile == 'D' and top_tile == 'B'):
            return False
    return True

def place_tiles(grid):
    for y in range(10):
        for x in range(10):
            random.shuffle(tiles)
            for tile in tiles:
                if can_place(tile, grid, x, y):
                    grid[y][x] = tile
                    break

def draw_grid(grid):
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(win, colors[grid[y][x]], (x*50, y*50, 50, 50), 0)
            text = font.render(grid[y][x], True, (0, 0, 0))
            win.blit(text, (x*50+22, y*50+15))
            pygame.draw.line(win, (255, 255, 255), (x*50+5, y*50+5), (x*50+45, y*50+5), 3)
            pygame.draw.line(win, (255, 255, 255), (x*50+5, y*50+45), (x*50+45, y*50+45), 3)
            pygame.draw.line(win, (255, 255, 255), (x*50+5, y*50+5), (x*50+5, y*50+45), 3)
            pygame.draw.line(win, (255, 255, 255), (x*50+45, y*50+5), (x*50+45, y*50+45), 3)

grid = [['A']*10 for _ in range(10)]
place_tiles(grid)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    draw_grid(grid)
    pygame.display.update()

pygame.quit()
