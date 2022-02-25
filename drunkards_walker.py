#!/usr/bin/python

import numpy as np
import random
#import drunkards_helper

ITERATIONS = 1000

def create_drunkards_walking_music(pitch_sets, distance_matrix):
	current_set = random.randint(0,len(pitch_sets)-1)
	drunkards_walking_music = [pitch_sets[current_set]]
	for i in range(ITERATIONS):
		r = random.uniform(0,1)
		j = 0
		while distance_matrix[current_set][j] < r:
			j +=1
		drunkards_walking_music.append(list(pitch_sets[j]))
		current_set = j
	return(drunkards_walking_music)

# if __name__ == "__main__":
# 	pitch_sets = drunkards_helper.create_pitch_sets(
# 		drunkards_helper.FULL_PITCH_SETS
# 	)
# 	distance_matrix = drunkards_helper.create_distance_matrix(pitch_sets)
# 	drunkards_walking_music = create_drunkards_walking_music(
# 		pitch_sets, 
# 		distance_matrix
# 	)
# 	print(drunkards_walking_music)

if __name__ == "__main__":
	pitch_sets = create_pitch_sets(
		FULL_PITCH_SETS
	)
	distance_matrix = create_distance_matrix(pitch_sets)
	drunkards_walking_music = create_drunkards_walking_music(
		pitch_sets, 
		distance_matrix
	)
	oscillator_list = create_oscillators(flatten(drunkards_walking_music))
    
Audio(flatten(oscillator_list),rate=SAMPLING_FREQUENCY,autoplay=True)