#RoadsMain.py
#Driver code for Roads

import viz
import vizshape
import vizcam
import math
import vizact


from Environment2 import *

# set size (in pixels) and title of application window
viz.window.setSize( 640, 480 )
viz.window.setName( "Taxi Driver!" )

# get graphics window
window = viz.MainWindow

sound = viz.addAudio('MoonlightSonata.wav')
sound.volume(.5) 
#sound.setTime(1) 
#sound.setRate(0.7) 
sound.play()

# get mini map
miniMap = viz.addWindow()
miniMap.setSize([.3, .4])
miniMap.setPosition([0, 1])
miniMap.fov(70)
miniMapView = viz.addView()
miniMap.setView(miniMapView)

miniMapView.setPosition([250 , 450, 275])
miniMapView.setEuler([90, 90, 0])



# set background color of window to gray
viz.MainWindow.clearcolor( [150,150,150] ) 

# allows mouse to rotate, translate, and zoom in/out on object
#pivotNav = vizcam.PivotNavigate()  

e = Environment2()

vizact.onkeydown('q', viz.window.startRecording, 'test.avi') 
vizact.onkeydown('e', viz.window.stopRecording)

# render the scene in the window
viz.go()
