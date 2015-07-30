import random

try:
    from tkinter import Tk, N, S, W, E
    from tkinter.ttk import Frame, Treeview
except ImportError:
    from Tkinter import Tk, N, S, W, E
    from ttk import Frame, Treeview 

class Randomsim():
	def __init__(self, *args):
		''' Initialisation '''
	
		self.stop, self.amount = 10, random.randint(2,20)
		self._intarrival,  self._service = [], []

		if len(args) == 0:
			[self._intarrival.append(random.randint(1, self.stop)) for i in range(self.amount)]	
			[self._service.append(random.randint(1, self.stop)) for i in range(self.amount)]

		elif len(args) == 1:
			[self._intarrival.append(random.randint(1, self.stop)) for i in range(args[0])]	
			[self._service.append(random.randint(1, self.stop)) for i in range(args[0])]

		elif len(args) == 2:
			[self._intarrival.append(random.randint(1, args[0])) for i in range(args[1])]	
			[self._service.append(random.randint(1, args[0])) for i in range(args[1])]

		elif len(args) == 3:
			[self._intarrival.append(random.randint(1, args[0])) for i in range(args[2])]	
			[self._service.append(random.randint(1, args[1])) for i in range(args[2])]

		else:
			raise ValueError("Arguments must be between 0 to 3")

		self._intarrival[0] = 0

		# Required variables
		self._arrival, self._preservstart, self._servstart = [], [0], []
		self._queue, self._servend, self._custspend, self._idle = [], [], [], [0]

		def getarrive_(self):
			'''Returns arrival time'''
			increase = 0
			for i in self._intarrival:
				increase +=i
				self._arrival.append(increase)
			return self._arrival

		def servbegins_(self):
			'''Returns time when service begin'''
			increase = 0
			for i in range(len(self._service)):
				increase += self._service[i]
				self._preservstart.append(increase)
			self._preservstart.pop()

			return self._preservstart

		for i in self._intarrival: self._servend.append(i) 
		#Please maintain order if you are editing the code!
		# Calling functions
		getarrive_(self)	#Returns arrival time
		servbegins_(self)	#Returns time when servce begin

		def get_servend_(self):
			'''Retuns time when service ends'''
			for x in range(len(self._preservstart)):
				self._servend[x] = self._preservstart[x] + self._service[x]
				s = 1
				while s < len(self._preservstart):
					if self._preservstart[s] < max(self._arrival[s], self._servend[x]):
						self._preservstart[s] = max(self._arrival[s], self._servend[x])
					s+=1 

			return self._servend

		# Method used to calculate the rest of the data like
		#time when service begins
		#wait time in queue, (_queue)
		#time customer spent in the system (_custspend)
		def otherresults(self, list1, list2, list3):
			''' Stores and return the value of (list2 - list3) in list1 '''
			for x in range(len(list2)):
				list1.append(list2[x] - list3[x]) 
			if list1[0] < 0:
				list1[0] = 0

		def idletime_(self):
			'''Returns the idle time of server'''
			x,y = 0,1
			while y < len(self._servend):
				(self._idle).append(self._servstart[y] - self._servend[x])
				x+=1
				y+=1
			return self._idle

		# Calling other methods
		get_servend_(self)
		otherresults(self, self._servstart, self._servend, self._service) 
		otherresults(self, self._queue, self._servstart, self._arrival) 
		otherresults(self, self._custspend, self._servend, self._arrival)
		idletime_(self)

	#Methods to be used outside of __init__ returning necessary values
	#Main methods

	def intarrival(self):
		'''Returns the interarrival time'''
		return self._intarrival

	def arrival(self):
		'''Returns the arrival time'''
		return self._arrival

	def service(self):
		'''Returns the service time'''
		return self._service

	def servbegin(self):
		'''Returns the time when service began'''
		return self._servstart

	def queuewait(self):
		'''Returns the customer's waiting time in the queue'''
		return self._queue

	def servend(self):
		'''Returns the time service ended'''
		return self._servend
 
	def custspend(self):
		'''Returns the time customer spends in system'''
		return self._custspend

	def idle(self):
		'''Returns the idle time of server'''
		return self._idle


class Simulate(Randomsim):
	def __init__(self, *args):
		''' Initialisation '''

		self.stop, self.amount = 10, random.randint(2,20)
		self._intarrival, self._service = [], []

		if len(args) == 1:
			self._intarrival = args[0]
			if type(args[0]) != list:
				raise ValueError("Argument must be a list")
			[self._service.append(random.randint(1, self.stop)) for i in range(len(args[0]))]
			
		elif len(args) == 2:
			if type(args[0]) != list and type(args[1]) != list:
				raise ValueError("Argument one and two must be lists")

			self._intarrival = args[0]
			self._service = args[1]

			#Check length of both lists and throw error if not equal
			if len(args[0]) != len(args[1]):
				raise ValueError("List arguments must be of equal length")


		else:
			raise ValueError("You must supply between one and two list arguments")

		if self._intarrival[0] < 0:
			self._intarrival[0] = 0
		
		# Required variables and input error handling
		self._preservstart = []; self._preservstart.append(args[0][0])
		if self._preservstart[0] < 0:
			self._preservstart[0] = 0

		self._arrival, self._servstart = [], []
		self._queue, self._servend, self._custspend, self._idle = [], [], [], [0]

		#Makes display less annoying
		def makenice(thelist):
			temp = []
			for i in thelist:
				if type(i) == int:
					temp.append(i)
				else:
					temp.append(float('%.4f' % i))
			thelist = temp
			return thelist


		def getarrive_(self):
			'''Returns arrival time'''
			increase = 0
			for i in self._intarrival:
				increase +=i
				self._arrival.append(increase)

			return self._arrival

		def servbegins_(self):
			'''Returns time when service begin'''
			increase = 0
			for i in range(len(self._service)):
				increase += self._service[i]
				self._preservstart.append(increase)
			self._preservstart.pop()

			return self._preservstart

		for i in self._intarrival: self._servend.append(i) 
		#Please maintain order if you are editing the code!
		# Calling functions
		getarrive_(self)	#Returns arrival time
		servbegins_(self)	#Returns time when servce begin

		def get_servend_(self):
			'''Retuns time when service ends'''
			for x in range(len(self._preservstart)):
				self._servend[x] = self._preservstart[x] + self._service[x]
				s = 1
				while s < len(self._preservstart):
					if self._preservstart[s] < max(self._arrival[s], self._servend[x]):
						self._preservstart[s] = max(self._arrival[s], self._servend[x])
					s+=1 

			return self._servend

		# Method used to calculate the rest of the data like
		#time when service begins
		#wait time in queue, (_queue)
		#time customer spent in the system (_custspend)
		def otherresults(self, list1, list2, list3):
			''' Stores and return the value of (list2 - list3) in list1 '''
			for x in range(len(list2)):
				list1.append(abs(list2[x] - list3[x]))

			if list1[0] < 0:
				list1[0] = 0

			return list1

		def idletime_(self):
			'''Returns the idle time of server'''
			x,y = 0,1
			while y < len(self._servend):
				(self._idle).append(abs(self._servstart[y] - self._servend[x]))
				x+=1; y+=1
			
			return self._idle


		# Calling other methods
		get_servend_(self)
		otherresults(self, self._servstart, self._servend, self._service) 
		otherresults(self, self._queue, self._servstart, self._arrival) 
		otherresults(self, self._custspend, self._servend, self._arrival)
		idletime_(self)

		#Rounding up to prevent annoying display of lots of decimals
		self._arrival = makenice(self._arrival)
		self._servend = makenice(self._servend)
		self._servstart = makenice(self._servstart)
		self._queue = makenice(self._queue)
		self._custspend = makenice(self._custspend)
		self._idle = makenice(self._idle)

	#Simulation class will inherit methods from the Randomsim class

class Simtable(Frame):
	def __init__(self, classInstance, parent):
		''' Initialisation '''
		
		#Inheriting from parent class
		Frame.__init__(self)

		self.parent = parent
		self.classInstance = classInstance
		self.CreateUI(classInstance)
		self.LoadTable()
		self.grid(sticky = (N,S,W,E))
		self.parent.grid_rowconfigure(0, weight = 1,)
		self.parent.grid_columnconfigure(0, weight = 1)
		self.parent.title("Simulation Table")

	def CreateUI(self, classInstance):

		self.headers = [ 
			"Customers", 
			"Inter-arrival time", 
			"Arrival time", 
			"Service time",
			"Waiting time in queue", 
			"Time when service begins", 
			"Time when service ends", 
			"Time customer spends in system",
			"Idle time of server"
		]

		self.contents =[]

		# populates the table from other class to generate the tkinter table
		def compilelist(classInstance):
			self.contents.append(classInstance.intarrival())
			self.contents.append(classInstance.arrival())
			self.contents.append(classInstance.service())
			self.contents.append(classInstance.queuewait())
			self.contents.append(classInstance.servbegin())
			self.contents.append(classInstance.servend())
			self.contents.append(classInstance.custspend())
			self.contents.append(classInstance.idle())

			return self.contents

		# Calling the function
		compilelist(classInstance)

		self.rearrange = []
		for row in zip(*self.contents):
			self.rearrange.append(row)

		self.headdata = []
		for x in range(len(self.contents[0])):
			self.headdata.append(x+1)

		header_lists = []
		tv = Treeview(self)
		tv['columns'] = (self.headers)

		for x in range(len(self.headers)):
			tv.heading("#%s"%x, text=self.headers[x], anchor='center')
			tv.column ("#%s"%x, anchor='center', width="150")

		tv.grid(sticky = (N,S,W,E))
		self.treeview = tv
		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)

	def LoadTable(self):
		x,y = 0,0
		while x < len(self.rearrange):
			self.treeview.insert("", "end", text= self.headdata[x], values=( self.rearrange[x]))
			x +=1

	def drawtable(self):
		self.parent.mainloop()

