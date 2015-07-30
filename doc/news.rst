.. eventsim documentation master file, created by
   sphinx-quickstart on Sun Jul  5 21:39:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. title:: What's new

What's new 
===========

in Eventsim 0.6
---------------
* Fixed tkinter issue between python 2 and 3 (importing tk not needed when using the import all syntax on eventsim.simevent)
* improvements and removed unnecessary codes.

in Eventsim 0.5.9
------------------
* Made improvements to trimlist to accept, display and trim more than one argument

in Eventsim 0.5.8
-----------------
* Made improvements to trimlist

in Eventsim 0.5.7
-----------------
* fixed double outcome list generation in the randgen module
* fixed errors shown when "r" or "s" is the only argument given
* Changed trimlist in the discrete module to approximate to 4 decimal places. (`Formerly 3 decimal places`)


in Eventsim 0.5.6
-----------------
* Fixed some bugs, optimised program
* Renamed models to discrete
* Now all classes begin with an uppercase 
* discrete(formerly models) now has its own class for easy manipulation
* Two more methods added to discrete (trimval and trimlist) to display number output in a clean way and approximate to 4d.p)

.. note::
  please if you had a previous version of eventsim, it is advisable to uninstall it first in case of errors. Use:

	.. code::

	   pip uninstall eventsim

     