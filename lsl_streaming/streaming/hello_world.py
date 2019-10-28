"""
Author: zachandfox
Co-author: Will Schoonhalls
Source Materials: https://docs.openbci.com/OpenBCI%20Software/05-OpenBCI_Python#pyopenbci-installation
    - Keyboard Interrupt: https://stackoverflow.com/questions/4205317/capture-keyboardinterrupt-in-python-without-try-except

Pull in raw data from Cyton Board using bluetooth arduino
"""

from pyOpenBCI import OpenBCICyton
import time
import numpy as np

output = np.zeros(8)
timer = 1000
SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) #uV/count

print("Starting Script") 

# OpenBCICyton() will cause an OS exception if no OpenBCI port is connected
# TODO: wrap in an try, catch statement
board = OpenBCICyton()

MaxVal = 100000
StepInterval = 1


### start_stream method ###
#def print_raw(sample):
#    try:
#        #output.append(sample.channels_data)
#        print(sample.channels_data)
#        for i in range(1, MaxVal, StepInterval):
#            print(i)
#    except KeyboardInterrupt:
#        for i in range(1, MaxVal, StepInterval):
#            print('INTERRUPTED! Closing in: ', str(MaxVal-i))
#        board.stop_stream()
#
#board.start_stream(print_raw)
#print("Line 29")


### Write commands, while with keyboard interrupt ###
board.write_command('b')

while True:
    try:
        #output.append(board.parse_board_data().channels_data*SCALE_FACTOR_EEG)
        #output.append(board.parse_board_data().channels_data*SCALE_FACTOR_EEG)
        sample = board.parse_board_data().channels_data
        print(sample)
        sample_np = np.array(sample)
        print(sample_np)
        scaled_sample = sample_np*SCALE_FACTOR_EEG
        #print(type(scaled_sample))
        output = np.vstack((output,scaled_sample))
    except KeyboardInterrupt:
        board.stop_stream()
        print("Stream Stopped!")
        np.savetxt("output/sample.csv", output, delimiter=",")
        break

print("Script complete")


### While Loop Method ###
#board.write_command('b')
#
#while timer > 0:
#    #output.append(board.parse_board_data().channels_data*SCALE_FACTOR_EEG)
#    #output.append(board.parse_board_data().channels_data*SCALE_FACTOR_EEG)
#    sample = board.parse_board_data().channels_data
#    print(sample)
#    sample_np = np.array(sample)
#    print(sample_np)
#    scaled_sample = sample_np*SCALE_FACTOR_EEG
#    #print(type(scaled_sample))
#    output = np.vstack((output,scaled_sample))
#    timer = timer -1
#    print(timer)
#
##lol = board.parse_board_data()
##time.sleep(10)
#board.stop_stream()
##print(lol.channels_data)
#print(output)
#np.savetxt("output/sample.csv", output, delimiter=",")
#


