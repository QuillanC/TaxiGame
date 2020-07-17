#Quil Cummings

import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.clearcolor(viz.SKYBLUE)

MOVE_SPEED = 5
TURN_SPEED = 60

car = viz.addChild('mini.osg')
ground = viz.addChild('ground.osgb')

view = viz.MainView

def updatecar():
	if viz.key.isDown(viz.KEY_UP):
		view.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_DOWN):
		view.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_RIGHT):
		view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
	elif viz.key.isDown(viz.KEY_LEFT):
		view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
		
	car.setPosition(view.getPosition())
	car.setEuler(view.getEuler(viz.BODY_ORI))
	car.setPosition([0.35,-1.2,0.2],viz.REL_LOCAL)

vizact.ontimer(0,updatecar)

