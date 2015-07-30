import random, math

#Removes leading zeros after decimal and/or approximate to 4dp
def trimval(thelist):
	''' Takes in number list or float and removes leading zeros '''
	if type(thelist) == list:
		temp = []
		for i in thelist:
			if type(i) == int:
				temp.append(i)
			else:
				temp.append(float('%.4f' % i))
		thelist = temp
		return thelist

	elif type(thelist) == float:
		return float('%.4f' % thelist)

	return thelist


def trimlist(*args):
	''' Takes in number list or float and removes leading zeros '''
	store = []
	values =[]
	for mylist in args:
		each = []
		for x in mylist:
			if type(x) == float:
				each.append (float("%.4f" % x))

			elif type(x) == list:
				inner = []
				for y in x:
					if type(y) == float:
						inner.append(float("%.4f" % y))
					
					else: 
						inner.append(y)

				each.append(inner)

			else:
				each.append(x)

		values.append(each)

	store.append(values)
	return store[0]

class Calculate():
	def __init__(self, *args):
		''' Initialising the instances '''

		#Checking for valid arguments and value assignment
		if len(args) == 3:
			self._steps = args[2]

		elif len(args) == 2:
			self._steps = 1

		else:
			raise Exception("Invalid arguments: must be 2 or 3 -->  Outcome , Cummulative probability, optional: steps")

		self._outcome, self._cum_prob, self._probability = args[0], args[1], []

		# Checks in case user hasn't inputted the right information
		#Error checks for invalid inputs
		self.last_cum = (self._cum_prob[-1:])
		self.last_cum = (''.join(map(str, self.last_cum)))

		if len(self._outcome) != len(self._cum_prob):
			raise ValueError("'prob' arguments must be of same length")

		elif float(self.last_cum) != 1:
			raise ValueError("last value of 2nd argument must be 1")

		for i in args[1]:
			try:
				if 0 > i < 1:
					raise ValueError("cummulative probability must be between 0 and 1")
			except TypeError:
				raise Exception("All items in the second argument list must be an int")
		# Calculates the probability of an outcome given its cummulative probability
		def prob_(self):
			''' Returns a probability given its cummulative probability '''

			# Starting variables
			y = 1; self._probability.append(args[1][0])
			while y < len(self._cum_prob):
				self._probability.append(self._cum_prob[y] - self._cum_prob[y-1])
				y+=1
			
			return self._probability

		prob_(self)

		# Generaes a discreteEmp for the given outcome 
		def discreteemp_(self):
			'''returns a random number from the outcome list'''
			#--- generating a random number based on discreteemp
			
			emplist = []

			def twoargs():
				count = 0
				self._number = random.random()

				while count < len(self._cum_prob):
					#self._number = random.random()
					if self._cum_prob[count] < self._number <= self._cum_prob[count+1]:
						return self._outcome[count+1]
					
					elif 0 <= self._number <= self._cum_prob[0]:
					 	return self._outcome[0]

					count+=1

			if len(args) == 2:
				return twoargs()

			elif len(args) == 3:
				self.amount = args[2]
				increment = 0

				if self.amount == 1:
					return twoargs()

				else:
					try:
						while increment < self.amount:
							generated = twoargs()
							emplist.append(generated)
							increment +=1
					except TypeError:
						raise Exception("Third argument must be an int > 0")
					return emplist

		# Calculates the expectation value given its outcome and cummulative probability
		def expect_(self):
			''' returns the expectation value of the outcomes'''

			expectation, increment = 0,0
			
			while increment < len(self._cum_prob):
				expectation += self._probability[increment] * self._outcome[increment]
				increment += 1

			if len(args) == 2:
				return expectation

			elif len(args) == 3:
				expectation *= self._steps
				return expectation

			else:
				raise valueerror("arguments must be two or three")

		# Calculates the estimated variance of the given lists
		def eststddev_(self):
			'''returns estimated variance of the outcome'''
			#arguments are: [outcomes], [cummulative probabilities], optional: float(steps)]

			mean = expect_(self) / self._steps
		
			increment = 0
			occurtimes = 0
			while increment < len(self._cum_prob):
				occurtimes += self._probability[increment] * pow((self._outcome[increment] - mean), 2)
				increment +=1

			try:
				if len(args) == 2:
					return math.sqrt(occurtimes)

				elif len(args) == 3:
					return math.sqrt(occurtimes) * math.sqrt(self._steps)
			except ValueError:
				raise Exception("Second list argument must be cummulative i.e always increasing")
			# else: 
			# 	raise valueerror("arguments must be two or three")

		# Calculates the estimated standard deviation of the given lists
		def estvar_(self):
			''' Returns the estimated standard deviation of the outcome'''
			#arguments are: [outcomes], [cummulative probabilities], optional: float(steps)]
			variance = math.pow(eststddev_(self), 2)
			return variance

		# Calling all methods
		self._discreteemp = discreteemp_(self)
		self._expectval = expect_(self)
		self._estvar = estvar_(self); 
		self._eststddev = eststddev_(self); 

	def prob(self):
		return trimval(self._probability)

	def discreteemp(self):
		return trimval(self._discreteemp)

	def expectval(self):
		return trimval(self._expectval)

	def estmean(self):
		return trimval(self._expectval)

	def estvar(self):
		return trimval(self._estvar)

	def eststddev(self):
		return trimval(self._eststddev)
