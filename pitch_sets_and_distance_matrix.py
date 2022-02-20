#!/usr/bin/python

import numpy as np

SETS_FILENAME = 'pitch_set_strings.txt'

simple_pitch_sets = [set([1,2,3]),set([1,3,4]),set([2,3,4]),set([3,4,5])]

def create_pitch_sets(sets_filename):
	with open(sets_filename) as file:
	    lines = [set(line.rstrip()) for line in file]
	return lines

def create_distance_matrix(pitch_sets):
	distance_matrix = []
	for i in range(len(pitch_sets)):
		row = []
		for j in range(len(pitch_sets)):
			row.append(len(pitch_sets[i].intersection(pitch_sets[j])))
		row_sum = sum(row)
		row = np.array(row,dtype='f')/row_sum
		row = np.cumsum(row)
		distance_matrix.append(list(row))
	return(distance_matrix)



if __name__ == "__main__":
	full_pitch_set = create_pitch_sets(SETS_FILENAME)
	print(create_distance_matrix(full_pitch_set))
