#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on February 16, 2018, at 13:23
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('1.85.6')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PC_ChEC_movie_scanner_1.0'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'', u'mode': u'scanner', u'version': u'PC'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\iView X\\Desktop\\ChEC\\chec\\scanner_version\\PC_ChEC_movie_scanner_1.0.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "waitscreen"
waitscreenClock = core.Clock()
waitimage = visual.ImageStim(
    win=win, name='waitimage',
    image=u'C:\\Users\\iView X\\Desktop\\ChEC\\stimuli\\waitslide.png', mask=None,
    ori=0, pos=(0, 0), size=[5.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "playmovie"
playmovieClock = core.Clock()
kingjulian = visual.MovieStim3(
    win=win, name='kingjulian',
    noAudio = False,
    filename='C:\\Users\\iView X\\Desktop\\ChEC\\stimuli\\AHKJ_S01E02.mp4',
    ori=0, pos=(0, 0), opacity=1,
    depth=0.0,
    )

# Initialize components for Routine "thankyou"
thankyouClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "waitscreen"-------
t = 0
waitscreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
prepforscan = event.BuilderKeyResponse()
# keep track of which components have finished
waitscreenComponents = [waitimage, prepforscan]
for thisComponent in waitscreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "waitscreen"-------
while continueRoutine:
    # get current time
    t = waitscreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *waitimage* updates
    if t >= 0.0 and waitimage.status == NOT_STARTED:
        # keep track of start time/frame for later
        waitimage.tStart = t
        waitimage.frameNStart = frameN  # exact frame index
        waitimage.setAutoDraw(True)
    
    # *prepforscan* updates
    if t >= 0.0 and prepforscan.status == NOT_STARTED:
        # keep track of start time/frame for later
        prepforscan.tStart = t
        prepforscan.frameNStart = frameN  # exact frame index
        prepforscan.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(prepforscan.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if prepforscan.status == STARTED:
        theseKeys = event.getKeys(keyList=['equal'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            prepforscan.keys = theseKeys[-1]  # just the last key pressed
            prepforscan.rt = prepforscan.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitscreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "waitscreen"-------
for thisComponent in waitscreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if prepforscan.keys in ['', [], None]:  # No response was made
    prepforscan.keys=None
thisExp.addData('prepforscan.keys',prepforscan.keys)
if prepforscan.keys != None:  # we had a response
    thisExp.addData('prepforscan.rt', prepforscan.rt)
thisExp.nextEntry()
# the Routine "waitscreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "playmovie"-------
t = 0
playmovieClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1284.000000)
# update component parameters for each repeat
premature_quit = event.BuilderKeyResponse()
# keep track of which components have finished
playmovieComponents = [kingjulian, premature_quit]
for thisComponent in playmovieComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "playmovie"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = playmovieClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *kingjulian* updates
    if t >= 0.0 and kingjulian.status == NOT_STARTED:
        # keep track of start time/frame for later
        kingjulian.tStart = t
        kingjulian.frameNStart = frameN  # exact frame index
        kingjulian.setAutoDraw(True)
    frameRemains = 0.0 + 1284- win.monitorFramePeriod * 0.75  # most of one frame period left
    if kingjulian.status == STARTED and t >= frameRemains:
        kingjulian.setAutoDraw(False)
    if kingjulian.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *premature_quit* updates
    if t >= 0.0 and premature_quit.status == NOT_STARTED:
        # keep track of start time/frame for later
        premature_quit.tStart = t
        premature_quit.frameNStart = frameN  # exact frame index
        premature_quit.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(premature_quit.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 1284- win.monitorFramePeriod * 0.75  # most of one frame period left
    if premature_quit.status == STARTED and t >= frameRemains:
        premature_quit.status = STOPPED
    if premature_quit.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            premature_quit.keys = theseKeys[-1]  # just the last key pressed
            premature_quit.rt = premature_quit.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in playmovieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "playmovie"-------
for thisComponent in playmovieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if premature_quit.keys in ['', [], None]:  # No response was made
    premature_quit.keys=None
thisExp.addData('premature_quit.keys',premature_quit.keys)
if premature_quit.keys != None:  # we had a response
    thisExp.addData('premature_quit.rt', premature_quit.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "thankyou"-------
t = 0
thankyouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thankyouComponents = [text]
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thankyou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thankyouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thankyou"-------
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
