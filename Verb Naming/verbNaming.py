#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Thu 06 May 2021 05:17:53 AM EEST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, microphone
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
expName = 'verbNaming'  # from the Builder filename that created this script
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
    originPath='/home/dude/Documents/psychological_tests/Verb Naming/verbNaming.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# Enable sound input/output:
microphone.switchOn()
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
    text='Σε αυτό το πείραμα θα εμφανίζονται εικόνες αντικειμένων στην οθόνη. Στόχος είναι να πεις τα ονόματα των αντικειμένων όσο πιο γρήγορα μπορείς. Θα κάνεις 3 διαλείμματα. Καλή επιτυχία!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
'''
from scipy.io import wavfile
from scipy.signal import hilbert, find_peaks, peak_widths, butter, lfilter
import numpy as np

def butter_lowpass(cutoff, fs, order=5):
  nyq = 0.5 * fs
  normal_cutoff = cutoff / nyq
  b, a = butter(order, normal_cutoff, btype='low', analog=False)
  return b, a
  
def butter_lowpass_filter(data, cutoff, fs, order=5):
  b, a = butter_lowpass(cutoff, fs, order=order) 
  y = lfilter(b,a,data)
  return y
  
  
  
def getSoundTimeStamps(filename, cutoff=200, order=1):
  samplerate, data = wavfile.read(filename)
  xn = np.int64(data)
  xn = xn - np.mean(xn) # Detrend
  
  fs = samplerate
  x_smoothed = butter_lowpass_filter(xn, cutoff, fs, order)
  hil_trans = hilbert(x_smoothed)
  
  y = np.sqrt(x_smoothed*x_smoothed + hil_trans.imag*hil_trans.imag)
  y /= np.max(y)
  
  peaks, properties = find_peaks(y, prominence=0.02,width=30)
  
  intervals = np.array(peaks[0],dtype=np.int64) # Start of first interval
  for i in range(len(peaks)-1):
    if peaks[i+1]-peaks[i] > samplerate/8:
      intervals = np.append(intervals, peaks[i])    # End of interval
      intervals = np.append(intervals, peaks[i+1])  # Start of next interval
  intervals = np.append(intervals, peaks[-1])   # End of last interval
  if intervals[0]==intervals[1]: # Single peak Na to dior8wsw na pianei k allou ektos ap'thn arxh
    intervals = np.delete(intervals,0)
    intervals = np.delete(intervals,0)
  widths = peak_widths(y, intervals, rel_height=0.95)[0]

  try:
    intervals.shape = (intervals.size//2, 2) # Make 2D array - 1st column start, 2nd end
  except ValueError as e: # Perittos ari8mos timestamps, leipei start h end
    print(e)
    thisExp.addData('Wrong_timestamps_check_wav', 1) # Na to grapsw sth routina, edw de douleuei
    # Na aporriptontai ta mikra intervals (Poso mikra?)
    # Na dw to sox an anagnwrizei foni kala
    # Na metatrepsw sth routina to samples se sec
  finally:
    print(filename.split('/')[-1],'\n', intervals)
    return intervals/samplerate
'''

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixCross = visual.TextStim(win=win, name='fixCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
polygon = visual.Rect(
    win=win, name='polygon',units='height', 
    width=(0.15,0.15)[0], height=(0.15,0.15)[1],
    ori=0.0, pos=(-1/2*win.size[0]/win.size[1]+.075, -0.425),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
empty = visual.TextStim(win=win, name='empty',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "pause"
pauseClock = core.Clock()
pauseText = visual.TextStim(win=win, name='pauseText',
    text='Διάλλειμα!\n\nΌταν είσαι έτοιμος/η κάνε κλικ για να συνεχίσεις!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pauseMouse = event.Mouse(win=win)
x, y = [None, None]
pauseMouse.mouseClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Το πείραμα τελείωσε. Ευχαριστούμε πολύ!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
mouse.setPos([0,0])
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
mouse.setVisible(0)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('imageList.csv'),
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    from random import random
    
    intertrial_interval = random()*2
    image.setImage(fname)
    resp = microphone.AdvAudioCapture(name='resp', saveDir=wavDirName, stereo=False, chnl=0)
    flag=False
    # keep track of which components have finished
    trialComponents = [fixCross, image, polygon, resp, empty, ISI]
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
        
        # *fixCross* updates
        if fixCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixCross.frameNStart = frameN  # exact frame index
            fixCross.tStart = t  # local t and not account for scr refresh
            fixCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixCross, 'tStartRefresh')  # time at next scr refresh
            fixCross.setAutoDraw(True)
        if fixCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixCross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixCross.tStop = t  # not accounting for scr refresh
                fixCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixCross, 'tStopRefresh')  # time at next scr refresh
                fixCross.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and asarray(fixCross.status==FINISHED):
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and asarray(image.status==STARTED):
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
        
        # *resp* updates
        if resp.status == NOT_STARTED and asarray(image.status==STARTED):
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            resp.record(sec=3.0, block=False)  # start the recording thread
        
        if resp.status == STARTED and not resp.recorder.running:
            resp.status = FINISHED
        
        # *empty* updates
        if empty.status == NOT_STARTED and asarray(resp.status==FINISHED):
            # keep track of start time/frame for later
            empty.frameNStart = frameN  # exact frame index
            empty.tStart = t  # local t and not account for scr refresh
            empty.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(empty, 'tStartRefresh')  # time at next scr refresh
            empty.setAutoDraw(True)
        if empty.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > empty.tStartRefresh + asarray(intertrial_interval)-frameTolerance:
                # keep track of stop time/frame for later
                empty.tStop = t  # not accounting for scr refresh
                empty.frameNStop = frameN  # exact frame index
                win.timeOnFlip(empty, 'tStopRefresh')  # time at next scr refresh
                empty.setAutoDraw(False)
        #resp.savedFile
        
        
        '''
        if resp.status==FINISHED and flag==False:
          intervals = getSoundTimeStamps(resp.savedFile)
          thisExp.addData('Time_Intervals', intervals)
          #thisExp.addData(f'start_time', intervals[0])
          #thisExp.addData(f'finish_time', intervals[1])
          #if len(intervals)>2: thisExp.addData(f'>1 Interval', True)
            #onset, offset = resp.getMarkerOnset(chunk=64, secs=3)
            #diarkeia = resp.getMarkerInfo()[1]
            #thisExp.addData('onset',diarkeia)
            #thisExp.addData('offset',offset)
          flag=True
        '''
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.5  # record stop time
        
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
    trials.addData('fixCross.started', fixCross.tStartRefresh)
    trials.addData('fixCross.stopped', fixCross.tStopRefresh)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    # resp stop & responses
    resp.stop()  # sometimes helpful
    if not resp.savedFile:
        resp.savedFile = None
    # store data for trials (TrialHandler)
    trials.addData('resp.filename', resp.savedFile)
    trials.addData('resp.started', resp.tStart)
    trials.addData('resp.stopped', resp.tStop)
    trials.addData('empty.started', empty.tStartRefresh)
    trials.addData('empty.stopped', empty.tStopRefresh)
    trials.addData('ISI.started', ISI.tStart)
    trials.addData('ISI.stopped', ISI.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    # update component parameters for each repeat
    pauseMouse.setVisible(1)
    pauseMouse.setPos([0,0])
    if trials.thisN == 0 or trials.thisN % 10 != 0:
        continueRoutine = False
    # setup some python lists for storing info about the pauseMouse
    pauseMouse.x = []
    pauseMouse.y = []
    pauseMouse.leftButton = []
    pauseMouse.midButton = []
    pauseMouse.rightButton = []
    pauseMouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pauseComponents = [pauseText, pauseMouse]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pauseText* updates
        if pauseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pauseText.frameNStart = frameN  # exact frame index
            pauseText.tStart = t  # local t and not account for scr refresh
            pauseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pauseText, 'tStartRefresh')  # time at next scr refresh
            pauseText.setAutoDraw(True)
        # *pauseMouse* updates
        if pauseMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pauseMouse.frameNStart = frameN  # exact frame index
            pauseMouse.tStart = t  # local t and not account for scr refresh
            pauseMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pauseMouse, 'tStartRefresh')  # time at next scr refresh
            pauseMouse.status = STARTED
            pauseMouse.mouseClock.reset()
            prevButtonState = pauseMouse.getPressed()  # if button is down already this ISN'T a new click
        if pauseMouse.status == STARTED:  # only update if started and not finished!
            buttons = pauseMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = pauseMouse.getPos()
                    pauseMouse.x.append(x)
                    pauseMouse.y.append(y)
                    buttons = pauseMouse.getPressed()
                    pauseMouse.leftButton.append(buttons[0])
                    pauseMouse.midButton.append(buttons[1])
                    pauseMouse.rightButton.append(buttons[2])
                    pauseMouse.time.append(pauseMouse.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pauseMouse.setVisible(0)
    trials.addData('pauseText.started', pauseText.tStartRefresh)
    trials.addData('pauseText.stopped', pauseText.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(pauseMouse.x): trials.addData('pauseMouse.x', pauseMouse.x[0])
    if len(pauseMouse.y): trials.addData('pauseMouse.y', pauseMouse.y[0])
    if len(pauseMouse.leftButton): trials.addData('pauseMouse.leftButton', pauseMouse.leftButton[0])
    if len(pauseMouse.midButton): trials.addData('pauseMouse.midButton', pauseMouse.midButton[0])
    if len(pauseMouse.rightButton): trials.addData('pauseMouse.rightButton', pauseMouse.rightButton[0])
    if len(pauseMouse.time): trials.addData('pauseMouse.time', pauseMouse.time[0])
    trials.addData('pauseMouse.started', pauseMouse.tStart)
    trials.addData('pauseMouse.stopped', pauseMouse.tStop)
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    if trials.thisN % 96 != 0 or trials.thisN == 0:
        continueRoutine = False
    # keep track of which components have finished
    feedbackComponents = [text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
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
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
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
