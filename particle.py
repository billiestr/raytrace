from initial import screen, pygame
from math import sin, cos, radians, atan
from methods import distance, add_tuples, limit
from ray import Ray

class Point():
	def __init__(self, pos, dist, colour):
		self.pos = pos
		self.distance = dist
		self.colour = colour



class Particle():
	
	def __init__(self, pos, angle, fov, raycount, viewdistance):
		start = angle - (fov//2)
		rays = []
		for degree in range(start, start+fov, fov//raycount):
			rad = radians(degree)
			rays.append(Ray((pos), (cos(rad), sin(rad)), degree))
		self.pos = pos
		self.rot = angle
		self.fov = fov
		self.count = raycount
		self.rays = rays
		self.vd = limit(viewdistance, 1, 1000)
		

	
	def set_rot(self, rot):
		self.rot = rot
		fov = self.fov
		start = int(rot - (fov//2))
		raycount = self.count
		step = fov//raycount
		rays = []
		for i, ray in enumerate(self.rays):
			degree = start + i * step
			rad = radians(degree)
			rays.append(Ray(self.pos, (cos(rad), sin(rad)), degree))
		self.rays = rays
		

	def move(self, amount, walls):
		ray = self.rays[self.count//2]
		pt = ray.point
		if pt:
			dist = distance(pt.pos, self.pos)
			if dist > 2:
				rad = radians(self.rot)
				normal = (cos(rad), sin(rad))
				vector = tuple(value*amount for value in normal)
				newpos = add_tuples(self.pos, vector)
				newpos = tuple(limit(v, 1, 200) for v in newpos)
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


		
		