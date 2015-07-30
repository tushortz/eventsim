%define name eventsim
%define version 0.6
%define unmangled_version 0.6
%define release 1

Summary: Contains various useful tools in simulating discrete system events based on outcome and probabilities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Taiwo Kareem <taiwo.kareem36@gmail.com>
Url: http://bitbucket.org/tushortz/eventsim

%description
.. -*- restructuredtext -*-


What's new 
===========

**in Eventsim 0.6**

* Fixed tkinter issue between python 2 and 3 (importing tk not needed when using the import all syntax on eventsim.simevent)
* improvements and removed unnecessary codes.

**in Eventsim 0.5.9**

* Made improvements to trimlist to accept, display and trim more than one argument

**in Eventsim 0.5.8**

* Made improvements to trimlist

**in Eventsim 0.5.7**

* fixed double outcome list generation in the randgen module
* fixed errors shown when "r" or "s" is the only argument given
* Changed trimlist in the discrete module to approximate to 4 decimal places. (`Formerly 3 decimal places`)


**in Eventsim 0.5.6**

* Fixed some bugs, optimised program
* Renamed models to discrete
* Now all classes begin with an uppercase 
* discrete(formerly models) now has its own class for easy manipulation
* Two more methods added to discrete (trimval and trimlist) to display number output in a clean way and approximate to 4d.p)

.. note::
  please if you had a previous version of eventsim, it is advisable to uninstall it first in case of errors. Use:

	.. code::

	   pip uninstall eventsim

     
Description
------------

eventsim makes discrete event easy to simulate

Currently, it consists of three modules:
discrete, randgen and simevent

MODULES
=======

Discrete
--------

Contains a class **Calculate** that takes two lists as arguments and an optional integer value (steps) for simplifying and calculating:

* probability,
* estimated variance,
* estimated mean,
* estimated standard deviation,
* expectation value,
* discreteEmp


as well as two other methods **trimval** that takes in one argument, (numbers or lists and strips it of leading zeros and round up to 4 decimal places 

and **trimlist** that takes in as many arguments as possibe and does the same thing **trimval** does but very useful if there is a nested list in the list of arguments.

They both help to display lists and numbers in a better and easier way to read rather than have values with many leading decimal numbers in a list keeping it concise.


Randgen
------- 

contains  a class **Generate** that takes integer numbers as arguments (from no argument to 5 arguments) with optional arguments being "r" or "s". r for reverse sorted and s for ascending order sort. It is used to generate:

* random outcome,
* a unique outcome
* times of occurrence of outcome
* probability of occurrence
* cummulative probability of occurrence

Simevent
--------

contains classes for generating and estimating events that happens in a workplace scenario. Simulating events like:

* Interarrival time
* Service time
* Arrival time
* Time when service begins
* Time when service ends
* Wait time in queue
* Time customer spends in system
* Idle time of server
* table display format you you want a more structured approach


This module currently contains three classes, **Randomsim**, **Simulate**, **Simtable**

* Randomsim which generates random values to populate the inter-arrival and service time ad then calculates the rest of the values (accepts 0 - 3 arguments)

* Simulate, a more flexible class that allows you to input your own inter-arrival time and service time as a list (takes 1-2 arguments [inter-arrival, service] time)

* Simtable contains one method, drawtable() for generating a tabled format of all the data using tkinter frames.make life easier by importing all classes from simevent

.. code::

	e.g. from eventsim.simevent import * 

or risk having to import at least three different modules by youself.Using drawtable is really simple, you only need to pass in the instance of your simulation class as first argument and Tk() as second argument and your table will be generated for you

.. code::

	e.g. a = Randomsim(4,6,9)
	Simtable(a, Tk()).drawtable()

help on using this package is included in the examples.
If you have an old version of eventsim, you are adviced to delete/uninstall the old one if the update isn't working well 

For more help information please see examples in the package or checkout its `documentation <http://www.pythonhosted.org/eventsim>`_ at http://www.pythonhosted.org/eventsim/
	
Requirements
------------

* Any version of python
* One of tkinter ot Tkinter is needed to display generated simulation in a tabular format

Download
---------

Download and install using:

.. code::

   pip install eventsim

   

Acknowledgements
----------------

I was inspired to write this package after my university coursework demanded using python to simulate events. I hope Modelling and Simulation students find it useful

All glory belongs to God for helping me in completing my first module.


Contact
-------

If further information or help is needed, feel free to contact me on my email at taiwo.kareem36@gmail.com
This is still in a test mode please if any errror or bugs is found, feel free to contact the developer and give details

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
