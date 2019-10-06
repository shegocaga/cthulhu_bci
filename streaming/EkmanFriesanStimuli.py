'''
Author: William Schoenhals

Purpose: Generate sequence of stimuli, faces from Ekman and Friesan paper 'Pictures of Facial Affect' (1976), exposure
 to reproduce Mahler and Reder paper:
 'Emoional Face Recognition and EEG Measures' University of British Columbia
 Save data to .csv with format [stimuli, time_start]

There are four possible face stimuli, not counting the grey netural screen, which will be presented. Within the four
faces there are three emotional expressions (Anger, Sad, Fear) and one Neutral face. The distinction is important.

Per Mahler and Reder:
'The stimulus [faces] was presented for 500ms on the monitor with an interstimulus interval parameter (ISI) of 2000 ms'
Each stimulus is presented 20 times. Order is randomized per seed.

'''

import numpy as np

# create list of simulit
STIMULI = ['neutral', 'happy', 'sad', 'fear']
INTERVAL = 'blank'

# assign presentation time in ms
STIMULI_PRES_TIME = 500
BLANK_PRES_TIME = 2000

# Assign number of exposures for each stimuli
STIMULI_PRES_EXPOSURE = 20

# create experiment stimuli list with header info
STIMULI_LIST = ['stimuli,time_start\n']

# always start experiment with 2000 ms of blank screen
STIMULI_LIST.append(INTERVAL + ',' + str(0) + '\n')
exp_time = 2000
# create list of stimuli and randomize
non_random_stim_list = []
for stim in STIMULI:
    for i in range(0, STIMULI_PRES_EXPOSURE, 1):
        non_random_stim_list.append(stim)

np.random.shuffle(non_random_stim_list)
random_stim_list = non_random_stim_list

# assign times to the randomized stimuli list
for ran_stim in random_stim_list:
    STIMULI_LIST.append(ran_stim + ',' + str(exp_time) + '\n')
    exp_time = exp_time + STIMULI_PRES_TIME
    STIMULI_LIST.append(INTERVAL + ',' + str(exp_time) + '\n')
    exp_time = exp_time + BLANK_PRES_TIME

# save as csv
file_path = 'C:\\Users\\Will\\Desktop\\BCI\\Face Recognition'
file_name = file_path + '\\' + 'EkmanFriesanSimuli.csv'
fp = open(file_name, 'w')
for line in STIMULI_LIST:
    fp.write(line)
fp.close()






