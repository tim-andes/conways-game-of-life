# Conway's Game of Life
import random, time, copy

WIDTH = 60
HEIGHT = 20
num_cycles = 100 # set number of cycles here
count_cycles = 0

def main(WIDTH, HEIGHT, num_cycles, count_cycles):
	"""
	Conway's Game of Life: An example of cellular automaton.

	Set number of cycles with num_cycles.

	:param WIDTH: Width of grid
	:param HEIGHT: Height of grid
	:return: None
	"""

	# create list of list for cells
	next_cells = []
	for x in range(WIDTH):
		column = [] # create new column
		for y in range(HEIGHT):
			if random.randint(0, 1) == 0:
				column.append('#') # add living cell
			else:
				column.append(' ') # add dead cell
		next_cells.append(column) # list of column lists

	# main program loop
	while num_cycles > count_cycles:
		count_cycles += 1

		# new lines for each step
		print('\n\n\n\n\n')
		current_cells = copy.deepcopy(next_cells)

		# print current_cells on the screen
		for y in range(HEIGHT):
			for x in range(WIDTH):
				print(current_cells[x][y], end='') # print # or a space
			print() # new line at end of row

		# calc the next step's cells based on current step's cells
		for x in range(WIDTH):
			for y in range(HEIGHT):
				# get neighboring coords:
				# (if at border, wrap around)
				left_coord = (x - 1) % WIDTH
				right_coord = (x + 1) % WIDTH
				above_coord = (y - 1) % HEIGHT
				below_coord = (y + 1) % HEIGHT

				# count number of living neighbors
				num_neighbors = 0
				if current_cells[left_coord][above_coord] == '#':
					num_neighbors += 1 # top left coord alive
				if current_cells[x][above_coord] == '#':
					num_neighbors += 1 # top
				if current_cells[right_coord][above_coord] == '#':
					num_neighbors += 1 # top right
				if current_cells[left_coord][y] == '#':
					num_neighbors += 1 # left
				if current_cells[right_coord][y] == '#':
					num_neighbors += 1 # right
				if current_cells[left_coord][below_coord] == '#':
					num_neighbors += 1 # bottom left
				if current_cells[x][below_coord] == '#':
					num_neighbors += 1 # bottom
				if current_cells[right_coord][below_coord] == '#':
					num_neighbors += 1 # bottom right

				# Conway's Game of Life rules:
				if current_cells[x][y] == '#' and num_neighbors in [2, 3]:
					# living cells with 2 or 3 neighbors stay alive
					next_cells[x][y] = '#'
				elif current_cells[x][y] == ' ' and num_neighbors == 3:
					# dead cells with 3 neighbors come alive
					next_cells[x][y] = '#'
				else: # dead
					next_cells[x][y] = ' '

		time.sleep(1) # one second pause

if __name__ == '__main__':
	main(WIDTH, HEIGHT, num_cycles, count_cycles)
