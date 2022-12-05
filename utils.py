import re
"""
Advent of Code 2022 - Utility functions

Some functions I figured might be useful enough to have at the ready.

"""

def getNumbers(string):
    """
    Return list of numbers from a string
    Added before day 6
    
    """
    return list(map(int, re.findall(r"\d+", string)))

def getLetters(string):
    """
    Return list of single letters *that are not adjacent to other letters*
    Added before day 6
    
    """
    return re.findall(r"(?<![A-Za-z])[A-Za-z](?![A-Za-z])", string)





if __name__ == "__main__":
    print("Testing utilities")
    test1 = "234 sdflj 39j [21] 321 [A] [21]"
    print(f"Numbers: {getNumbers(test1)}")
    print(f"Letters: {getLetters(test1)}")