.. eventsim documentation master file, created by
   sphinx-quickstart on Sun Jul  5 21:39:27 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. title:: Discrete Module


Discrete
========
The Discrete module has a **Calculate** class, **trimval** and **trimlist** method

Calculate
---------
**Calculate** has six methods for calculating/generating ``probability``, ``estimated variance``, ``estimated mean``, ``estimated standard deviation``, ``expectation value`` and ``discreteEmp``.

Discrete's "`Calculate` class" takes `two arguments`: ``outcome`` and ``cummulative probability`` or a third optional argument which is `amount of times to be generated` (``steps``). 

Methods
^^^^^^^
Calculate methods are:

* prob() ----> To calculate the probability based on the given outcome list(second argument of the **Calculate** instance).
* discreteemp() ----> To generate a random outcome depending on its probability of occurrence.
* expectval() ----> To generate an expectation value i.e. the mean of the outcome depending on its probability
* estmean() ----> Same as expectval() because they always give the same output.
* estvar() ----> To calculate the estimated variance of the list data
* eststddev ----> To calculate the estimated standard deviation of the list data


Importing the Calculate class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can import the Calculate class in three ways:

.. sidebar:: Note

   The highlighted code for importing should be used along with the highlighted code for creating an instance of the class (usage). Both way of creating an instance can take two or three arguments.

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 1-2,5
      :emphasize-lines: 2,3

and you can then respectively use it like this:

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 11-12
      :emphasize-lines: 2


Example 1
^^^^^^^^^
**Two arguments**
Usage: Calculate(**outcome list**, **cummulative probability list**)

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 2, 6, 8-10, 12-19  
.. line 6 is space

Result
^^^^^^
.. literalinclude:: ./programs/results.txt
      :language: python
      :lines: 5-10


Example 2
^^^^^^^^^
**three arguments**

Usage: Calculate(**outcome list**, **cummulative probability list**, "`Optional: amount/steps`")

.. literalinclude:: ./programs/example.py
      :language: python
      :lines: 1, 6, 8-9, 6, 11, 6, 14-19  
.. line 6 is space

Result
^^^^^^
.. literalinclude:: ./programs/results.txt
      :language: python
      :lines: 13-18


.. note::
   **argument one** of the Calculate class should be the **outcome** list while **argument two** should be the **cummulative probability** list. **Argument three (steps)** is optional and only needed if any of the data is to be calculated after a certain number of times or to generate a list of discreteEmp values. 

   If no optional argument is given (same as if an optional argument is set to 1), discreteemp will generate only one outcome but if more the optional argument is more than one e.g. 5, then *discreteemp* will generate a list containing several generated outcomes (5 items in a list in this case).


trimval and trimlist
--------------------
**trimval** is a `discrete` module method that takes in one argument, (numbers or lists and strips it of leading zeros and round up to 4 decimal places. If more than one argument is given, none of the other arguments after the first would remain unchanged but no error would be raised.

**trimlist** on the other takes as many arguments as possibe and does the same thing **trimval** does but it's very useful if there is a nested list in the list of arguments. It is also very useful than trimval because it alter's all the arguments even to the first nested list of any of the arguments.

.. note::
  `It originally wasn't meant to be included in the module but because I used it a lot, I decided to include it in case.`

They both help to display lists and numbers in a better and easier way to read rather than have values with many leading decimal numbers in a list keeping it concise.


Importing the methods
^^^^^^^^^^^^^^^^^^^^^
They can be imported similar to the Calculate class. in any of the three ways.

.. literalinclude:: ./programs/example.py
    :language: python
    :lines: 1, 3-6
    :emphasize-lines: 1

and you can then respectively use it like this:

.. literalinclude:: ./programs/example.py
    :language: python
    :lines: 23, 6, 29,32
    :emphasize-lines: 3

Example 1 (Using trimval)
^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ./programs/example.py
    :language: python
    :lines: 5-6, 23-24, 6, 25-26, 6, 28-26
    :emphasize-lines: 6-7, 9-10
.. line 6 is space


Result
^^^^^^
.. literalinclude:: ./programs/results.txt
    :language: python
    :lines: 22-23
    :emphasize-lines: 2

.. note::
   The last highlighted result was not completely changed because **trimval** only works on the first argument. Use **trimlist** if this is the case.


Example 2 (Using trimlist)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ./programs/example.py
    :language: python
    :lines: 5-6, 31-34, 32
    :emphasize-lines: 3-4
.. line 6 is space


Result
^^^^^^
.. literalinclude:: ./programs/results.txt
    :language: python
    :lines: 28-29
    :emphasize-lines: 1

.. note::
   **trimlist** can only trim values up to and including one nested list and does not affect lists nested two levels within each other