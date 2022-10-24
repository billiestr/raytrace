from initial import screen, pygame, SIZE
swidth, sheight = SIZE[0], SIZE[1]
from math import sin, cos, radians, copysign
from methods import distance, add_tuples, limit
from ray import Ray

class Point():
	def __init__(self, pos, dist, colour):
		self.pos = pos
		self.distance = dist
		self.colour = colour
''' # tried to fix some perspective warping but caused too many issues
def root_map(maxvalue, value):
	return abs(value)**0.5 * (maxvalue/2)**0.5 * copysign(1, value)
'''

class Particle():
	def __init__(self, pos, angle, fov, raycount, viewdistance):
		start = angle - (fov//2)
		step = fov/raycount
		pointrange = list(v*step for v in range(start, start+raycount))
		rays = []
		for i in range(raycount):
			degree = start + i * step
			rad = radians(degree)
			rays.append(Ray(pos, (cos(rad), sin(rad)), degree))
		self.pos = pos
		self.rot = angle
		self.fov = fov
		self.count = raycount
		self.rays = rays
		rad = radians(angle+180)
		self.backray = Ray(pos, (cos(rad), sin(rad)), angle+180)
		self.vd = limit(viewdistance, 1, 1000)
		

	
	def set_rot(self, rot):
		self.rot = rot
		fov = self.fov
		start = int(rot - (fov//2))
		raycount = self.count
		step = fov/raycount
		rays = []
		for i in range(raycount):
			degree = start + i * step
			rad = radians(degree)
			rays.append(Ray(self.pos, (cos(rad), sin(rad)), degree))
		rad = radians(rot+180)
		self.backray = Ray(self.pos, (cos(rad), sin(rad)), rot+180)
		self.rays = rays
		

	def check_collision(self, direction, walls):
		if direction == 1:
			pt = self.rays[self.count//2].point
		elif direction == -1:
			backray = self.backray
			raypoints = []
			for wall in walls:
				point = backray.cast(wall)
				if point:
					dist = distance(point, self.pos)
					raypoints.append(Point(point, dist, (0, 0, 0)))
			if (len(raypoints) == 0):
				return False
			else:
				pt = sorted(raypoints, key=lambda x: x.distance)[0]
		return (pt and distance(self.pos, pt.pos) < 3)

	def check_interaction(self, colour):
		pt = self.rays[self.count//2].point
		return (pt and distance(self.pos, pt.pos) < 3 and pt.colour == colour)
			

	def move(self, amount, walls):
		direction = int(copysign(1, amount))
		if not self.check_collision(direction, walls):
			rad = radians(self.rot)
			normal = (cos(rad), sin(rad))
			vector = tuple(value*amount for value in normal)
			newpos = add_tuples(self.pos, vector)
			newpos = tuple(v % 200 for v in newpos)
			#newpos = tuple(limit(v, 1, sheight-2) for v in newpos)
			self.pos = newpos
			for ray in self.rays:
				ray.pos = newpos
		
	
	def update_points(self, walls, draw):
		for ray in self.rays:
			raypoints = []
			for wall in walls:
				point = ray.cast(wall)
				if point:
					dist = distance(point, self.pos)
					angle = ray.rot - self.rot
					dist2 = cos(radians(angle))*dist
					dist = (dist, dist2)
					col = wall.colour
					raypoints.append(Point(point, dist, col))
			if len(raypoints) == 0:
				ray.point = False
			else:
				raypoints=sorted(raypoints, key=lambda x: x.distance[0])
				ray.point = raypoints[0]
			
			if draw:
				if ray.point:
					pygame.draw.circle(screen, draw, ray.point.pos, 5)
	
	def get_points(self):
		points = []
		for ray in self.rays:
			points.append(ray.point)
		return points

	def show_ray(self, ray, colour, width):
		if ray.point:
			point = ray.point.pos
			pygame.draw.line(screen, colour, self.pos, point, width)

	def show(self, colour):
		for ray in self.rays:
			self.show_ray(ray, colour, 5)
	
	
	def set_pos(self, pos):
		self.pos = pos
		for ray in self.rays:
			ray.pos = pos


		
		