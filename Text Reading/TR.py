#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Thu 06 May 2021 04:37:11 AM EEST
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
expName = 'TR'  # from the Builder filename that created this script
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
    originPath='/home/dude/Documents/psychological_tests/Text Reading/TR.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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
instrText = visual.TextStim(win=win, name='instrText',
    text='1) Διάβασε το κείμενο.\n2) Διάβασε την ερώτηση που ακολουθεί.\n3) Κάνε κλικ στη σωστή απάντηση\n\nΌταν είσαι έτοιμος/η, κάνε κλικ για να ξεκινήσεις ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "ready"
readyClock = core.Clock()
getReady = visual.TextStim(win=win, name='getReady',
    text='Ετοιμάσου!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse.setPos([0,0])
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.22), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
q = visual.TextStim(win=win, name='q',
    text='',
    font='Open Sans',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
a1 = visual.TextStim(win=win, name='a1',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.22), height=0.03, wrapWidth=0.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
a2 = visual.TextStim(win=win, name='a2',
    text='',
    font='Open Sans',
    pos=(0.4, -0.22), height=0.03, wrapWidth=0.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
a3 = visual.TextStim(win=win, name='a3',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.37), height=0.03, wrapWidth=0.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
a4 = visual.TextStim(win=win, name='a4',
    text='',
    font='Open Sans',
    pos=(0.4,-0.37), height=0.03, wrapWidth=0.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
resp = event.Mouse(win=win)
x, y = [None, None]
resp.mouseClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',units='height', 
    width=(0.15,0.15)[0], height=(0.15,0.15)[1],
    ori=0.0, pos=(-1/2*win.size[0]/win.size[1]+.075, -0.425),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
instrComponents = [instrText, mouse]
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
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
textTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('first.csv'),
    seed=None, name='textTrials')
thisExp.addLoop(textTrials)  # add the loop to the experiment
thisTextTrial = textTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTextTrial.rgb)
if thisTextTrial != None:
    for paramName in thisTextTrial:
        exec('{} = thisTextTrial[paramName]'.format(paramName))

for thisTextTrial in textTrials:
    currentLoop = textTrials
    # abbreviate parameter names if possible (e.g. rgb = thisTextTrial.rgb)
    if thisTextTrial != None:
        for paramName in thisTextTrial:
            exec('{} = thisTextTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready"-------
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    # keep track of which components have finished
    readyComponents = [getReady]
    for thisComponent in readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = readyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=readyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *getReady* updates
        if getReady.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            getReady.frameNStart = frameN  # exact frame index
            getReady.tStart = t  # local t and not account for scr refresh
            getReady.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getReady, 'tStartRefresh')  # time at next scr refresh
            getReady.setAutoDraw(True)
        if getReady.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > getReady.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                getReady.tStop = t  # not accounting for scr refresh
                getReady.frameNStop = frameN  # exact frame index
                win.timeOnFlip(getReady, 'tStopRefresh')  # time at next scr refresh
                getReady.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready"-------
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    textTrials.addData('getReady.started', getReady.tStartRefresh)
    textTrials.addData('getReady.stopped', getReady.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    questionTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(questionsAndAnswers),
        seed=None, name='questionTrials')
    thisExp.addLoop(questionTrials)  # add the loop to the experiment
    thisQuestionTrial = questionTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
    if thisQuestionTrial != None:
        for paramName in thisQuestionTrial:
            exec('{} = thisQuestionTrial[paramName]'.format(paramName))
    
    for thisQuestionTrial in questionTrials:
        currentLoop = questionTrials
        # abbreviate parameter names if possible (e.g. rgb = thisQuestionTrial.rgb)
        if thisQuestionTrial != None:
            for paramName in thisQuestionTrial:
                exec('{} = thisQuestionTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        import random
        
        # Shuffle answers to appear at random positions each time
        # Uncomment if needed
        #ansList = [ans1, ans2, ans3, ans4]
        #random.shuffle(ansList)
        #ans4 = ansList.pop(-1)
        #ans3 = ansList.pop(-1)
        #ans2 = ansList.pop(-1)
        #ans1 = ansList.pop(-1)
        
        
        colorList = ['red', 'green', 'blue', (255,255,0)]
        random.shuffle(colorList)
        c1 = colorList[0]
        c2 = colorList[1]
        c3 = colorList[2]
        c4 = colorList[3]
        text.setText(textStim)
        q.setText(question)
        a1.setColor(c1, colorSpace='rgb')
        a1.setText(ans1)
        a2.setColor(c2, colorSpace='rgb')
        a2.setText(ans2)
        a3.setColor(c3, colorSpace='rgb')
        a3.setText(ans3)
        a4.setColor(c4, colorSpace='rgb')
        a4.setText(ans4)
        # setup some python lists for storing info about the resp
        resp.x = []
        resp.y = []
        resp.leftButton = []
        resp.midButton = []
        resp.rightButton = []
        resp.time = []
        resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trialComponents = [text, q, a1, a2, a3, a4, resp, polygon]
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
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
            
            # *q* updates
            if q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                q.frameNStart = frameN  # exact frame index
                q.tStart = t  # local t and not account for scr refresh
                q.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(q, 'tStartRefresh')  # time at next scr refresh
                q.setAutoDraw(True)
            
            # *a1* updates
            if a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a1.frameNStart = frameN  # exact frame index
                a1.tStart = t  # local t and not account for scr refresh
                a1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1, 'tStartRefresh')  # time at next scr refresh
                a1.setAutoDraw(True)
            
            # *a2* updates
            if a2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a2.frameNStart = frameN  # exact frame index
                a2.tStart = t  # local t and not account for scr refresh
                a2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2, 'tStartRefresh')  # time at next scr refresh
                a2.setAutoDraw(True)
            
            # *a3* updates
            if a3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a3.frameNStart = frameN  # exact frame index
                a3.tStart = t  # local t and not account for scr refresh
                a3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a3, 'tStartRefresh')  # time at next scr refresh
                a3.setAutoDraw(True)
            
            # *a4* updates
            if a4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a4.frameNStart = frameN  # exact frame index
                a4.tStart = t  # local t and not account for scr refresh
                a4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a4, 'tStartRefresh')  # time at next scr refresh
                a4.setAutoDraw(True)
            # *resp* updates
            if resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                resp.mouseClock.reset()
                prevButtonState = resp.getPressed()  # if button is down already this ISN'T a new click
            if resp.status == STARTED:  # only update if started and not finished!
                buttons = resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [a1,a2,a3,a4]:
                            if obj.contains(resp):
                                gotValidClick = True
                                resp.clicked_name.append(obj.name)
                        x, y = resp.getPos()
                        resp.x.append(x)
                        resp.y.append(y)
                        buttons = resp.getPressed()
                        resp.leftButton.append(buttons[0])
                        resp.midButton.append(buttons[1])
                        resp.rightButton.append(buttons[2])
                        resp.time.append(resp.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
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
        questionTrials.addData('text.started', text.tStartRefresh)
        questionTrials.addData('text.stopped', text.tStopRefresh)
        questionTrials.addData('q.started', q.tStartRefresh)
        questionTrials.addData('q.stopped', q.tStopRefresh)
        questionTrials.addData('a1.started', a1.tStartRefresh)
        questionTrials.addData('a1.stopped', a1.tStopRefresh)
        questionTrials.addData('a2.started', a2.tStartRefresh)
        questionTrials.addData('a2.stopped', a2.tStopRefresh)
        questionTrials.addData('a3.started', a3.tStartRefresh)
        questionTrials.addData('a3.stopped', a3.tStopRefresh)
        questionTrials.addData('a4.started', a4.tStartRefresh)
        questionTrials.addData('a4.stopped', a4.tStopRefresh)
        # store data for questionTrials (TrialHandler)
        if len(resp.x): questionTrials.addData('resp.x', resp.x[0])
        if len(resp.y): questionTrials.addData('resp.y', resp.y[0])
        if len(resp.leftButton): questionTrials.addData('resp.leftButton', resp.leftButton[0])
        if len(resp.midButton): questionTrials.addData('resp.midButton', resp.midButton[0])
        if len(resp.rightButton): questionTrials.addData('resp.rightButton', resp.rightButton[0])
        if len(resp.time): questionTrials.addData('resp.time', resp.time[0])
        if len(resp.clicked_name): questionTrials.addData('resp.clicked_name', resp.clicked_name[0])
        questionTrials.addData('resp.started', resp.tStart)
        questionTrials.addData('resp.stopped', resp.tStop)
        questionTrials.addData('polygon.started', polygon.tStartRefresh)
        questionTrials.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'questionTrials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'textTrials'


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
