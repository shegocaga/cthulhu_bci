#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: zachandfox
Description:
    Set up Ekman and Friesan faces experiment:
    -   Display faces with known reactions using PsychoPy, export event
        timestamps to LSL 
    -   Record Reaction of faces (using OpenBCI + LSL)  

This experiment was (initially) created using PsychoPy3 Experiment Builder (v3.2.0),
    on Sun Sep  8 17:22:44 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet # Import LSL streaming library

# setup realitive asset folder path
one_folder_up = os.path.abspath(os.path.join(__file__,"../../../.."))
asset_folder = one_folder_up + '/assets_cthulhu_bci/psychopy_experiments/ekman_and_friesan_faces'

suspicious_image_path = asset_folder + '/suspicious.png'
confident_image_path = asset_folder + '/confident.png'

# Set up stream to LSL
stream_info = StreamInfo(name='psychopy_stimuli', type='Markers', channel_count=1, channel_format='int32', source_id='psychopy')
outlet = StreamOutlet(stream_info) # Initialize Stream
stimuli_status = 0

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.0'
expName = 'ekman_and_friesan_faces'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/shegocaga/OpenBCI/cthulhu_bci/psychopy_experiments/ekman_and_friesan_faces/ekman_and_friesan_faces_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
suspicious = visual.ImageStim(
    win=win,
    name='suspicious', 
    image=suspicious_image_path, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
confident = visual.ImageStim(
    win=win,
    name='confident', 
    image= confident_image_path, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [suspicious, confident]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    if (suspicious.status == 1 or confident.status == 1):
        stimuli_status = 1
    else:
        stimuli_status = 0
    
#    print(('continueRoutine = {} \n   '+
#        't = {} \n   '+
#        'tThisFlip = {} \n   '+
#        'tThisFlipGlobal = {} \n   '+
#        'frameN = {} \n   '+
#        'suspicious.status = {} \n   '+
#        'confident.status = {} \n   '+
#        '-----------------------------------------').format(continueRoutine, t, tThisFlip, tThisFlipGlobal, frameN, suspicious.status, confident.status))
    # *suspicious* updates
    if suspicious.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        suspicious.frameNStart = frameN  # exact frame index
        suspicious.tStart = t  # local t and not account for scr refresh
        suspicious.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(suspicious, 'tStartRefresh')  # time at next scr refresh
        suspicious.setAutoDraw(True)
    if suspicious.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > suspicious.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            suspicious.tStop = t  # not accounting for scr refresh
            suspicious.frameNStop = frameN  # exact frame index
            win.timeOnFlip(suspicious, 'tStopRefresh')  # time at next scr refresh
            suspicious.setAutoDraw(False)
    
    # *confident* updates
    if confident.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        confident.frameNStart = frameN  # exact frame index
        confident.tStart = t  # local t and not account for scr refresh
        confident.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confident, 'tStartRefresh')  # time at next scr refresh
        confident.setAutoDraw(True)
    if confident.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > confident.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            confident.tStop = t  # not accounting for scr refresh
            confident.frameNStop = frameN  # exact frame index
            win.timeOnFlip(confident, 'tStopRefresh')  # time at next scr refresh
            confident.setAutoDraw(False)
    
    print(stimuli_status)
    outlet.push_sample(x=[stimuli_status])

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('suspicious.started', suspicious.tStartRefresh)
thisExp.addData('suspicious.stopped', suspicious.tStopRefresh)
thisExp.addData('confident.started', confident.tStartRefresh)
thisExp.addData('confident.stopped', confident.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
