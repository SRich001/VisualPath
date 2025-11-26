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

    def open_it(self):
        self.colour = EMERALD
        
    def close_it(self):
        self.colour = SALMON
  
    def block_it(self):
        self.colour = MOONSTONE
       
    def end_it(self):
        self.colour = AMETHYST
    
    def make_path(self):
        self.colour == CITRINE
    
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_blocked(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row ][self.col + 1].is_blocked(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col - 1].is_blocked(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])


    def is_less_than(self, other):
        return False

    
def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2 + abs(y1 - y2))   

def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_position(), end.get_position())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			pass
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_position(), end.get_position())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.open_it()
                    

		draw()

		if current != start:
			current.close_it()
        

	return False

                

       
      
    
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
  

def draw(window, grid, rows, width):
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
    while run:
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]: #LEFT CLICK
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
                    
                
            
            elif pygame.mouse.get_pressed()[2]: #RIGHT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_pos_clicked(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(window, grid, ROWS, width), grid, start, end)

				    
							
						
					
			    

            
    
    pygame.quit()


main(WINDOW, WIDTH)




    
        


