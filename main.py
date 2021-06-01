import pygame, sys, time, random
from dijkstra import Dijkstra
from a_star import AStar

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
blockSize = 10 #Set the size of the grid block

done = False
ploted = False

# start = (3,1)
# end = (10,12)

def main():
    global SCREEN, CLOCK, done
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    grid, start, end = randomize_grid((WINDOW_WIDTH//blockSize, WINDOW_HEIGHT//blockSize))

    a_star = AStar(grid, start, end)
    # a_star = Dijkstra(grid, start, end)

    draw_grid(grid, start, end)
    while not done:
        updateGrid(a_star, start, end)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    input()


def updateGrid(path_finder, start, end):
    global done, ploted
    if not done:
        grid, result, path = path_finder.run_next()
        if not result:
            for x, row in enumerate(grid):
                for y, item in enumerate(row):
                    rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)

                    if start == (x, y):
                        pygame.draw.rect(SCREEN, GREEN, rect)
                    elif end == (x, y):
                        pygame.draw.rect(SCREEN, RED, rect)
                    elif is_in_stash(path_finder.stash, (x, y)):
                        pygame.draw.rect(SCREEN, YELLOW, rect)
                    elif item != float("inf") and item is not None:
                        pygame.draw.rect(SCREEN, BLUE, rect)
                    else:
                        continue

        else:
            for item in path:
                x, y = item
                rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
                pygame.draw.rect(SCREEN, GREEN, rect)
            done = True

def draw_grid(grid, start, end):
    for x, row in enumerate(grid):
        for y, item in enumerate(row):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)

            if start == (x, y):
                pygame.draw.rect(SCREEN, GREEN, rect)
            elif end == (x, y):
                pygame.draw.rect(SCREEN, RED, rect)
            elif item == float("inf"):
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect)

def is_in_stash(stash, item):
    for i in stash:
        if i == item:
            return True
    return False

def randomize_points():
    start = (random.randint(0, WINDOW_WIDTH//blockSize), random.randint(0, WINDOW_HEIGHT//blockSize))
    end = (random.randint(0, WINDOW_WIDTH//blockSize), random.randint(0, WINDOW_HEIGHT//blockSize))
    return start, end

def randomize_grid(grid_size):
    start = (random.randint(0, WINDOW_WIDTH//blockSize), random.randint(0, WINDOW_HEIGHT//blockSize))
    end = (random.randint(0, WINDOW_WIDTH//blockSize), random.randint(0, WINDOW_HEIGHT//blockSize))
    grid = [[float("inf") for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if random.random() > 0.75:
                grid[i][j] = None
    grid[start[0]][start[1]] = float("inf")
    grid[end[0]][end[1]] = float("inf")
    return grid, start, end

if __name__ == "__main__":
    main()