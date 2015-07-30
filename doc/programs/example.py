import eventsim.discrete 
from eventsim.discrete import Calculate
from eventsim.discrete import trimval
from eventsim.discrete import trimlist
from eventsim.discrete import *


a = [-1,0,3,4]
b = [0.1, 0.4, 0.7, 1]

sample = eventsim.discrete.Calculate(a, b, 10)
sample = Calculate(a, b)

print("Probability:",sample.prob())
print("DiscreteEmp:",sample.discreteemp())
print("Expectation value:",sample.expectval())
print("Estimated Mean:",sample.estmean())
print("Estimated Variance:",sample.estvar())
print("Estimated Standard deviation:",sample.eststddev())


#only does one value and can only take float and int
sample = [12.00647886, 6543.23456, 9]
print(trimval(sample))
sample = [12.00647886, 6543.23456, 9], 12.87532
print(trimval(sample))
#doesnt do this. Use trimlist instead
sample = [53.00647886, 2], 4.9080000, "cat", [4, [5.98753]]
print(eventsim.discrete.trimval(sample))

sample = [1, 12.063506, ["cat", 56.000001, 2, [7, 9.046376] ] ]
print(trimlist(sample))

sample = [1, 12.063506, ["cat", 56.000001, 2, 9.03479] ]
print(eventsim.discrete.trimlist(sample))


#---------------------------------------------
import eventsim.randgen
from eventsim.randgen import Generate
from eventsim.randgen import *

#Takes 0-5 arguments
sample = Generate()
sample = eventsim.randgen.Generate()
sample = Generate("r")
sample = Generate(8)
sample = Generate(10,"s")
sample = Generate(3, 7)
sample = Generate(2, 6, "r")
sample = Generate(2, 5, 7)
sample = Generate(2, 5, 7, "s")
sample = Generate(2, 20, 3, 10)
sample = Generate(2, 20, 3, 10, "r")

print ("Outcome:",sample.outcome())
print ("Unique Outcome:",sample.unique())
print ("Occurrence:",sample.occur())
print ("Probability:",sample.getprob())
print ("Cummulative Probability:",sample.getcum())


#---------------------------------------------
import eventsim.simevent
from eventsim.simevent import Randomsim
from eventsim.simevent import Simulate
from eventsim.simevent import Simtable
from eventsim.simevent import *

sample = Randomsim()
sample = Randomsim(6)
sample = eventsim.simevent.Randomsim(6)
sample = Randomsim(4,6)
sample = Randomsim(4, 6, 8)

sample = eventsim.simevent.Simulate([5, 6, 3], [4,7,2])
 
print("Inter-arrival time:",sample.intarrival())
print("Arrival time:",sample.arrival())
print("Service time:",sample.service())
print("Time when Service begins:",sample.servbegin())
print("Time when Service ends:",sample.servend())
print("Time customer spends waiting in Queue:",sample.queuewait())
print("Time customer spends in system:",sample.custspend())
print("Idle time of server:",sample.idle())

sample = Simulate([7, 9, 6])
sample = Simulate([0, 5, 6, 3, 7, 9, 3], [4, 7, 2, 1, 3, 11, 7])

sampletable = eventsim.simevent.Simtable(sample, Tk())
sampletable = Simtable(sample, Tk())
sampletable.drawtable()



try:
    from tkinter import *			#for python 3
except ImportError:
    from Tkinter import *			#   for
    from ttk import * 				# python 2