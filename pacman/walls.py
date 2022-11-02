from initial import SIZE
width, height = SIZE[0], SIZE[1]

#classes
from boundary import Boundary, BoundaryPolygon
#utility functions
from methods import flip_vectors, add_tuples, sub_tuples

def make_quad(pos, size):
    quadw, quadh = size
    vertices = [(0, 0), (quadw, 0), (quadw, quadh), (0, quadh)]
    vertices = list(add_tuples(pos, vec) for vec in vertices)
    quad = BoundaryPolygon(vertices, True)
    quad.set_colour((25, 25, 166))
    return quad


def make_tblock(pos, length, middlepos, orientation):
    midlength, midheight = middlepos
    tw = 1
    vertices = [(0, tw), (0, -tw), (length, -tw), (length, tw), (midlength+tw, tw), 
        (midlength+tw, midheight), (midlength-tw, midheight), (midlength-tw, tw)]
    if orientation in ('u', 'd'):
        vertices = list((x-length//2, y) for x, y in vertices)
        if orientation == 'u':
            vertices= flip_vectors(vertices, 'y', 0)
    else: 
        vertices = list((y, x) for x, y in vertices)
        vertices = list((x, y-length//2) for x, y in vertices)
        if orientation == 'l':
            vertices= flip_vectors(vertices, 'x', 0)

    vertices = list(add_tuples(vpos, pos) for vpos in vertices)
    tb = BoundaryPolygon(vertices, True)
    tb.set_colour((25, 25, 166))
    return tb


#colour values
wallcol = (25, 25, 166)
wallcoll = (30, 30, 170)

#walls
#top main
vertices = [(5,85), (45,85), (45,65), (5,65), (5, 5)]
vertices = vertices + flip_vectors(vertices, 'x', 100)[::-1] #flips and reverses order
topwalls = BoundaryPolygon(vertices, False)
topwalls.set_colour(wallcol)
#bottom main
vertices = flip_vectors(vertices, 'y', 100) # flips for bottom
bottomwalls = BoundaryPolygon(vertices, False)
bottomwalls.set_colour(wallcol)

#top quads
quads = []
quads.append(make_quad((20, 20), (20, 10)))
quads.append(make_quad((55, 20), (25, 10)))
quads.append(make_quad((180, 20), (-20, 10)))
quads.append(make_quad((145, 20), (-25, 10)))

quads.append(make_quad((20, 45), (20, 5)))
quads.append(make_quad((180, 45), (-20, 5)))

#top barriers
b1 = make_quad((96, 5), (8, 25))
#top 'T's
tb1 = make_tblock((100, 47), 40, (20, 20), 'd')
tb2 = make_tblock((62, 65), 40, (20, 20), 'r')
tb3 = make_tblock((138, 65), 40, (20, 20), 'l')

#ghost spawn
vertices = [(93, 88), (80, 88), (80, 112)]
vertices = vertices + flip_vectors(vertices, 'x', 100)[::-1]
gs = BoundaryPolygon(vertices, False)
gs.set_colour(wallcoll)

#bottom quads
quads.append(make_quad((60, 115), (3, 20)))
quads.append(make_quad((140, 115), (-3, 20)))

quads.append(make_quad((55, 150), (25, 5)))
quads.append(make_quad((145, 150), (-25, 5)))

#bottom 'T's
tb4 = make_tblock((100, 133), 40, (20, 15), 'd')
tb5 = make_tblock((100, 162), 40, (20, 18), 'd')
tb6 = make_tblock((50, 180), -55, (-20, 20), 'u')
tb7 = make_tblock((150, 180), 55, (20, 20), 'u')


wallobjects = [topwalls, bottomwalls] + quads + [b1, tb1, tb2, tb3, gs]
wallobjects += [tb4, tb5, tb6, tb7]
walls = []
for wall in wallobjects:
    try:
        walls += wall.boundarys
    except AttributeError:
        walls += [wall]