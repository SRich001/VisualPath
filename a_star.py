import pygame
import math
from queue import PriorityQueue

#Defining Window size
WIDTH = 500
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinder")

#Defining Colours

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MOONSTONE = (0, 159, 183)
CITRINE = (236, 212, 68)
SALMON = (253, 150, 169)
EMERALD = (61, 220, 151)
AMETHYST = (157, 117, 203)

class Node:
    def __init__(self, row, col, width, total_rows):

        self.row = row
        self.col = col

        self.x = row * width
        self.y = col * width

        self.colour = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_position(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.colour == SALMON
    
    def is_open(self):
        return self.colour == EMERALD
    
    def is_blocked(self):
        return self.colour == MOONSTONE
    
    def is_start(self):
        return self.colour == CITRINE
    
    def is_end(self):
        return self.colour == AMETHYST
    
    def reset(self):
        self.colour = WHITE

    def start_it(self):
        self.colour = CITRINE

        

    def close_it(self):
        self.colour == SALMON
    
    def open_it(self):
        self.colour == EMERALD
    
    def block_it(self):
        self.colour = MOONSTONE
       
    def end_it(self):
        self.colour = AMETHYST
    
    def make_path(self):
        self.colour == CITRINE
    
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def is_less_than(self, other):
        return False

    
def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2 + abs(y1 - y2))    
    
def make_grid(rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(i, j, gap, rows)
                grid[i].append(node)
        
        return grid    
    
def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, BLACK, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(window, BLACK, (j * gap, 0), (j * gap, width))
  

def draw_all(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()

def get_pos_clicked(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(window, width):

    ROWS = 25
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw_all(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            if pygame.mouse.get_pressed()[0]: #Left Click
                pos = pygame.mouse.get_pos()
                row, col = get_pos_clicked(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.start_it()

                elif not end and node != start:
                    end = node
                    end.end_it()

                elif node != end and node != start:
                    node.block_it()
                    
                
            
            elif pygame.mouse.get_pressed()[2]: #Right Click
                pos = pygame.mouse.get_pos()
                row, col = get_pos_clicked(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
                



    
    pygame.quit()


main(WINDOW, WIDTH)




    
        


