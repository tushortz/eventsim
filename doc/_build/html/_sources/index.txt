.. eventsim documentation master file, created by
   sphinx-quickstart on Sun Jul  5 21:39:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :hidden:
   :maxdepth: 2

   news
   discrete
   randgen
   simevent

 
.. title:: Eventsim

Getting started with Eventsim
=============================

:Author:   **Taiwo Kareem**
:Contact:  taiwo.kareem36@gmail.com

Eventsim is a python package that uses various useful tools in simulating discrete system events based on outcome and probabilities easily. It contains three main modules namely:


* **Discrete** 
	has a class **Calculate** which has six methods for simplifying and calculating:

	#. probability
	#. estimated variance
	#. estimated mean
	#. estimated standard deviation
	#. expectation value
	#. discreteEmp

  as well as two other methods **trimval** that
  takes in one argument, (numbers or lists and strips it of leading zeros and round up to 4 decimal places 

  and **trimlist** that takes in as many arguments as possible and does the same thing **trimval** does but very useful if there is a nested list in the list of arguments. It also round up numbers to 3 decimal places

  They both help to display lists and numbers in a better and easier way to read rather than have values with many leading decimal numbers in a list keeping it concise.
  
|

* **Randgen**
	contains a class **Generate** which has five methods for simplifying and generating:

    #. random outcome,
    #. a unique outcome
    #. times of occurrence of outcome
    #. probability of occurrence
    #. cummulative probability of occurrence

* **Simevent**
	contains three classes **Randomsim**, **Simulate** and **Simtable** for simplifying, generating and displaying:

    #. interarrival time
    #. service time
    #. arrival time
    #. time when service begins
    #. time when service ends
    #. wait time in queue
    #. time customer spends in system
    #. idle time of server
    #. table display data format

**Randomsim** is used to generate random values to populate the inter-arrival and service time which is then used to calculate the rest. It takes in two arguments as input. inter-arrival time list and service time list.

**Simulate** is more flexible in that it allows you to input your values. `first` argument being the `inter-arrival time` and the `second` argument being `service time`.

**Simtable** displays the given result as a table using the tkinter module. It takes two arguments, being an instance of any of the *Randomsim* or *Simulate* class and **Tk()**. 

.. note::
   **Tk()** must be the second argument of the **Simtable** `instance` or it would not work

Downloading Eventsim
--------------------

To use eventsim modules, you first need to ``download`` it from the `python packaging website <https://pypi.python.org/pypi/eventsim>`_ or if you have ``pip`` or ``easy_install`` installed, go to the ``command line (terminal)`` and type:

.. code::
  
  easy_install eventsim

or 

.. code::
  
  pip install eventsim



