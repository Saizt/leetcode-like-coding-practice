import inspect
import numpy as np
from collections import namedtuple
from typing import NamedTuple


class Creature:
    def __init__(self, x):
        self.x = x

    def initial_parent_func(self):
        return "this is an initial parent func"


class Animal(Creature):
    def __init__(self, x, y):
        super().__init__(x) #inherits Creature's __init__
        self.y = y

    def parent_func(self):
        return "this is a parent func"

    def speak(self):
        return "sound"


class Dog(Animal): 
    #inherits Animal's __init__ automatically because we don't redefine __init__
    def speak(self):
        parent_result = super().speak()
        return "woof is from me", parent_result + " is from parent"


# NamedTuples are immutable
Point_old = namedtuple("Point", ["x", "y"]) # Old-style
class Point(NamedTuple): #Modern
    x: float
    y: float


def safe_print_attrs(obj):
    """Quick runtime introspection helper for unfamiliar objects."""
    print("type:", type(obj))
    print("class:", obj.__class__)
    print("mro:", type(obj).__mro__)
    print("__dict__:", getattr(obj, "__dict__", "<no __dict__>"))
    print("_fields:", getattr(obj, "_fields", "<no _fields>"))
    print(
        "public-ish attrs:",
        [name for name in dir(obj) if not name.startswith("__")]
    )


class BaseProcessor:
    def process(self, x):
        return self.transform(x)

    def transform(self, x):
        return x


class NormalizingProcessor(BaseProcessor):
    def transform(self, x):
        return x / 10


def inner(values):
    """
    breakpoint()    enter debugger
    p x             print expression (p locals() shows all local variables for example)
    pp x            pretty-print (same, but rendered?)
    n               execute next line
    s               step into called function
    c               continue
    l               list nearby source (l . shows around current exec. line, l 20 shows around line 20, l 20,35 shows 20-35 lines)
    w               show call stack
    u               move one stack frame up
    d               move one stack frame down
    q               quit
    r               return (continue execution until the current function returns)
    """
    breakpoint() #for pdb debugging
    return sum(values)


def middle(values):
    doubled = [x * 2 for x in values]
    return inner(doubled)


def outer():
    data = [1, 2, 3]
    return middle(data)
    

if __name__=="__main__":
    d = Dog(x="mamal", y="dog")
    print("x =", d.x, "y =", d.y)
    print("d.speak()", d.speak())
    print("Animal.__name__", Animal.__name__)
    #Python searches according to the MRO for methods/variables
    print("Animal.__mro__", Animal.__mro__)
    print("Dog.__name__", Dog.__name__)
    print("Dog.__mro__", Dog.__mro__)

    help(Dog)

    print("d.__class__", d.__class__) #tells you the runtime class
    print("d.__dict__", d.__dict__) #shows instance attributes
    print("type(d)", type(d)) #What object am I even looking at?
    print("dir(d)", dir(d)) #Shows available attributes/methods.
    print("vars(d)", vars(d)) #equivalent to print(d.__dict__)

    print("Inspect")
    print("inspect.getsource(type(d))", inspect.getsource(type(d)))
    print("inspect.signature(d.speak)", inspect.signature(d.speak))
    print("inspect.getfile(type(d))", inspect.getfile(type(d)))

    print("NamedTuple")
    p = Point(3, 4)
    print(p.x, p.y, p[0], p[1])
    p = Point_old(3, 4)
    print(p.x, p.y, p[0], p[1])
    print(p._fields)
    print(p._asdict())
    print(
        "NamedTuple note: instances are tuple-based "
        "and usually do not have __dict__"
    )
    print(type(p))
    print(
        "p.__dict__ (safe):",
        getattr(p, "__dict__", "<no __dict__; NamedTuple is tuple-based>")
    )
    print("dir(p):", dir(p))
    print("safe_print_attrs(p)")
    safe_print_attrs(p)
    p2 = p._replace(x=10)
    print(p2.x, p2.y, p2[0], p2[1])

    print(
        "Dynamic dispatch: a parent method calling "
        "self.some_method() can invoke a child override."
    )
    p = NormalizingProcessor()
    print(p.process(50))
    print(type(p)) #If behavior surprises you, inspect
    print(type(p).__mro__)

    print(p.process) # shows the bound method object, which tells you which implementation is actually bound
    print(
        "process implementation:",
        p.process.__func__ #can reveal the underlying function for bound methods
    ) # BaseProcessor.process
    print(
        "transform implementation:",
        p.transform.__func__
    ) # NormalizingProcessor.transform
    print("safe_print_attrs(p)")
    safe_print_attrs(p)

    print("\nPDB STACK PRACTICE")
    result = outer()
    print("result:", result)

    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
    ])
    b = np.array([10, 20, 30])
    print(A.shape)  # (2, 3)
    print(b.shape)  # (3,)
    print(A + b)

    x = np.nan #floating-point value
    print(x == np.nan)       # False
    print(x != np.nan)       # True
    print(np.isnan(x))       # True
    print(x is None)         # False

    a = np.array([1.0, np.nan, 3.0])

    print(np.min(a))   # nan
    print(np.max(a))   # nan
    print(np.sum(a))   # nan

    x = np.array([0, 2, 2, 1, 2])
    print(np.bincount(x)) #[1 1 3] The index is the value of x; the stored number is its count.

    x = np.array([0, 5, 0, 7])
    print(np.nonzero(x)) # returns indexes of nonzero values of x, smth like (array([1, 3]),)

    A = np.array([
        [0, 5, 5],
        [7, 0, 4],
    ])
    rows, cols = np.nonzero(A)
    print(rows)  # [0 1]
    print(cols)  # [1 0]
    print(np.nonzero(A))

    x = np.array([1, 5, 2, 8])
    result = np.where(x > 3, 100, 0) # if cond, choose A, else choose B
    print(result) # [0, 100, 0, 100]
    print(np.where(x > 3)) # returns indexes (another form without choices)

    rng1 = np.random.RandomState(42) #gives reproducible pseudorandom results
    rng2 = np.random.RandomState(42)

    print(rng1.rand(3))
    print(rng2.rand(3)) #Both produce the same sequence because the seed is identical

    np.random.seed(42)
    a = np.random.randint(0, 100)
    b = np.random.randint(0, 100)
    np.random.seed(42)
    c = np.random.randint(0, 100)
    d = np.random.randint(0, 100)
    print(a == c)  # True
    print(b == d)  # True

    x = np.array([[1, 5, 2, 8]])
    print(x)
    print(type(x))
    print(x.shape)
    print(x.dtype)
    print(x.ndim)
    print(x)

    