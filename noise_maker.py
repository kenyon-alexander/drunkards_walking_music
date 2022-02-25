#!/usr/bin/python

import numpy as np
import random
from IPython.display import Audio

SAMPLING_FREQUENCY = 44100
DURATION = .25
FREQUENCY_VALUES = [
	261.626,
	277.183,
	293.665,
	311.127,
	329.628,
	349.228,
	369.994,
	391.995,
	415.305,
	440,
	466.164,
	493.883
]

def create_oscillators(pitch_list):
	time = np.arange(0,DURATION,1/SAMPLING_FREQUENCY)
	oscillator_list = []
	for pitch in pitch_list:
		oscillator_list.append(np.cos(2*np.pi*FREQUENCY_VALUES[pitch]*time))
	return oscillator_list

def flatten(t):
    return [item for sublist in t for item in sublist]