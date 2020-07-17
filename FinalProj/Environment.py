#Quil Cummings

import viz
import vizshape
import vizcam
import math

#an instance of this class creates a simple network of roads and loads a car into it
class Environment(viz.EventClass):
	
	def __init__(self):
		
		# base class constructor 
		viz.EventClass.__init__(self)
		
		# set up keyboard and timer callback methods
		self.callback(viz.TIMER_EVENT, self.onTimer)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		self.starttimer(1, (1/25.0), viz.FOREVER)
		
		# car's x,z location in maze and its rotation angle
		self.theta = 0
		self.x = 0.5
		self.z = 0.5
		
		#cars velocity
		self.vx = 2
		self.vy = 0
		self.vz = 0
		
		viz.phys.enable()
		
		self.mat = viz.Matrix()
		
		self.forwards = 0
		
		
		self.car = viz.add('car2\model.dae')
		#self.car.setEuler([180, 0, 0], viz.ABS_GLOBAL)
		m = viz.Matrix()
		m.postTrans(self.x, 0.1, self.z)
		self.car.setMatrix(m)
		
		self.car.setVelocity([self.vx, self.vy, self.vz])
		
		
		
		self.house1 = viz.add('house1\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(115, 0, 230)
		self.house1.setMatrix(m)
		
		self.house2 = viz.add('house2\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(15, 0, 30)
		self.house2.setMatrix(m)
		
		self.house3 = viz.add('house3\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 180)
		m.postTrans(20, 0, 35)
		self.house3.setMatrix(m)
		
		self.house4 = viz.add('house4\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(220, 0, 235)
		self.house4.setMatrix(m)
		
		self.house5 = viz.add('house5\model.dae')
		
		m = viz.Matrix()
		#m.postAxisAngle(0, 1, 0, 180)
		m.postTrans(375, 0, 355)
		self.house5.setMatrix(m)
		
		self.house6 = viz.add('house6\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(107, 0, 450)
		self.house6.setMatrix(m)
		
		self.house7 = viz.add('house2\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(255, 0, 205)
		self.house7.setMatrix(m)
		
		self.house8 = viz.add('house5\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 180)
		m.postTrans(200, 0, 50)
		self.house8.setMatrix(m)
		
		self.house9 = viz.add('house7\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(217, 0, 365)
		self.house9.setMatrix(m)
		
		self.house10 = viz.add('house8\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(400, 0, 550)
		self.house10.setMatrix(m)
		
		self.house11 = viz.add('house9\model.dae')
		
		m = viz.Matrix()
		#m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(375, 0, 180)
		self.house11.setMatrix(m)
		
		self.pizza = viz.add('pizza\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(300, 0, 550)
		self.pizza.setMatrix(m)
		
		self.diner = viz.add('diner\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(260, 0, 570)
		self.diner.setMatrix(m)
		
		self.stop = viz.add('stop\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		m.postTrans(100, 1, 50)
		self.stop.setMatrix(m)
		
		self.stop2 = viz.add('stop\model.dae')
		
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, -90)
		m.postTrans(108, 1, 57)
		self.stop2.setMatrix(m)
		
		self.tree = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(50, 0, 40)
		m.postScale(3, 3, 3)
		self.tree.setMatrix(m)
		
		self.tree2 = viz.add('tree\model.dae')
		m = viz.Matrix()
		m.postTrans(190, 0, 190)
		m.postScale(2, 2, 2)
		self.tree2.setMatrix(m)
		
		self.tree3 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(120, 0, 90)
		m.postScale(2, 2, 2)
		self.tree3.setMatrix(m)
		
		self.tree4 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(70, 0, 40)
		m.postScale(3, 3, 3)
		self.tree4.setMatrix(m)
		
		self.tree5 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(65, 0, 50)
		m.postScale(2, 2, 2)
		self.tree5.setMatrix(m)
		
		self.tree6 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(30, 0, 60)
		m.postScale(3, 3, 3)
		self.tree6.setMatrix(m)
		
		self.tree7 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(25, 0, 40)
		m.postScale(4, 4, 4)
		self.tree7.setMatrix(m)
		
		self.tree8 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(10, 0, 15)
		m.postScale(4, 4, 4)
		self.tree8.setMatrix(m)
		
		self.tree9 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(65, 0, 200)
		m.postScale(2, 2, 2)
		self.tree9.setMatrix(m)
		
		self.tree10 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(40, 0, 140)
		m.postScale(4, 4, 4)
		self.tree10.setMatrix(m)
		
		self.tree11 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(35, 0, 150)
		m.postScale(3, 3, 3)
		self.tree11.setMatrix(m)
		
		self.tree13 = viz.add('tree\model.dae')
		m = viz.Matrix()
		m.postTrans(180, 0, 190)
		m.postScale(2, 2, 2)
		self.tree13.setMatrix(m)
		
		self.tree14 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(120, 0, 90)
		m.postScale(2, 2, 2)
		self.tree14.setMatrix(m)
		
		self.tree15 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(100, 0, 40)
		m.postScale(3, 3, 3)
		self.tree15.setMatrix(m)
		
		self.tree16 = viz.add('tree\model.dae')
		
		m = viz.Matrix()
		m.postTrans(165, 0, 50)
		m.postScale(2, 2, 2)
		self.tree16.setMatrix(m)
		
		self.tree17 = viz.add('tree2\model.dae')
		
		m = viz.Matrix()
		m.postTrans(100, 0, 50)
		m.postScale(2, 2, 2)
		self.tree17.setMatrix(m)
		
		self.tree18 = viz.add('tree3\model.dae')
		
		m = viz.Matrix()
		m.postTrans(90, 0, 70)
		m.postScale(2, 2, 2)
		self.tree18.setMatrix(m)
		
		self.road = viz.add('Roads.dae')
		
		
		#self.car.setCenter([5, 1.75, 0])
		view = viz.MainView
		carLink = viz.link(self.car, view)
		carLink.preEuler([180, 0, 0])
		carLink.postTrans([0, 1.75, 0])
		
		# Key pressed down event code.
	def onKeyDown(self,key):
		
		m = viz.Matrix()	
		
		#if the right key is pressed turn right
		if (key == viz.KEY_RIGHT):
			self.theta += 5
			m.postAxisAngle(0, 1, 0, self.theta)
			m.postTrans(self.x, 0.1, self.z)
			self.car.setMatrix(m)
			
		#if the left key if pressed turn left
		if (key == viz.KEY_LEFT):
			self.theta -=  5
			m.postAxisAngle(0, 1, 0, self.theta)
			m.postTrans(self.x, 0.1, self.z)
			self.car.setMatrix(m)
		
		#if the down key is pressed go "forwards" which is backwards for this model
		if (key == viz.KEY_DOWN):
			self.forwards = 1
#			x = math.sin(math.radians(self.theta))*.5
#			z = math.cos(math.radians(self.theta))*.5
#			self.x = self.x + x
#			self.z = self.z + z
#			m.postAxisAngle(0, 1, 0, self.theta)
#			m.postTrans(self.x, .1, self.z)
#			self.car.setMatrix(m)
			
			
		#if the up key if pressed go "backwards" which is really forwards for this model
		if (key == viz.KEY_UP):
			self.forwards = -1
#			x = math.sin(math.radians(self.theta))*.5
#			z = math.cos(math.radians(self.theta))*.5
#			self.x = self.x - x
#			self.z = self.z - z
#			m.postAxisAngle(0, 1, 0, self.theta)
#			m.postTrans(self.x, .1, self.z)
#			self.car.setMatrix(m)
			
		
	def onTimer(self, num):
			
		x = math.sin(math.radians(self.theta))*.5*self.forwards
		z = math.cos(math.radians(self.theta))*.5*self.forwards
		self.x = self.x - x
		self.z = self.z - z
		self.mat.postAxisAngle(0, 1, 0, self.theta)
		self.mat.postTrans(self.x, 0, self.z)
		self.car.setMatrix(self.mat)