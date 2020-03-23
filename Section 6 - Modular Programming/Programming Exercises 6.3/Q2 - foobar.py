# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q2(a)
# Purpose: A program to demonstrate the effect of function calls


def foo():
    print("Starting foo()")
    print("Leaving foo()")

# The following function just displays two lines
def bar():
    print("Starting bar()")
    foo()
    print("Leaving bar()")


def foobar():
    print("Starting foobar()")
    bar()
    print("Leaving foobar()")


foo()
bar()
foobar()

