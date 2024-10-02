import numpy as np
import pygame
import time

WIDTH, HEIGHT = 700, 700
N = 70
CELL_SIZE = WIDTH // N

ALIVE_COLOR = (255, 255, 255)  #células vivas
DEAD_COLOR = (0, 0, 0)  #células muertas
GRID_COLOR = (40, 40, 40)  #cuadrícula

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Vida")

def create_grid(N):
    """Crea una cuadrícula de NxN con células vivas aleatorias"""
    return np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

def update_grid(grid):
    """Actualiza la cuadrícula de acuerdo a las reglas del Juego de la Vida"""
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Contar vecinos vivos
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            # Aplicar reglas del Juego de la Vida
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def draw_grid(screen, grid):
    screen.fill(DEAD_COLOR)
    for i in range(N):
        for j in range(N):
            color = ALIVE_COLOR if grid[i, j] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    grid = create_grid(N)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        draw_grid(screen, grid)
        pygame.display.flip()

        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()
