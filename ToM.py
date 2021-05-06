#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Thu 06 May 2021 04:09:03 AM EEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.3'
expName = 'ToM'  # from the Builder filename that created this script
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
    originPath='/home/dude/Documents/psychological_tests/Theory of Mind/ToM.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
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

# Initialize components for Routine "instr"
instrClock = core.Clock()
'''import os
from random import sample,shuffle
with open('.' + os.sep + 'TomVideos' + os.sep + 'videoList.csv') as f:
    lines = f.readlines()
 
x = []
for line in lines:
    x.append(line.split(','))
    
    con_indices =   [i-1 for i in range(len(x)) if x[i][2]=='1'] 
    incon_indices = [i-1 for i in range(len(x)) if x[i][2]=='0']

# Balancing congruent & incongruent trials
# Testing
repIndices = sample(con_indices, 1) + sample(incon_indices, 1)

shuffle(repIndices)'''
'''
Code to not have more than two similar stories 
appearing consecutively
Hard-coded for 96 stimuli
'''
x = [[i for i in range(12)], 
     [i for i in range(12,24)], 
     [i for i in range(24,36)], 
     [i for i in range(36,48)], 
     [i for i in range(48,60)], 
     [i for i in range(60,72)], 
     [i for i in range(72,84)], 
     [i for i in range(84,96)]]  

repIndices = []


rows = [i for i in range(8)]
cols = [i for i in range(12)]

for col in cols:
    shuffle(x) # Shuffles row-wise
    for row in rows: 
        shuffle(x[row]) # Shuffle column-wise
        if len(x[row])>0: #
            temp = x[row].pop(-1)
            #temp = x[row].pop(randint(0,len(x[row])-1))
            repIndices.append(temp)
# Production - Uncomment lines below
# sample_num = min(len(con_indices), len(incon_indices))
# repIndices  = sample(con_indices, sample_num) + sample(incon_indices, sample_num)
# Uncomment if necessary
text = visual.TextStim(win=win, name='text',
    text='Put instructions here',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
preloadfVid = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='preloadfVid')
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
correct = visual.ImageStim(
    win=win,
    name='correct', 
    image='true.png', mask=None,
    ori=0.0, pos=(0.4,0), size=(0.1,0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='false.png', mask=None,
    ori=0.0, pos=(-0.4,0), size=(0.1,0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
instrComponents = [text, mouse_2]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TomVideos/videoList.csv', selection=repIndices),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    fVid = visual.MovieStim3(
        win=win, name='fVid',
        noAudio = False,
        filename=firstVideo,
        ori=0.0, pos=(0, 0), opacity=1.0,
        loop=False,
        depth=-1.0,
        )
    sVid = visual.MovieStim3(
        win=win, name='sVid',
        noAudio = False,
        filename=secondVideo,
        ori=0.0, pos=(0, 0), opacity=1.0,
        loop=False,
        depth=-3.0,
        )
    #flag = False
    #if fVid.status==STARTED and flag==False:
    on_flag_fvid = False
    on_flag_svid = False
    mouse.setVisible(False)
    
    # Flags to keep video times
    
    #thisExp.addData('firstVideo.started ', globalClock.getTime() + fixation1_stopped)
    
    
    
    #flag = True
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trial_1Components = [fix1, fVid, fix2, sVid, preloadfVid, mouse, correct, incorrect]
    for thisComponent in trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_1"-------
    while continueRoutine:
        # get current time
        t = trial_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            fix1.setAutoDraw(True)
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
                fix1.setAutoDraw(False)
        
        # *fVid* updates
        if fVid.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            fVid.frameNStart = frameN  # exact frame index
            fVid.tStart = t  # local t and not account for scr refresh
            fVid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fVid, 'tStartRefresh')  # time at next scr refresh
            fVid.setAutoDraw(True)
        
        # *fix2* updates
        if fix2.status == NOT_STARTED and asarray(fVid.status==FINISHED):
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            fix2.setAutoDraw(True)
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
                fix2.setAutoDraw(False)
        
        # *sVid* updates
        if sVid.status == NOT_STARTED and asarray(fix2.status==FINISHED):
            # keep track of start time/frame for later
            sVid.frameNStart = frameN  # exact frame index
            sVid.tStart = t  # local t and not account for scr refresh
            sVid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sVid, 'tStartRefresh')  # time at next scr refresh
            sVid.setAutoDraw(True)
        
        if fVid.status==FINISHED and on_flag_fvid == False:
            fVid.tStopRefresh = tThisFlipGlobal
            on_flag_fvid = True
            
        if sVid.status==FINISHED and on_flag_svid == False:
            sVid.tStopRefresh = tThisFlipGlobal
            on_flag_svid = True
            mouse.setPos(newPos=(0,0))
            mouse.setVisible(True)
            
        
            #thisExp.addData('firstVideo.started ', globalClock.getTime() + fixation1_stopped)
        # *mouse* updates
        if mouse.status == NOT_STARTED and asarray(sVid.status==FINISHED):
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [correct,incorrect]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *correct* updates
        if correct.status == NOT_STARTED and asarray(sVid.status==FINISHED):
            # keep track of start time/frame for later
            correct.frameNStart = frameN  # exact frame index
            correct.tStart = t  # local t and not account for scr refresh
            correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct, 'tStartRefresh')  # time at next scr refresh
            correct.setAutoDraw(True)
        
        # *incorrect* updates
        if incorrect.status == NOT_STARTED and asarray(sVid.status==FINISHED):
            # keep track of start time/frame for later
            incorrect.frameNStart = frameN  # exact frame index
            incorrect.tStart = t  # local t and not account for scr refresh
            incorrect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incorrect, 'tStartRefresh')  # time at next scr refresh
            incorrect.setAutoDraw(True)
        # *preloadfVid* period
        if preloadfVid.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preloadfVid.frameNStart = frameN  # exact frame index
            preloadfVid.tStart = t  # local t and not account for scr refresh
            preloadfVid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preloadfVid, 'tStartRefresh')  # time at next scr refresh
            preloadfVid.start(1.5)
        elif preloadfVid.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *preloadfVid*
            fVid.setMovie(firstVideo)
            sVid.setMovie(secondVideo)
            # component updates done
            preloadfVid.complete()  # finish the static period
            preloadfVid.tStop = preloadfVid.tStart + 1.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_1"-------
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix1.started', fix1.tStartRefresh)
    trials.addData('fix1.stopped', fix1.tStopRefresh)
    fVid.stop()
    trials.addData('fix2.started', fix2.tStartRefresh)
    trials.addData('fix2.stopped', fix2.tStopRefresh)
    sVid.stop()
    thisExp.addData('fVid.started',  fVid.tStartRefresh)
    thisExp.addData('sVid.started', sVid.tStartRefresh)
    
    thisExp.addData('fVid.stopped', fVid.tStopRefresh)
    thisExp.addData('sVid.stopped', sVid.tStopRefresh)
    
    
    trials.addData('preloadfVid.started', preloadfVid.tStart)
    trials.addData('preloadfVid.stopped', preloadfVid.tStop)
    # store data for trials (TrialHandler)
    if len(mouse.x): trials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials.addData('mouse.started', mouse.tStartRefresh)
    trials.addData('mouse.stopped', mouse.tStopRefresh)
    trials.addData('correct.started', correct.tStartRefresh)
    trials.addData('correct.stopped', correct.tStopRefresh)
    trials.addData('incorrect.started', incorrect.tStartRefresh)
    trials.addData('incorrect.stopped', incorrect.tStopRefresh)
    # the Routine "trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
