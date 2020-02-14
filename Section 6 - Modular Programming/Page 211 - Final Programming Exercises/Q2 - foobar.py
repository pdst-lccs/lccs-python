
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


