#Quil Cummings

import viz
import vizshape
import vizcam
import math
import random

#an instance of this class creates a simple network of roads and loads a car into it
class Environment2(viz.EventClass):
	
	def __init__(self):
		
		# base class constructor 
		viz.EventClass.__init__(self)
		
		#self.addCoordinateAxes()
		
		# set up keyboard and timer callback methods
		self.callback(viz.TIMER_EVENT, self.onTimer)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		self.starttimer(1, (1/25.0), viz.FOREVER)
		#self.starttimer(2, (30), viz.FOREVER)
		#self.starttimer(1, (30), viz.FOREVER)
		
		self.timePassed = 0
		
		# car's x,z location in maze and its rotation angle
		self.theta = 0
		self.x = 0
		self.z = 0
		
		#cars velocity
		self.vx = 0
		self.vy = 0
		self.vz = 0
		
		self.v = 0
		
		#lighting codeeeee
		self.myLight = viz.addLight()
		self.myLight.enable()
		self.myLight.color(1, 1, 1)
		
		m = viz.Matrix()
		m.postAxisAngle(1, 0, 0, 90)
		self.myLight.setMatrix(m)
		
		self.mat = viz.Matrix()
		
		
		#load taxi
		c = viz.add('taxiNew.dae')
		m = viz.Matrix()
		m.postAxisAngle(0, 1, 0, 90)
		c.setMatrix(m)
		
		self.car = viz.addGroup()
		c.setParent( self.car )
		
		
		# create ball and link it to car so the user can see where they are on the minimap
		self.circ2 = vizshape.addSphere(radius = 15.0, slices = 20, stacks = 20, axis = vizshape.AXIS_Y)
		self.circ2.color(1, 1, 0)
		self.circ2.setParent(self.car)
		
		
		#create a rectangle over visible ground and add grass texture
		viz.startLayer(viz.QUADS)
		viz.texCoord(0, 16)
		viz.vertex(700, 0, -100)
		viz.texCoord(16, 16)
		viz.vertex(700, 0, 600)
		viz.texCoord(16, 0)
		viz.vertex(-100, 0, 600)
		viz.texCoord(0, 0)
		viz.vertex(-100, 0, -100)
		self.vertices = viz.endLayer()
		
		tex = viz.addTexture('grass.jpg')
		
		tex.wrap(viz.WRAP_S, viz.REPEAT)
		tex.wrap(viz.WRAP_T, viz.REPEAT)
		
		self.vertices.texture(tex)
		
		#load in models
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
		m.postTrans(375, 0, 180)
		self.house11.setMatrix(m)
		
		self.pizza = viz.add('pizza\model.dae')
		
		m = viz.Matrix()
		#m.postAxisAngle(0, 1, 0, 90)
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
	
		self.road.ambient(.5, .5, .5)
		self.myLight.ambient(.5, .5, .5)
		
		#add text telling player who needs a ride
		
		textScreen = viz.addText('Mike needs a ride to the diner!', viz.SCREEN, pos =[0, 0, 0])
		textScreen.color(viz.BLUE)
		textScreen.fontSize(60)
		
		self.circ = vizshape.addSphere(radius = 15.0, slices = 20, stacks = 20, axis = vizshape.AXIS_Y)
		self.circ.color(1, 0, 0)
		m = viz.Matrix()
		m.postTrans(350, 100, 345)
		self.circ.setMatrix(m)
		
		
		
		
		# Key pressed down event code.
	def onKeyDown(self,key):
		
		#if the d key is pressed turn right
		if (key == "d"):
			self.theta += 3
			
		#if the a key is pressed turn left
		if (key == "a"):  
			self.theta -=  3

		#if the s key is pressed go "forwards" which is backwards for this model
		if (key == "s"):
			self.v -= .5
			self.vx = math.sin(math.radians(self.theta))*self.v
			self.vz = math.cos(math.radians(self.theta))*self.v
			self.mat.postTrans(0, 0.1, 0)
			
		#if the w key is pressed go "backwards" which is really forwards for this model
		if (key == "w"):
			self.v += .1
			
		if (key == "b"):
			
			self.v = 0
			self.vx = 0
			self.vz = 0
			
			
	def onTimer(self, num):
		
		if (num == 1):
			carPos = self.car.getPosition()
			circPos = self.circ.getPosition()
	
			print("pos[0]: " + (str)(carPos[0]))
			print("pos[2]: " + (str)(carPos[2]))
			
			if (carPos[0] >= 375 and carPos[0] <= 395):
				if (carPos[2] >= 345 and carPos[2] <= 375):
					m = viz.Matrix()
					m.postTrans(350, 100, 345)
					m.postTrans(-75, 0, 140)
					self.circ.setMatrix(m)
					
			if (carPos[0] >= 265 and carPos[0] <= 300):
				if (carPos[2] >= 514 and carPos[2] <= 554):
					print("Good Job!")
					
					textScreen = viz.addText(' Mike: "Thank you!" ', viz.SCREEN, pos =[.2, .5, 0])
					textScreen.color(viz.BLUE)
					textScreen.fontSize(90)
					
					
		
			if(self.v > 1.5):
				self.v = 1.5
			
			if (self.v < -1.5):
				self.v = -1.5
				
			self.vx = math.sin(math.radians(self.theta))*self.v
			self.vz = math.cos(math.radians(self.theta))*self.v
			self.x = self.x + self.vx
			self.z = self.z + self.vz
			m = viz.Matrix()
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,.1,self.z)
			self.car.setMatrix(m)
			
			#set view to match that of car
			self.view = viz.MainView
			m = viz.Matrix()
			# first position view wrt car when it is at origin and looking down z axis
			m.postAxisAngle(1,0,0,20) # rotate the view down a bit
			m.postTrans(0,4,-3.4)   # then translate it up above car and back a bit
			# now align view with the current rotation/location of the car
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,0,self.z)
			self.view.setMatrix(m)
			
			
		
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
			
		
		