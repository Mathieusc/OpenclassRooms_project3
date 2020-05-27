class Position:

	def __init__(self, x, y):
		self.position = (x, y)

	def __repr__(self):
		return str(self.position)

	def __hash__(self):
		# Transform into a 'str'
		return hash(self.position)

	def __eq__(self, pos):
		return self.position == pos.position # 'in' will find each position in the set

	def up(self):
		x, y = self.position
		return Position (x - 1, y)

	def down(self):
		x, y = self.position		
		return Position (x + 1, y)

	def right(self):
		x, y = self.position		
		return Position (x, y + 1)

	def left(self):
		x, y = self.position		
		return Position (x, y - 1)