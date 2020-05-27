class Hero:

	def __init__(self, map):
		self.map = map
		self.position = self.map.start # From start()

	def move(self, direction): 
		new_position = getattr(self.position, direction)() # call an attribute or a method with a str, here I call it with "up"
		if new_position in self.map
			self.position = new_position