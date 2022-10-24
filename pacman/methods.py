from math import sqrt

#combines tuples through addition
def add_tuples(tuple1, tuple2):
	return tuple(v+tuple2[i] for i, v in enumerate(tuple1))

#combines tuples through subtraction
def sub_tuples(tuple1, tuple2):
	return tuple(v-tuple2[i] for i, v in enumerate(tuple1))

def abs_list(new_list):
	new_list = list(new_list)
	for i, value in enumerate(new_list):
		new_list[i] = abs(value)
	return tuple(new_list)
	
#sum will equal 1
def normalize_tuple(tuple1):
	new_list = []
	den = sum(abs_list(tuple1))
	for value in tuple1:
		new_list.append(value/den)
	return tuple(new_list)

def distance(pos1, pos2):
	xchange = abs(pos1[0]-pos2[0])
	ychange = abs(pos1[1]-pos2[1])
	return sqrt(xchange**2+ychange**2)

def mapto(v, a1, b1, a2, b2):
	v=a2 + (v-a1)/(b1 - a1) * (b2 - a2)
	return v

def limit(v, min, max):
	if v < min:
		return min
	elif v > max:
		return max
	else:
		return v

def flip_vectors(vectors, axis, centre):
	if axis == 'x':
		return list((2*centre-x, y) for x, y in vectors)
	elif axis == 'y':
		return list((x, 2*centre-y) for x, y in vectors)