'''
Created by: Roman Beya
Created on: 28-sep-2017
Created for: ICS3U
This program displays local and global variables
'''

import ui

variableX = 25

def local_button_touch_up_inside(sender):
	# shows what happens to a local variable
	
	variableX = 10
	variableY = 30
	variableZ = variableX + variableY
	
	view['local_var_label'].text = str(variableZ)

def global_button_touch_up_inside(sender):
	# shows what happens to a global variable
	
	global variableX
	variableX = variableX + 1
	variableY = 30
	variableZ = variableX + variableY
	
	view['global_var_label'].text = str(variableZ)
	
view = ui.load_view()
view.present('sheet')
