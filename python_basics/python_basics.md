---
title:
- Python Basics

author:
- Jie Niu

date:
- 2020-1-7

theme:
- CambridgeUS

---
# Hello Python
## Install Python
[https://www.python.org](https://www.python.org)

Anaconda (includes everything you need for scientific computing) [https://www.anaconda.com](https://www.anaconda.com)

## Start using Python interpreter
Open **terminal** (Mac OS or Linux)
``` bash
$ python
```
or **cmd** (Windows)
``` bash
C:\> python
```
``` bash
$ python

Python 2.x.xx ...
...

>>>
```
## Start using Python interpreter
``` bash
$ python3

Python 3.x.xx ...
...

>>>
```
``` python
>>> print('Hello Python!')
Hello Python!
>>>
```
## Write your first Python script file
Using any of your favorite Text Editor.
``` bash
$ vim 01_hello_python.py
```
Input `print("Hello Python!")` in your file.
``` bash
$ python 01_hello_python.py
Hello Python!

$
```

# Python Strings
## Python Strings
``` python
$ python

Python 3.x.xx ...
...

>>> message = 'Meet me tonight.'
>>> print(message)
Meet me tonight.
>>>
>>> message2 = "The clock strikes at midnight."
>>> print(message2)
The clock strikes at midnight.
>>>
```
## Python Strings
``` python
>>> message3 = 'I'm looking for someone to ...'
... ...
SyntaxError: invalid syntax
>>> message3 = 'I\'m looking for someone to ...'
>>> message3 = "I'm looking for someone to ..."
>>> message4 = "The word "apple" was not ..."
... ...
SyntaxError: invalid syntax
>>>
>>> message4 = 'The word "apple" was not ...'
>>>
```
## Python Strings
``` python
>>> complex_string = """no matter you have
... "double quote", or
... 'single quote', or multiple lines,
... this triple quote can handle."""
>>>
```
