from utils import *

"""
May as well learn pytest while doing this


"""



test1 = "234 sdflj 39j [21] 321 [A] [21]"
test2 = "2423 234_465 234 1231_12 [213]A [BC] _D_"


def testNumbers():
    assert getNumbers(test1) == [234, 39, 21, 321, 21]
    assert getNumbers(test2) == [2423, 234, 465, 234, 1231, 12, 213]


def testLetters():
    assert getLetters(test1) == ["j", "A"]
    assert getLetters(test2) == ["A", "D"]