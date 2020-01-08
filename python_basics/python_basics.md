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
## Single or Double Quote
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
## Mixed Quotes
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
## Triple Quote
``` python
>>> complex_string = """no matter you have
... "double quote", or
... 'single quote', or multiple lines,
... this triple quote can handle."""
>>>
```
# Numbers in Python
## Numbers in Python Version 2
``` python
$ python

Python 2.x.xx ...
...

>>> # Types of numbers: int, long, float, complex
... # Whole numbers: int, long
...
>>> a = 28  # This is an integer
>>> type(a)
<type 'int'>
>>> a
28
>>> print(a)
28
>>>
```
## Numbers in Python Version 2
``` python
>>> import sys
>>> sys.maxint
2147483647
>>> b = 2147483647
>>> type(b)
<type 'int'>
>>> c = 2147483648
>>> type(c)
<type 'long'>
>>> c
2147483648L
>>> print(c)
2147483648
>>>
```
## Numbers in Python Version 2
``` python
>>> d = -sys.maxint - 1
>>> type(d)
<type 'int'>
>>> d
-2147483648
>>> e = -2147483649
>>> type(e)
<type 'long'>
>>>
>>> f = 1L
>>>
```
## Numbers in Python Version 2
### Floats
``` python
>>> e = 2.718281828
>>> type(e)
<type 'float'>
>>>
```
### Complex Numbers
``` python
>>> z = 3 + 5.7j
>>> type(z)
<type 'complex'>
>>> z.real
3.0
>>> z.imag
5.7
>>>
```
