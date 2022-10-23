from initial import screen, pygame, SIZE
from methods import mapto, limit
from math import sqrt
def change_br(colour, brightness):
	if colour == 0:
		return 0
	else:
		return brightness

class Render():
	def __init__(self, points, viewdistance):
		self.size = SIZE
		self.points = points
		self.viewdistance = viewdistance
		
	def show(self):
		points = self.points
		length = len(points)
		size = self.size
		width, height = size[0], size[1]
		step = (width-200) // length#lines per points
		for i in range(0, step*length, step):
			cstep = (i // step) #which point to display
			#cstep = int(sqrt(length*cstep))
			# view distance and squared vd
			viewd = self.viewdistance
			sqrw = viewd**2 
			point = points[cstep]
			col = (0, 0, 0) # default colour black
			h=0 # defualt height none
			if points[cstep]:
				
				distance = points[cstep].distance[1]
				sqrd = distance**2

				# brightness value 0-1
				mb = mapto(sqrd, 0, sqrw, 1, 0)
				b = limit(mb, 0, 1) 
				#height value 0-halfheight
				mh = mapto(distance**0.5, 0, 200**0.5, 1, 0)
				h = limit(mh*height//2, 0, height//2)
				#colour set with brightness
				col = tuple(value*b for value in point.colour)
			#pygame.draw.line(screen, col, (x, 100-h), (x, 100+h), 2)
			x = i + 200 # where to place rect
			rect = pygame.Rect(x, height//2-h, step, h*2)
			pygame.draw.rect(screen, col, rect)