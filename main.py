hellow_string = 'hellow world'

print(repr(hellow_string))

hellow_multi = '''
hellow
world'
!'''

print(repr(hellow_multi))

hellow_string = 1

print(hellow_string)
print(type(hellow_string))
print(2 ** 64)
print((2 ** 64) ** 10)
print(2.001 ** 300)

float_val = 3.5
print(float_val.as_integer_ratio())

a = 4
b = 4

res = 100000 / 3
res_str = 'result {:2.1f}'.format(res)
print(res_str)

if a > b:
    print('a if great than b')
# elif a == b:
#     print('equal')
else:
    print('not great')

string_mes = 'asdgfgffgrt'

for c in string_mes:
    print(c, end=" ")

print()

my_list = ['a', 'b', 42, True, ['a', 2]]

for index, elem in enumerate(my_list):
    print(index, elem, end=" ")

my_tuple = ()
print(my_tuple)
my_tuple = (1., 2, True, False, "str", [1, 2])
print(my_tuple)
print(my_tuple[0])
