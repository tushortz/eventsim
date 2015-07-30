import random

# Generating random outcomes and probabilities
class Generate():
	def __init__(self, *args):
		''' Initialisation of all values'''
	# Starting variables that change result depending on the if statements
		start, stop, step = 0, 10, 1
		_outcome, _occurrence, _uniqueoutcome, _problist, _cumprob = [], [], [], [], []
		amount = random.randrange(2, 20)
		[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]

	# If statements to run different functions
		if len(args) == 0:
			_outcome = _outcome

		elif len(args) == 1:
			if type(args[0]) == int: 
				amount = args[0]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				
			elif args[0] == "r":
				_outcome = sorted(_outcome)
				_outcome.reverse()

			elif args[0] == "s":
				_outcome = sorted(_outcome)

			else:
				raise ValueError("Enter the right arguments value")

		elif len(args) == 2:
			if (type(args[0]),type(args[1])) == (int,int): 
				start, stop = args[0], args[1]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				
			elif args[1] == "r":
				amount = args[0]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)
				_outcome.reverse()

			elif args[1] == "s":
				amount = args[0]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)

			else:
				raise ValueError("Enter the right arguments value")

		elif len(args) == 3:
			if (type(args[0]), type(args[1]), type(args[2])) == (int, int, int):
				start, stop, amount = args[0], args[1], args[2]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				
			elif args[2] == "r":
				start, stop = args[0], args[1]
				_outcome = []
				outcome = [_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)
				_outcome.reverse()

			elif args[2] == "s":
				start, stop = args[0], args[1]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)

			else:
				raise ValueError("Enter the right arguments value")

		elif len(args) == 4:
			if (type(args[0]), type(args[1]), type(args[2]), 
				type(args[3])) == (int, int, int, int):
				start, stop, step, amount = args[0], args[1], args[2], args[3]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				
			elif args[3] == "r":
				start, stop, amount = args[0], args[1],  args[2]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)
				_outcome.reverse()

			elif args[3] == "s":
				start, stop, amount = args[0], args[1],  args[2]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)

			else:
				raise ValueError("Enter the right arguments value")

		elif len(args) == 5:	
			if args[4] == "r":
				start, stop, step, amount = args[0], args[1], args[2], args[3]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)
				_outcome.reverse()

			elif args[4] == "s":
				start, stop, step, amount = args[0], args[1], args[2], args[3]
				_outcome = []
				[_outcome.append(random.randrange(start, stop + 1, step)) for i in range(amount)]
				_outcome = sorted(_outcome)

			else:
				raise ValueError("Enter the right arguments value")

		else:
			raise ValueError("Enter the right arguments value")
 
 	# Returns a set of the element and how many times it appears
		def eachcount(mylist):
			'''Returns a set of the element and how many times it appears'''
			unique = []
			result = []
			[unique.append(item) for item in mylist if item not in unique]
			
			for item in unique:
				increase, x = 0,0
				if (item in mylist):
					x = mylist.count(item)
				result.append(x)
			return (unique, result)

	# Returns only the set of the element as eachcount method above
		def makeunique(mylist):
			'''Returns the set of the element in the list argument'''
			unique,_ = eachcount(mylist)
			return unique 

	# Returns the number of times a item is found
		def timesfound(mylist):
			''' Returns the number of times a item is found'''
			_,result = eachcount(mylist)
			return result 

	# Returns a probability list of all items in its argument
		def problist_(probstorage, timesitemfound):
			'''Returns a probability list of all items in its argument'''
			return [probstorage.append(float("%.4f" % (i/amount)))  for i in timesitemfound]

	# Returns a cummulative probability list of all items in its argument
		def cumprob_(probstorage, cumlist):
			'''Returns a cummulative probability list of all items in its argument'''
			increase = 0
			try:
				for i in probstorage:
					increase +=i
					cumlist.append(float("%.4f" % increase))
				cumlist[-1] = 1.0      #makes sure the last value is 1.0
			except IndexError:
				raise ValueError("third argument must be > 0, 'r' or 's'")
				quit()
			return cumlist

	# Calls all the necessary methods to generate the required results
		_uniqueoutcome = makeunique(_outcome)
		_occurrence = timesfound(_outcome)
		problist_( _problist, _occurrence)
		cumprob_( _problist, _cumprob)

	# Assigning variables to be used by methods outside __init__ code
		self._outcome = _outcome      			# Generated result
		self._uniqueoutcome = _uniqueoutcome    # Uinque list of outcome
		self._occurrence = _occurrence      	# No of times each item is found
		self._problist = _problist    			# Liist of probabilities for each outcome
		self._cumprob = _cumprob      			# Cummulative probability list of each outcome


# Methods to return result
	# Returns the outcome
	def outcome(self):
		''' Returns a generated outcome '''
		return self._outcome

	# Returns the unique outcome
	def unique(self):
		'''Returns the unique outcome'''
		return self._uniqueoutcome

	# Returns the number of times the unique item is found
	def occur(self):
		'''Returns the number of times the unique item is found'''
		return self._occurrence

	# Returns the probability of each outcome in a list
	def getprob(self):
		'''Returns the probability of each unique outcome'''
		return self._problist

	# Returns the cummulative probability of each outcome in a list
	def getcum(self):
		'''Returns the cummulative probability of each unique outcome'''
		return self._cumprob