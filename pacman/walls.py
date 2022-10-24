from initial import SIZE
width, height = SIZE[0], SIZE[1]

#classes
from boundary import Boundary, BoundaryPolygon
#utility functions
from methods import flip_vectors, add_tuples

def make_quad(*args):
    pos, size, *colour = args
    quadw, quadh = size
    vertices = [(0, 0), (quadw, 0), (quadw, quadh), (0, quadh)]
    vertices = list(add_tuples(pos, vec) for vec in vertices)
    quad = BoundaryPolygon(vertices, True)
    if colour:
        quad.set_colour(colour[0])
    return quad

#colour values
wallcol = (25, 25, 166)

#walls
#top main
vertices = [(5,85), (45,85), (45,65), (5,65), (5, 5)]
vertices = vertices + flip_vectors(vertices, 'x')[::-1] #flips and reverses order
topwalls = BoundaryPolygon(vertices, False)
topwalls.set_colour(wallcol)
#bottom main
vertices = flip_vectors(vertices, 'y') # flips for bottom
bottomwalls = BoundaryPolygon(vertices, False)
bottomwalls.set_colour(wallcol)

#quads
quads = []
quads.append(make_quad((20, 20), (20, 10), wallcol))
quads.append(make_quad((55, 20), (30, 10), wallcol))
wallobjects = [topwalls, bottomwalls] + quads
walls = []
for wall in wallobjects:
    walls += wall.boundarys