from functools import wraps
from time import time

hellow_world = "Hello world!"

x = "foo"


def show_x(val):
    print(val)


print(x)
show_x(x)
print(x)


def greet(name="world"):
    print("Hellow", name.title())


def filter_names(names):
    for name in names[:]:
        if len(name) > 3:
            names.remove(name)
    return names


names = ["sam", "dot", "grey", "tod", "lili"]

print(names)
filtered_names = filter_names(names)
print("---", filtered_names)
print(names)

# greet()
# if hellow_world:
#     print(hellow_world[0], hellow_world[-1])
#     print(hellow_world)
#
# if hellow_world:
#     print(hellow_world[0], hellow_world[-1])
#     print(hellow_world)
#
# if hellow_world:
#     print(hellow_world[0], hellow_world[-1])
#     print(hellow_world)

i = 1
i_n = -1
b = True
s = "spam"
t = ("spam", "eggs")
l = ["foo"]

b = False

print(1 == True)
print(0 == False)
print(True + False + True)

s = set()
d = {}


def time_call(func):
    print("incomming func:", func)

    def wrapper(p):
        start = time()
        res = func(p)
        end = time()
        print("res for", p, " = ", res)
        time_taken = end - start
        print(f"inside wrapper {time_taken:.13f}")
        return res

    return wrapper


#
# @time_call
def fib(pos):
    if pos <= 1:
        return 1
    return fib(pos - 1) + fib(pos - 2)


fib_nums = []
for i in range(5):
    fib_nums.append(fib(i))


# print(fib_nums)
# print([fib(i) for i in range(5)])
#
# for i in range(5):
#     print("pos", i)
#     start = time()
#     res = fib(i)
#     end = time()
#     fib_nums.append(res)
#     print("res for", i, " = ", res)
#     time_taken = end - start
#     print(f"time: {time_taken:.13f}")
#
# timed_fib = time_call(fib)
# print("created new func")
# print(timed_fib(3))


def time_call_any(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print("res ", func, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return res

    return wrapper


@time_call_any
def add(a, b):
    return a + b


add(5, 10)


@time_call_any
def hello_ag(name="world"):
    return "hellow " + name


print('d', hello_ag())
print('d', hello_ag("Samm"))
print('d', hello_ag("slava"))

print('o', hello_ag.__wrapped__())
print('o', hello_ag.__wrapped__("Samm1"))
print('o', hello_ag.__wrapped__(name="slava1"))
