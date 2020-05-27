import config.settings as constants
from position import Position

class Map:

	def __init__(self, filename):
		self.filename = filename

		self.paths = set() # set to benifit from operators, (if path - start - goal = every possible paths, etc, ...)
		self.data = {
			"start_pos": set(),
			"goal_pos": set()
		}
		self.start = set()
		self.goal = set()
		self.items = set()
		self.guardian = set()

		self.load_from_file()

	#@property # Used to make start() as a Method while it's being used like an attribute NOT WORKING ATM
	#def start(self):
	#	return list(self.data['start_pos'])[0]

	def __contains__(self, position):
		# Magical, check why, if def is_valid_path error : TypeError: argument of Type 'Map' is not iterable
		return position in self.paths # If a movement is valid

	def load_from_file(self):
		with open(self.filename) as infile:
			for x, line in enumerate(infile):
				for y, col in enumerate(line):
					if col == constants.PATH_CHAR:
						self.paths.add(Position(x, y))
					elif col == constants.START_CHAR:
						self.start.add(Position(x, y))
						self.paths.add(Position(x, y))
					elif col == constants.GOAL_CHAR:
						self.goal.add(Position(x, y))
						self.paths.add(Position(x, y))
					#else:
						#It's a wall or outside the map

def main():
	map = Map('data/maps/map1.txt')

	p = Position(0, 0).down().left() # Calling each function to move in a direction returns me if the character CAN or CANNOT move
	print(p in map) # Same as this: (map.is_valid_path(p))

if __name__ == "__main__":
	main()