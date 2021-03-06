import pygame
import random
import time


def cwrap(x):
    q,r = divmod(x,255)
    if q%2:
        return 255-r
    else:
        return r


def removeWalls(a, b):
	x = a.x-b.x
	y = a.y-b.y

#Top right bottom left
	if(x == -1):#remove right wall of A and left wall of b
		a.walls[1] = False
		b.walls[3] = False
	if(x==1):#Remove left wall of A and right wall of b
		a.walls[3] = False
		b.walls[1] = False
	if(y == -1):#Remove bottom wall of A and top wall of b
		a.walls[2] = False
		b.walls[0] = False
	if(y == 1):#Remove top wall of A and bottom wall of b
		a.walls[0] = False
		b.walls[2] = False



class Cell():
	def __init__(self, x, y,w, gameDisplay, grid, cols, rows):
		self.cols = cols
		self.rows = rows
		self.x = x
		self.y = y
		self.w = w
		self.gameDisplay = gameDisplay
		self.walls = [True, True, True, True] #Top, right, bottom, left
		self.visited = False



	def show(self):
		x_pos = self.x*self.w
		y_pos = self.y*self.w

		if(self.visited):
			col = (cwrap(self.x * 30),
			      cwrap(self.y * -10),
				  cwrap(self.y * 40))
			pygame.draw.rect(gameDisplay,col,(x_pos,y_pos,w,w))
		#pygame.draw.rect(gameDisplay,(255,255,255),(x_pos,y_pos,w,w), 1)
		if (self.walls[0]):
		#Top
			pygame.draw.line(gameDisplay, (255,255,255), (x_pos, y_pos), (x_pos+w, y_pos), 1)
		if (self.walls[1]):
		#Right
			pygame.draw.line(gameDisplay, (255, 255,255), (x_pos+w, y_pos), (x_pos+w, y_pos+w), 1)
		if (self.walls[2]):
		#Bottom
			pygame.draw.line(gameDisplay, (255, 255,255), (x_pos, y_pos+w), (x_pos+w, y_pos+w), 1)
		if (self.walls[3]):
		#Left
			pygame.draw.line(gameDisplay, (255, 255,255), (x_pos, y_pos), (x_pos, y_pos+w), 1)

		

	def checkNeighbours(self):
		neighbours = []
		if(self.index(self.x, self.y-1)!= -1):
			top = grid[self.index(self.x, self.y-1)]

			if not top.visited :
				neighbours.append(top)
		
		if(self.index(self.x+1, self.y)!= -1):
			right = grid[self.index(self.x+1, self.y)]

			if not right.visited:
				neighbours.append(right)
		
		if(self.index(self.x, self.y+1)!= -1):
			bottom = grid[self.index(self.x, self.y+1)]

			if not bottom.visited:
				neighbours.append(bottom)

		if(self.index(self.x-1, self.y)!= -1):
			left = grid[self.index(self.x-1, self.y)]

			if not left.visited:
				neighbours.append(left)

		#print(top, self.index(self.x, self.y-1))
		if(neighbours):
			return neighbours[random.randint(0, len(neighbours)-1)]
		else:
			return None



	def index(self, x, y):
		if(x<0 or y<0 or x>self.cols-1 or y>self.rows-1):
			return -1

		else:
			return (x+y*self.cols)

	def highlight(self):
		x_pos = self.x*self.w
		y_pos = self.y*self.w

		pygame.draw.rect(gameDisplay,(96,50,158),(x_pos,y_pos,w,w))


if __name__ == "__main__":
	pygame.init()
	WIDTH = 600
	HEIGHT = 600

	w = 10
	cols = int(WIDTH/w)
	rows = int(HEIGHT/w)
	grid = []
	stack = []
	
	gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Recursive Backtracker Maze Generator")

	for i in range(rows):
		for j in range(cols):
			grid.append(Cell(j, i, w, gameDisplay, grid, cols, rows))


	current = grid[0]

	clock = pygame.time.Clock()

	exit = False
	time.sleep(10)

	while not exit:
		for i in range(len(grid)):
			grid[i].show()

		#Step 1
		current.visited = True
		current.highlight()

		next = current.checkNeighbours()

		if (next != None):
			next.visited = True
			#Step 2
			stack.append(current)

			#Step 3
			removeWalls(current, next)


			#Step 4
			current = next


		elif (len(stack)>0):
			current = stack.pop()



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True

		pygame.display.update()
		gameDisplay.fill((0,0,0))
		clock.tick(60)
	pygame.quit()
	quit()




