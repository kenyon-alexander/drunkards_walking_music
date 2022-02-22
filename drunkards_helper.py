#!/usr/bin/python

import numpy as np

FULL_PITCH_SETS = 'full_pitch_sets.txt'
SIMPLE_PITCH_SETS = 'simple_pitch_sets.txt'

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
