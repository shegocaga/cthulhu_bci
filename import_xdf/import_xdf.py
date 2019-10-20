"""
File: import_xdf.py
Author: zachandfox
Source Script: https://github.com/xdf-modules/xdf-python/blob/master/pyxdf/example.py 

Description: Import EEG stream data

# Authors: Christian Kothe & the Intheon pyxdf team
#          Tristan Stenner
#
# License: BSD (2-clause)
"""
import os
import logging
import pyxdf
import sys 
import pprint

pp = pprint.PrettyPrinter(indent=4)


logging.basicConfig(level=logging.DEBUG)  # Use logging.INFO to reduce output.
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:   
    # fname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'xdf_sample.xdf'))
    fname = '/Users/shegocaga/OpenBCI/assets/2019_09_11/sub-P001/ses-S001/eeg/sub-P001_ses-S001_task-Default_run-001_eeg.xdf'

streams, fileheader = pyxdf.load_xdf(fname)

pp.pprint(streams[0]['info'])

print("Found {} streams:".format(len(streams)))
for ix, stream in enumerate(streams):
    print("Stream {}: {} \n\t- type {} \n\t- uid {} \n\t- shape {} \n\t- at {} Hz (effective {} Hz)".format(
        ix + 1, stream['info']['name'][0],
        stream['info']['type'][0],
        stream['info']['uid'][0],
        (int(stream['info']['channel_count'][0]), len(stream['time_stamps'])),
        stream['info']['nominal_srate'][0],
        stream['info']['effective_srate'])
    )       
    if any(stream['time_stamps']):
        print("\t- Duration: {} s".format(stream['time_stamps'][-1] - stream['time_stamps'][0]))
print("Done.")

