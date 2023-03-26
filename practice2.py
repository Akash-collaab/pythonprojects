'''

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)


range(10)




a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i, a[i])
    

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print (n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number ", num)

This is commonly used for creating minimal classes:
   Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:
   


 class MyEmptyClass:
    pass


def fib(n):
    print("Print a fibonacci series upt to n.")
    a,b = 0,1
    while a < n:
        print(a)
        a, b = b, a+b

fib(2000)



  Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it’s a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using print:

>>> fib(0)
>>> print fib(0)
None


def fib2(n):
    result = []

    a, b = 0 ,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    
fib2(100)

def ask_ok(prompt, retries = 4, complaint ='yes or no, please'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('not valid argument')
        print(complaint)

i = 5

def f(arg=1):
    print(arg)
i = 6
f()


def f(a, L=[]):
    L.append(a)
    return(L)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(2))
print(f(3))
print(f(1))


x=4.0
y="raj"
print(type(x))
print(type(y))



def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind,"?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

range(3, 6)             # normal call with separate arguments
[3, 4, 5]

args = [3, 6]
range(*args)            # call with arguments unpacked from a list
[3, 4, 5]


def make_increment(n):
    return lambda x:x+ n 
f = make_increment(42)
f(0)

f(1)



a = [66.25, 333, 333, 1, 1234.5]
print (a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

a.index(333)





# List as a ques using append and pop methods


from collections import deque
queue = deque(["Eric", "John", "Michael"]) 
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
print(queue)


gsbazyclpbqdxdcz




def f(x):
    return x % 3 == 0 or x % 5 == 0
filter(f, range(2, 25))

def cube(x):
    return x*x*x
map(cube, range(1,11))

'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# we can obtain from this also
squares = [x**2 for x in range(10)]
print(squares)

# this listcomp combines the elements of two lists if they are not equal:
x = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(x)

# And it’s equivalent to:

combs = []
for x in (1,2,3):
    for y in (3,1,4):
        if x!=y:
            combs.append((x,y))
print(combs)

