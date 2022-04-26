import usb_hid
import time
import random

import tools

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)



group1 = (40,0,0) #red
group2 = (35,29,0) # tools.colorShift(group1,40) #gold?
group3 = (35,20,0) # tools.colorShift(group2,40) #orange
group4 = (24,24,0) # tools.colorShift(group3,40) #yellow
group5 = (0,40,0) # tools.colorShift(group4,40) #green
group6 = (0,0,40) # tools.colorShift(group5,40) #blue
group7 = (25,0,25) # tools.colorShift(group6,40)  #purple
group8 = (0,30,30) #teal

group9 = tools.colorShift(group1,365/15)

consumer_control = ConsumerControl(usb_hid.devices)

# https://colorbrewer2.org/
# https://learn.adafruit.com/fancyled-library-for-circuitpython
# http://colorizer.org/
# https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html

####################################################
# Template classes

#class groupName(AbstractConfiguration):
#    def getName():
#        return 'clasName'
#    def getColor():
#        return # groupColor
#    def getMacros():
#        return [
#            # group_actions
#        ]
#
#class group_action(AbstractMacro):
#    def getMacroName():
#        return 'Action name'
#    def getMacro():
#        keyboard.send(Keycode.HOME)
#    def getMacroColor():
#        return groupName.getColor() OR
#        return tools.colorShift(groupName.getColor(), hsv_colorshift) 
####################################################

#==================================================#
# Blank class to use as a placeholder for short rows
class blank(AbstractMacro):
    def getMacroName():
        return 'Blank'
    def getMacro():
        pass
    def getMacroColor():
        return (0, 0, 0)
#==================================================#

####################################################

class Navigation(AbstractConfiguration):
    def getName():
        return 'Navigation'
    def getColor():
        return group1
    def getMacros():
        return [
            nav_home,
            nav_up,            
            nav_end,
            nav_pageUp,
            nav_left,
            nav_down,
            nav_right,
            nav_pageDn,
            nav_cut_line,
            nav_copy_line,
            nav_paste_line,
            blank,
            nav_cut,
            nav_copy,
            nav_paste
        ]

class nav_home(AbstractMacro):
    def getMacroName():
        return 'Home'
    def getMacro():
        keyboard.send(Keycode.HOME)
    def getMacroColor():
        return Navigation.getColor()
        
class nav_up(AbstractMacro):
    def getMacroName():
        return 'Up'
    def getMacro():
        keyboard.send(Keycode.UP_ARROW)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), 15)

class nav_end(AbstractMacro):
    def getMacroName():
        return 'End'
    def getMacro():
        keyboard.send(Keycode.END)
    def getMacroColor():
        return Navigation.getColor()

class nav_pageUp(AbstractMacro):
    def getMacroName():
        return 'Page Up'
    def getMacro():
        keyboard.send(Keycode.PAGE_UP)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), -15)

class nav_left(AbstractMacro):
    def getMacroName():
        return 'Left'
    def getMacro():
        keyboard.send(Keycode.LEFT_ARROW)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), 15)

class nav_down(AbstractMacro):
    def getMacroName():
        return 'Down'
    def getMacro():
        keyboard.send(Keycode.DOWN_ARROW)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), 15)

class nav_right(AbstractMacro):
    def getMacroName():
        return 'Right'
    def getMacro():
        keyboard.send(Keycode.RIGHT_ARROW)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), 15)

class nav_pageDn(AbstractMacro):
    def getMacroName():
        return 'Page Down'
    def getMacro():
        keyboard.send(Keycode.PAGE_DOWN)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(), -15)

class nav_cut_line(AbstractMacro):
    def getMacroName():
        return 'Cut Line'
    def getMacro():
        keyboard.send(Keycode.HOME)
        keyboard.send(Keycode.LEFT_SHIFT,Keycode.END)
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.X)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-135)

class nav_copy_line(AbstractMacro):
    def getMacroName():
        return 'Copy Line'
    def getMacro():
        keyboard.send(Keycode.HOME)
        keyboard.send(Keycode.LEFT_SHIFT,Keycode.END)
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.C)
        time.sleep(0.5)
        keyboard.send(Keycode.LEFT_SHIFT,Keycode.END)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-195)

class nav_paste_line(AbstractMacro):
    def getMacroName():
        return 'Paste Line'
    def getMacro():
        keyboard.send(Keycode.HOME)
        keyboard.send(Keycode.LEFT_SHIFT,Keycode.END)
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.V)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-225)     

class nav_cut(AbstractMacro):
    def getMacroName():
        return 'Cut'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.X)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-150)

class nav_copy(AbstractMacro):
    def getMacroName():
        return 'Copy'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.C)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-180)

class nav_paste(AbstractMacro):
    def getMacroName():
        return 'Paste'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.V)
    def getMacroColor():
        return tools.colorShift(Navigation.getColor(),-210)

#===========================================#

class Media(AbstractConfiguration):
    def getName():
        return 'Media Controls'
    def getColor():
        return group2
    def getMacros():
        return [
            med_prev,
            med_play,
            med_next,
            med_volUp,
            teams_cam,
            teams_mute,
            blank,
            med_volDown
        ]

class med_prev(AbstractMacro):
    def getMacroName():
        return 'Previous'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
    def getMacroColor():
        return tools.colorShift(Media.getColor(),-10)

class med_play(AbstractMacro):
    def getMacroName():
        return 'Play/Pause'
    def getMacro():
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
    def getMacroColor():
        return Media.getColor()

class med_next(AbstractMacro):
    def getMacroName():
        return 'Next'
    def getMacro():
        consumer_control.send(ConsumerControlCode.SCAN_NEXT_TRACK)
    def getMacroColor():
        return tools.colorShift(Media.getColor(),10)

class med_volUp(AbstractMacro):
    def getMacroName():
        return 'Volume Up'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return tools.colorShift(Media.getColor(),30)

class med_volDown(AbstractMacro):
    def getMacroName():
        return 'Volume Down'
    def getMacro():
        consumer_control.press(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.5)
        consumer_control.release()
    def getMacroColor():
        return tools.colorShift(Media.getColor(), 20) 

class teams_cam(AbstractMacro):
    def getMacroName():
        return 'Teams webcam'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.O)
    def getMacroColor():
        return tools.colorShift(Media.getColor(), 35) 

class teams_mute(AbstractMacro):
    def getMacroName():
        return 'Teams Mute'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.M)
    def getMacroColor():
        return tools.colorShift(Media.getColor(), 50) 

#===========================================#
#Visual Studio commands

class vsControls(AbstractConfiguration):
    def getName():
        return 'Visual Studio Controls'
    def getColor():
        return group7
    def getMacros():
        return [
            vs_start,            
            vs_restart,
            vs_stop,
            vs_breakpoint,
            vs_prev,
            vs_next,
            blank,
            blank,
            vs_comment,
            vs_uncomment,
            blank,
            blank,
            blank
        ]

class vs_start(AbstractMacro):
    def getMacroName():
        return 'Start/Continue Debugging'
    def getMacro():
        keyboard.send(Keycode.F5)
    def getMacroColor():
        return tools.colorShift(Media.getColor(), 50)

class vs_stop(AbstractMacro):
    def getMacroName():
        return 'Stop Debugging'
    def getMacro():
        keyboard.send(Keycode.LEFT_SHIFT,Keycode.F5)
    def getMacroColor():
        return Navigation.getColor()

class vs_restart(AbstractMacro):
    def getMacroName():
        return 'Restart Debugging'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.F5)
    def getMacroColor():
        return tools.colorShift(Media.getColor(), 65)

class vs_breakpoint(AbstractMacro):
    def getMacroName():
        return 'Toggle Breakpoint'
    def getMacro():
        keyboard.send(Keycode.F9)
    def getMacroColor():
        return tools.colorShift(vsControls.getColor(), 0)

class vs_prev(AbstractMacro):
    def getMacroName():
        return 'Previous Location'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.MINUS)
    def getMacroColor():
        return tools.colorShift(vsControls.getColor(), 46)

class vs_next(AbstractMacro):
    def getMacroName():
        return 'Next Location'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL,Keycode.LEFT_SHIFT,Keycode.MINUS)
    def getMacroColor():
        return tools.colorShift(vsControls.getColor(), 53)

class vs_comment(AbstractMacro):
    def getMacroName():
        return 'Comment Selection'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.K, Keycode.C)
    def getMacroColor():
        return tools.colorShift(vsControls.getColor(), 180) 

class vs_uncomment(AbstractMacro):
    def getMacroName():
        return 'Uncomment Selection'
    def getMacro():
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.K, Keycode.U)
    def getMacroColor():        
        return tools.colorShift(vsControls.getColor(), 200) 

#class group_action(AbstractMacro):
#    def getMacroName():
#        return 'Action name'
#    def getMacro():
#        keyboard.send(Keycode.HOME)
#    def getMacroColor():
#        return groupName.getColor() OR
#        return tools.colorShift(groupName.getColor(), hsv colorshift) 


#consumer_control.press(ConsumerControlCode.VOLUME_INCREMENT)
#        time.sleep(0.5)
#        consumer_control.release()

## COMMANDS ##

# Map your configurations inside this array
configurations_map = [Navigation, Media, vsControls] #[Git, Navigation, Terminal] #, GoogleMeet, Obsidian, RandomEstimation, PhpStorm ]	

