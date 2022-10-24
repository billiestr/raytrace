from re import M
from initial import screen, SIZE
width, height = SIZE[0], SIZE[1]
#
#pygame
import pygame
from pygame.locals import (QUIT, 
	KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_RIGHT, K_i, K_o)

#classes
from particle import Particle
from boundary import Boundary, BoundaryPolygon
from render import Render
from methods import flip_vectors

print('loading')
#colour values
white, black = (255, 255, 255), (0, 0, 0)
r, g, b = (255, 0, 0), (0, 255, 0), (0, 0, 255)
y, c, m = (255, 255, 0), (0, 255, 255), (255, 0, 255)
wallcol = (25, 25, 166)
pacmancol = (255, 255, 0)
pink, brown = (255, 50, 50), (139, 64, 0)

#walls
vertices = [(5,85), (45,85), (45,65), (5,65), (5, 5)]
vertices = vertices + flip_vectors(vertices, 'x')[::-1] #flips and reverses order
topwalls = BoundaryPolygon(vertices, False)
topwalls.set_colour((25, 25, 166))
vertices = flip_vectors(vertices, 'y') # flips for bottom
bottomwalls = BoundaryPolygon(vertices, False)
bottomwalls.set_colour((25, 25, 166))

walls = topwalls.boundarys + bottomwalls.boundarys

#teleports
tp1 = BoundaryPolygon(((5,85), (-3,85), (-3,115), (5,115)), False)
tp2 = BoundaryPolygon(((195,85), (203,85), (203,115), (195,115)), False)
#ghosts 
ghostnames = ['Blinky', 'Pinky', 'Inky', 'Clyde']	
ghostcolours = [(255, 0, 0), (255, 184, 255), (0, 255, 255), (255, 184, 82)]
#player
# start pos, start angle, fov, ray count, view distance
player = Particle((50, 100), 0, 80, 1000, 200)

#bounds
#vertices = [(0, 0), (width//2, 0), (width//2, height), (0, height)]
vertices = [(0, 0), (200, 0), (200, 200), (0, 200)]
bound = BoundaryPolygon(vertices, True)
bound.set_colour(white)

clock = pygame.time.Clock()
ROTVELOCITY = .1
MOVEVELOCITY = .04
boundarys = walls + tp1.boundarys + tp2.boundarys

print('drawing')
bgcolour = black
done = False
while not done:
	tm = clock.tick(60)
	movev = MOVEVELOCITY * tm
	rotv = ROTVELOCITY * tm
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
	keys = pygame.key.get_pressed()
	if keys[K_UP]:
		player.move(movev, boundarys)
	if keys[K_DOWN]:
			player.move(-movev, boundarys)
	if keys[K_LEFT]:
		player.set_rot(player.rot-rotv)
	if keys[K_RIGHT]:
		player.set_rot(player.rot+rotv)
	if keys[K_i] and player.vd>1:
			player.vd -= 1
	if keys[K_o]:
			player.vd += 1
	
	#logic code

	
	player.update_points(boundarys, False)
	r = Render(player.get_points(), player.vd)

	
	#draw code
	screen.fill(bgcolour)
	r.show()
	#raycaster
	player.show((10, 10, 10))
	player.show_ray(player.rays[len(player.rays)//2], y, 2)
	#walls
	topwalls.show()
	bottomwalls.show()
	#selection
	
	pygame.display.update()
	

pygame.quit()
exit('bye bye!')