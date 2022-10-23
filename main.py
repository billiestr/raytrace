from initial import screen, SIZE
import pygame
from pygame.locals import (QUIT, 
	KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_RIGHT, K_i, K_o)
from particle import Particle
from boundary import Boundary, BoundaryPolygon
from render import Render
print('loading')
#colour values
white, black = (255, 255, 255), (0, 0, 0)
r, g, b = (255, 0, 0), (0, 255, 0), (0, 0, 255)
y, c, m = (255, 255, 0), (0, 255, 255), (255, 0, 255)
#line
b1 = Boundary((50, 160), (165, 186))
b1.colour = g
#quadrilateral
vertices = [(20, 30), (70, 30), (70, 80), (20, 80)]
bp1 = BoundaryPolygon(vertices, True)
bp1.set_colour(b)
#triangle
vertices = [(160, 150), (170, 30), (110, 130)]
bp2 = BoundaryPolygon(vertices, False)
bp2.set_colour(r)
#ray caster
p1 = Particle((50, 100), 0, 80, 20, 200)

#bounds
#vertices = [(0, 0), (SIZE[0]//2, 0), (SIZE[0]//2, SIZE[1]), (0, SIZE[1])]
vertices = [(0, 0), (200, 0), (200, SIZE[1]), (0, SIZE[1])]
bound = BoundaryPolygon(vertices, True)
bound.set_colour(white)

ROTVELOCITY = .8
MOVEVELOCITY = .2
walls = bp1.boundarys+bp2.boundarys+bound.boundarys+[b1]
done = False
print('drawing')
while not done:
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
	keys = pygame.key.get_pressed()
	if keys[K_LEFT]:
		p1.set_rot(p1.rot-ROTVELOCITY)
	if keys[K_RIGHT]:
		p1.set_rot(p1.rot+ROTVELOCITY)
	if keys[K_UP]:
		p1.move(MOVEVELOCITY, walls)
	if keys[K_DOWN]:
			p1.move(-MOVEVELOCITY, walls)
	if keys[K_i] and p1.vd>1:
			p1.vd -= 1
	if keys[K_o]:
			p1.vd += 1
	
	#logic code

	screen.fill(black)
	p1.update_points(walls, False)
	r = Render(p1.get_points(), p1.vd)
	
	#p1.set_pos(pygame.mouse.get_pos())
	#draw code
	
	r.show()
	b1.show()
	bp1.show()
	bp2.show()
	p1.show(y)
	p1.show_ray(p1.rays[len(p1.rays)//2], c, 2)
	pygame.display.update()
	

pygame.quit()
exit('bye bye!')