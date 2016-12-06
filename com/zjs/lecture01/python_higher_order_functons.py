# coding: utf-8
'''
Created on 2016-12-6

@author: zhujisong
'''

# # Python高阶函数
# * 函数式编程
# 函数本身也可赋值给变量
import math
math.sqrt(25)

math.sqrt
fun = math.sqrt
fun
fun(10)

# 将函数作为参数
def func_add(x, y, f):
    """
        functional addition
    """
    return f(x) + f(y)

print func_add(4, 25, math.sqrt)
print func_add(-4, 25, abs)

# map/reduce
x_2_lst = [x**2 for x in range(10)]
print x_2_lst

x_sqrt_lst = map(math.sqrt, x_2_lst)
print x_sqrt_lst

x_2_float_lst = map(float, x_2_lst)
print x_2_float_lst

x_2_str_lst = map(str, x_2_lst)
print x_2_str_lst

# * reduce
str_lst = map(str, range(5)) # ['0', '1', ...]
print str_lst

def make_num(str1, str2):
    return int(str1) * 10 + int(str2)

result = reduce(make_num, str_lst)
print result

# 规范字符串
name_lst = ['poNNY MA', 'rObIN li', 'steve JOBS', 'bILL gates']
standard_name_lst = map(str, name_lst)
print standard_name_lst

# # filter
number_lst = range(-10, 10)

def is_negative(x):
    return x < 0

filtered_lst = filter(is_negative, number_lst)
print number_lst
print filtered_lst

# # map reduce filter 与匿名函数
# * map与匿名函数
x_lst = range(10)
result_lst = map(lambda item : item**2 +item**3, x_lst)
print x_lst
print result_lst

# * reduce与匿名函数
x_lst = range(1, 5)
product = reduce(lambda x, y : x*y, x_lst)
print x_lst
print product

# * filter与匿名函数
number_lst = range(-10, 10)
filtered_lst = filter(lambda x : x<0, number_lst)
print number_lst
print filtered_lst