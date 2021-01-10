from functools import wraps
from time import time


def pow(up_to, e=2):
    results = []
    for i in range(up_to):
        results.append(i ** e)

    return results


print("pow up to 13", pow(13))


def pow_gen(up_to, e=3):
    print('pow gen')
    for i in range(up_to):
        print("process", i)
        yield i ** e
        print("continue", i)


print("pow_gen up to 13", list(pow_gen(13)))
for i in pow_gen(13):
    print(i)
    if i > 100:
        print("i is gt 100")
        break


def true_and_false(val=True):
    val = True
    while True:
        yield val
        val = not val


g = true_and_false()

for i in range(100):
    print(next(g))

