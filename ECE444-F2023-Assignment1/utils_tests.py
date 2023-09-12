#utils_func contains utils class with two functions 'reversed' and 'formatter' that take only integer inputs and return their reversed, binary and octal form
#this file tests the functionality of utils_func with float, string and integer inputs

import utils_func

util_functions = utils_func.utils()
float_num =float(input("Please enter a decimal value: "))
string = input("Please enter a string text: ")
integer = int(input("Please enter an integer value: "))

print("\n----------Here are the function results to the inputs provided----------\n")

print("Function 'reversed'")
util_functions.reversed(float_num)
util_functions.reversed(string)
util_functions.reversed(integer)
print("\nFunction 'formatter'")
util_functions.formatter(float_num)
util_functions.formatter(string)
util_functions.formatter(integer)

print("\n----------END OF UTILS_TEST----------\n")