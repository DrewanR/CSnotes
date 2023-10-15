---
tags:
  - Python
  - Programming
  - testing
---
# [Doc Test](https://docs.python.org/3.8/library/doctest.html)module
The doc test module is a module within python that tests a given program's functions in reference to examples given in comments.
Within [[_CM1101 Computational Thinking|CM1101]] they use the tests here for testing and said tests for marking.
Presumably, other modules also use this with python.
## Running a test
The easiest wat to run a test is from the command line.
`python -m doctest -v game.py`
Runs a detailed test showing successes and failures. Remove the -v for less detailed tests.

Make sure you run with with the current folder selected, an easy way to do this is open it in file explorer, click on the address box and type in `cmd` (Windows specific).
##  Creating tests (example)
*Source: [CM1101 EX4 Game.py](https://cf-my.sharepoint.com/:u:/r/personal/rutherforda2_cardiff_ac_uk/Documents/Documents/CM1101/L%20EX%204/game1_template/game.py?csf=1&web=1&e=DIOdqk)*
```python
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:

    >>> remove_punct("Hello, World!")
    'Hello World'
    >>> remove_punct("-- ...Hey! -- Yes?!...")
    ' Hey  Yes'
    >>> remove_punct(",go!So.?uTh")
    'goSouTh'
    """
    
    index = 0
    while index < len(text):
        if text[index] in string.punctuation:
            text = remove_character_at_index(text, index)
        else:
            index += 1
    return text
```
`NOTE:` the documentation string at top second half. This function should currently pass all the tests, provided that `remove_character_at_index(text, index)` is present.