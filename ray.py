from initial import screen, pygame
from methods import add_tuples, sub_tuples

#creates ray (cast)
class Ray():
	def __init__(self, pos, dir, angle):
		self.pos = pos
		self.dir = dir
		self.rot = angle # degrees
		self.point = False

	def look(self, dir):
		dir = sub_tuples(dir, self.pos)
		#self.dir = normalize_tuple(dir)
		self.dir = dir
	
	def show(self, colour):
		pos2 = add_tuples(self.pos, self.dir)
		pygame.draw.line(screen, colour, self.pos, pos2, 5)

	def cast(self, wall):
		pos1, pos2 = wall.pos1, wall.pos2
		x1, y1 = pos1[0], pos1[1]
		x2, y2 = pos2[0], pos2[1]

		pos3, pos4 = self.pos, add_tuples(self.pos, self.dir)
		x3, y3 = pos3[0], pos3[1]
		x4, y4 = pos4[0], pos4[1]

		den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
		if den == 0:
			return False
		else:
			t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
			u = -(((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den)
			if t > 0 and t < 1 and u > 0:
				x = x1 + t * (x2-x1)
				y = y1 + t * (y2-y1)
				return (x, y)
			else:
				return False

