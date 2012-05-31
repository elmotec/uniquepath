uniquepath
==========

Simple utility to manage PATH-like environment variables.

Usage
-----

::

  usage: uniquepath.py [-h] [-v] [-r PATH] [-a PATH] [-p PATH]
                       [--separator CHAR] [--debug]
                       variable

  positional arguments:
    variable              environment variable or variable value to process.
  
  optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -r PATH, --remove PATH
                          remove value(s) from the environment variable.
    -a PATH, --append PATH
                          append value(s) to the environment variable.
    -p PATH, --prepend PATH
                          prepend value(s) to the environment variable.
    --separator CHAR      changes the path separator (default is os specific).
    --debug               different output format more readable but invalid. DO
                          NOT ASSIGN to an environment variable.
  
  On Windows: use uniquepath.py.bat helper script.
  
There are also a few `.bat` example in the directory.  

Installation
------------

Download uniquepath.py from http://github.com/elmotec/uniquepath


Plans
-----

- Handle wildcards.


License
-------

Licensed under the term of `MIT License`_. See file LICENSE.



.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
