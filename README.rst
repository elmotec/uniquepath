uniquepath
==========

Simple utility to remove duplicate in PATH-like environment variables. 

On Unix, it outputs the transformed variable so it can be used like this :

::

  $ PATH=`uniquepath.py PATH`

On Windows, there is a helper ``.bat`` script that achieve the same effect (even if it is not as explicit):

::

  C:\uniquepath.bat PATH

The command line also offers ways to append, prepend, and remove path to the variable and it supports wildcard (usefull for remove).

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
  
  On Windows: use uniquepath.bat helper script.
  
There are also 2 usage examples in the directory ``pyenv.bat`` (to switch python version) and the helper script ``uniquepath.bat`` for windows.

Installation
------------

Download uniquepath.py from http://github.com/elmotec/uniquepath


License
-------

Licensed under the term of `MIT License`_. See file LICENSE.



.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
