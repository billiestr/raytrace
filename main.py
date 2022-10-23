from initial import screen, SIZE
width, height = SIZE[0], SIZE[1]

#pygame
import pygame
from pygame.locals import (QUIT, 
	KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_RIGHT, K_i, K_o)

#classes
from particle import Particle
from boundary import Boundary, BoundaryPolygon
from render import Render

print('loading')
#colour values
white, black = (255, 255, 255), (0, 0, 0)
r, g, b = (255, 0, 0), (0, 255, 0), (0, 0, 255)
y, c, m = (255, 255, 0), (0, 255, 255), (255, 0, 255)
pink, brown = (255, 50, 50), (139, 64, 0)
#line
b1 = Boundary((50, 160), (165, 186))
b1.colour = g
#quadrilateral
vertices = [(20, 30), (70, 30), (70, 80), (20, 80)]
square = BoundaryPolygon(vertices, True)
square.set_colour(b)

#house
vertices = [(50, 220), (20, 220), (20, 380), (180, 380), (180, 220), (90, 220), (90, 290), (150, 290), (150, 230)]
housewalls = BoundaryPolygon(vertices, False)
housewalls.set_colour(b)
wardrobe = BoundaryPolygon(((110,220), (110,222), (120, 222), (120, 220)), False)
wardrobe.set_colour(brown)
house = housewalls.boundarys + wardrobe.boundarys

#triangle
vertices = [(160, 150), (170, 30), (110, 130)]
triangle = BoundaryPolygon(vertices, False)
triangle.set_colour(r)


#ray caster
# start pos, start angle, fov, ray count, view distance
p1 = Particle((50, 100), 0, 80, 1000, 200)

#bounds
#vertices = [(0, 0), (width//2, 0), (width//2, height), (0, height)]
vertices = [(0, 0), (200, 0), (200, height), (0, height)]
bound = BoundaryPolygon(vertices, True)
bound.set_colour(white)

clock = pygame.time.Clock()
ROTVELOCITY = .1
MOVEVELOCITY = .05
walls = square.boundarys+triangle.boundarys+bound.boundarys+house+[b1]
done = False
print('drawing')
while not done:
	tm = clock.tick(60)
	movev = MOVEVELOCITY * tm
	rotv = ROTVELOCITY * tm
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
	keys = pygame.key.get_pressed()
	if keys[K_LEFT]:
		p1.set_rot(p1.rot-rotv)
	if keys[K_RIGHT]:
		p1.set_rot(p1.rot+rotv)
	if keys[K_UP]:
		p1.move(movev, walls)
	if keys[K_DOWN]:
			p1.move(-movev, walls)
	if keys[K_i] and p1.vd>1:
			p1.vd -= 1
	if keys[K_o]:
			p1.vd += 1
	
	#logic code

	
	p1.update_points(walls, False)
	r = Render(p1.get_points(), p1.vd)

	#draw code
	screen.fill(black)
	r.show()
	b1.show()
	square.show()
	triangle.show()
	#house
	housewalls.show()
	wardrobe.show()
	#raycaster
	p1.show(y)
	p1.show_ray(p1.rays[len(p1.rays)//2], c, 2)
	pygame.display.update()
	

pygame.quit()
exit('bye bye!')