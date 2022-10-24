from initial import screen, pygame

#create wall
class Boundary():
	def __init__(self, pos1, pos2):
		self.pos1 = pos1
		self.pos2 = pos2
		self.colour = (255, 255, 255)
	
	def show(self):
		colour = self.colour
		pygame.draw.line(screen, colour, self.pos1, self.pos2, 5)

#create connected walls
class BoundaryPolygon():
	def __init__(self, points, connected):
		boundarys = []
		for i, pos in enumerate(points):
			if i == len(points)-1 and not connected:
				pass
			else:
				boundarys.append(Boundary(pos, points[(i+1)%len(points)]))
		self.boundarys = boundarys

	def set_colour(self, colour):
		for boundary in self.boundarys:
			boundary.colour = colour
	
	def show(self):
		for boundary in self.boundarys:
			boundary.show()