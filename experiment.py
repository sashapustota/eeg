"""
Wrapper to run psychopy experiment.
"""

from multiprocessing.connection import wait
from src.scripts import storytime
from psychopy import visual, core, event, gui, data
import glob
import pandas as pd
import random

# Run the experiment
storytime.run_experiment()

## Start EEG recording from the dongle, check that everything is working.

## Showcase instructions
    # In this experiment, you will have to kinesthetically imagine movements of either your left or right hand.
    # The specific movements you will have to imagine is a fist clench.

# Write a function that shows text on the screen in psychopy

def showtext(text, wait=True):
    # Display the text
    text = visual.TextStim(win, text=text)
    text.draw()
    win.flip()
    # Wait for a keypress
    if wait:
        event.waitKeys()


SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1100

# get date for unique file name
date = data.getDateStr()

#creating an empty pandas data frame with column names
columns = ['Timestamp','ID', 'Age', 'Gender', 'State', 'RT']
win = visual.Window((SCREEN_WIDTH, SCREEN_HEIGHT), fullscr = False, color = "grey", units = 'pix')

introtext = ''' 
In this experiment you will be asked to kinesthetically imagine a fist clench, of either right or left hand.  \n
Before every round a cross is presented on the screen, for 2 seconds. Please focus on the cross. \n
After the cross disappears, you will see a red circle, indicating that in 1 second, an arrow, pointing either left, right or forward will appear. \n
If the arrow is pointing right, you have to imagine clenching your right first. If left - left fist.  \n
The arrow will disappear after 4 seconds. During these 4 seconds, please imagine clenching your fist continously. \n
This means clenching your fist and continuing to clench for the whole time, not clenching it as many times as possible. \n
If the arrow points forward, simply look at the screen, don't deliberately think of anything.  \n
Please keep your eyes open while imagining movements and try to move as little as possible.  \n
Press any key to continue. \n
'''

endtext = ''' 
Thank you for your participation.  \n
You can press any key to yeet out from the experiment. \n
'''

stimuli = random.choice(glob.glob("stimuli/arrow*.jpg"))
# Name stimuli right, left and neutral.
whitecircle = glob.glob("cross.jpg")
redcircle = glob.glob("image.jpg")

# Write a function that picks a random object from stimuli and displays it on the screen, waits 4 seconds, over a loop of 50 times

def showstimuli(waittime, image):
    # Pick a random image
    image_path = image
    # Display the image
    image = visual.ImageStim(win, image=image_path)
    image.draw()
    win.flip()
    core.wait(waittime)

stopwatch = core.Clock()

def experiment_flow():

    # Show the intro text
    showtext(introtext, wait=True)

    # Start EEG recording

    for i in range(1:3):
        # Show the cross
        showstimuli(2, whitecircle)
        # Show the red circle
        showstimuli(1, redcircle)
        # Show the stimuli
        # Throw a tag to EEG
        showstimuli(4, stimuli)
        DATA = DATA.append({"State": str(stimuli[1])
            # Write to the dataframe that the image shown was right
        # Get the RT
    
    # Stop EEG recording

    # Show the end text

    showtext(endtext, wait=True)

    display.quit()
    win.close()










