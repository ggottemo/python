#! python3
#createPr.py - GUI Automation to create a PR, accepts vendor as arg
#Usage - create <vendor> 
#        where  <vendor> is a string.
import sys, subprocess, cv2, time
import pyautogui as pag
import numpy as np

#CONSTANT file paths and threshold
PROCESS = 'astea browser.exe' 
FILEPATH = '#'
FORMFILEPATH ='#'
NEWFILEPATH ='#'
NEWKEYPATH ='#' 
THRESHOLD = .95
FLAG = False

if not len(sys.argv) == 2:
    print('USAGE: create <vendor>, where vendor is a string')
    print('vendor argument is required.')
    sys.exit()

vendor = str(sys.argv[1])
pag.PAUSE = 1 #Failsafe pause for testing
pag.FAILSAFE = True

#TODO If process is not running, open process.
#TODO Fill out vendor form, hit save and continue.  
pag.click(195,48) #Links
pag.click(131,121)#PR Link

#Wait for new button to load
while True:
    #Screenshot new button location 
    pag.screenshot(imageFilename= NEWFILEPATH)
    #Load screenshot and key image with cv2
    template = cv2.imread(NEWKEYPATH, 0)
    form = cv2.imread(NEWFILEPATH, 0)
    #Use match template to check for presence of key
    result = cv2.matchTemplate(form, template, cv2.TM_CCOEFF)
    for i in result:
        for j in i:
            if j > THRESHOLD:
                FLAG = True
    if FLAG:
        FLAG = False
        break
    else:
        continue

pag.click(18,232) #Click New Button
#Check that window has updated using cv2 / numpy
while True:
    #Screenshot target form
    pag.screenshot(imageFilename=FORMFILEPATH)
    

    #Use openCv to detect form is present
    template = cv2.imread(FILEPATH, 0)
    form = cv2.imread(FORMFILEPATH, 0)

    result = cv2.matchTemplate(form, template, cv2.TM_CCOEFF)
    for i in result:
        for j in i:
            if j > THRESHOLD:
                FLAG = True
    if FLAG:
        FLAG = False
        break
    else:
        continue

#Click through form
pag.click(561,342)#Vendor ID
pag.write(vendor)
pag.click(845,627)#Click off of text box
pag.click(304,448)#Select Vendor
#TODO Set date to two weeks out.

pag.doubleClick(864,341)
pag.click(916,348)