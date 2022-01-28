print('hello', 'world')

other_print = print
other_print('this is just print with a new name')

def do_math(num1, num2=7):
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return result

print(do_math(5))
print(do_math(8, 10))

import operator
print(operator.add(2, 2))   # 2 + 2
print(operator.not_(True))  # not True

def other_function(arg1, arg2='a', arg3=None, arg4=True, arg5='hello'):
    pass

other_function(1, arg4=False)