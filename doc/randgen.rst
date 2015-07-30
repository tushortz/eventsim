.. eventsim documentation master file, created by
   sphinx-quickstart on Sun Jul  5 21:39:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. title:: Randgen Module

Randgen
=======
The Randgen module has a **Generate** class 

Generate
---------
**Generate** takes integer values as arguments (from `no arguments` up to and including `five arguments`) with optional `string` arguments being **"r"** or **"s"**. **r** for **reverse(descending order)** sorting and **s** for **ascending order** sorting. It has five methods which can be called on its instance namely:

Methods
^^^^^^^
* outcome() ----> generate outcomes based on the inputs supplied as arguments.
* unique() ----> generate unique outcomes based on the inputs supplied as arguments. You can think of it as a *set* of the outcome() method result.
* occur() ----> generate the number of times a unique item is found.
* getprob() ----> generate the probability of the outcome with respect to the unique outcome.
* getcum() ----> generate the cummulative probability of occurrence with respect to the unique outcome.


Importing the Generate class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can import the Generate class in three ways:

.. sidebar:: Note

   The highlighted code for importing should be used along with the highlighted code for creating an instance of the class (usage). Both way of creating an instance takes the same amount of arguments.

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 39-41
      :emphasize-lines: 2,3

and you can then respectively use it like this:

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 45, 44
      :emphasize-lines: 2

The following examples will cover how arguments are used in the Generate class. In the examples, we assume that the class has been imported first as

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 40

Example 1a
^^^^^^^^^^
**zero arguments**

What this does is populate the outcome list with random values (between 0 and 10) the default amount of times (i.e. a random number between 2 and 20).

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 44, 55-60
.. line 6 is space

Result 1a
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 33-37

Example 1b
^^^^^^^^^^
**Optional string argument**

Usage: Generate ('optional: **sort** ')

Adding an optional string argument *"r"* will *sort* the *outcome* in *descending* order whereas using the *"s"* string argument will *sort* the *outcome* in *ascending* order

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 46, 55-60 
.. line 6 is space

Result 1b
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 40-44


Example 2a
^^^^^^^^^^
**one argument**

Usage: Generate (**amount**)

What this does is populate the outcome list with random values (between 0 and 10) the amount of times specified in the argument. For example if 10 was specified in the argument, it will populate the outcome list with values ten times

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 47, 55-60 
.. line 6 is space

Result 2a
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 47-51

Example 2b
^^^^^^^^^^
**Optional string argument**

Usage: Generate (**amount**, 'optional: **sort**')

Adding an optional string argument *"r"* will *sort* the *outcome* in *descending* order whereas using the *"s"* string argument will *sort* the *outcome* in *ascending* order

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 48, 6, 56-60 
.. line 6 is space

Result 2b
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 54-58


Example 3a
^^^^^^^^^^
**two arguments**

Usage: Generate (**start**, **stop**)

What this does is populate the outcome list with values (between argument one and argument two) the default amount of times (i.e. a random number between 2 and 20).

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 49, 55-60
.. line 6 is space

Result 3a
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 61-65

Example 3b
^^^^^^^^^^
**Optional string argument**

Usage: Generate (**start**, **stop**, 'optional: **sort** ')

Adding an optional string argument *"r"* will *sort* the *outcome* in *descending* order whereas using the *"s"* string argument will *sort* the *outcome* in *ascending* order

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 50, 6, 56-60 
.. line 6 is space

Result 3b
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 68-72


Example 4a
^^^^^^^^^^
**three arguments**

Usage: Generate (**start**, **stop**, **amount**)

What this does is populate the outcome list with values (between argument one and argument two) the amount of times supplied in argument three. i.e. if 4 was supplied as the third argument, there will be four values in the outcome list.

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 51, 55-60
.. line 6 is space

Result 4a
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 75-79

Example 4b
^^^^^^^^^^
**Optional string argument**

Usage: Generate (**start**, **stop**, **amount**, 'optional: **sort** ')

Adding an optional string argument *"r"* will *sort* the *outcome* in *descending* order whereas using the *"s"* string argument will *sort* the *outcome* in *ascending* order

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 52, 6, 56-60 
.. line 6 is space

Result 4b
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 82-86


Example 5a
^^^^^^^^^^
**four arguments**

Usage: Generate (**start**, **stop**, **step**, **amount**)

What this does is populate the outcome list with values (between argument one and argument two) in steps of argument three value the amount of times in argument four's value. 

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 53, 55-60
.. line 6 is space

Result 5a
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 89-93

Example 5b
^^^^^^^^^^
**Optional string argument**

Usage: Generate (**start**, **stop**, **step**, **amount**, 'optional: **sort** ')

Adding an optional string argument *"r"* will *sort* the *outcome* in *descending* order whereas using the *"s"* string argument will *sort* the *outcome* in *ascending* order

.. literalinclude:: ./programs/example.py
  :language: python
  :lines: 54, 6, 56-60 
.. line 6 is space

Result 5b
^^^^^^^^^
.. literalinclude:: ./programs/results.txt
  :language: python
  :lines: 96-100