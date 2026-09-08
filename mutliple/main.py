# import support

# print(support.add_2_numbers(1,2))
# print(support.var)
# test = support.Test()
# print(test.a, test.some_method())

from support import *

test = Test()
print(test.a, test.some_method(), var, add_2_numbers(2,4))