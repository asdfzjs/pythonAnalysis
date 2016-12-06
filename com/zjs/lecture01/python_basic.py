# coding: utf-8
'''
Created on 2016-12-6

@author: zhujisong
'''
# * 大部分python对象是可变的
a = 5
a = 6
print a

# *　字符串个元组是不可变的
#字符串
str = 'Hello zjs'
#str[-1] = '!'

#元组
tup = (1,2,3)
#tup[0] = 2

#*三重引号(""" """)
def print_info():
    """
        This is a function for information print
    """
    print 'hello zjs'

#* 字符串格式化(%)   
print '%d %s cost me $%.2f' %(2,'cars',10000.233)

#* 类型转换
s_val = '3.141592657'
print 'string value: %s' %s_val
f_val = float(s_val)
print 'float value: %f' %f_val
i_val = int(f_val)
print 'int value: %i' %i_val

##时间日期
#*datetime 模块
from datetime import  datetime
dt = datetime(2016,12,3,15,9,9)
print dt.month,dt.hour

# * strftime将datetime类型格式化为字符串  格式化一个日期
dt.strftime('%Y/%m/%d %H:%M')
dt.strftime('%d/%m/%Y %H:%M')

# * strptime将字符串解析为datetime类型
datetime.strptime('20161203','%Y%m%d')

##控制流 if else
m = -1
if m < 0:
    print 'negative'
elif m >0:
    print 'positive'
else:
    print 'zero'

# # for循环 continue, break
l = xrange(20)
for i in l:
    if i%2 ==0:
        continue
    if i ==15:
        break
    print i

#while循环
i = 1
sum = 0
while i<=100:
    sum +=i
    i +=1
print sum

#空函数
def f():
    pass

#异常处理
def divide(x,y):
    """
        do division
    """
    try:
        return x/y
    except:
        return 'error happens'
print divide(8,2)
print divide('8', 2)

#range 和 xrange python3中range已经被移除，把xrange重命名成range,xrange做循环的性能比range好，尤其是返回很大的时候。尽量用xrange吧，除非你是要返回一个列表
range(1,20,2)
print list(xrange(1,20,2))

#* 变量传递
a = 5
b = a
a =3
print a 
print b

def fun1(a):
    a = 2
    print a

b = 3
fun1(b)
print b

#* 列表传递
l_1 = [1,2,3]
l_2 = l_1
l_1.append(4)
print l_1
print l_2

def fun2(lst):
    lst[0] = 5
    print lst
    
lst1 = range(5)
print lst1

fun2(lst1)
print lst1


# * 浅拷贝 和 深拷贝

# In[9]:

import copy
 
a = [[1, 2, 3], [4, 5, 6]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
 
print 'a-id:', id(a)
print 'b-id:',id(b)
print 'c-id:',id(c)
print 'd-id:',id(d)

a.append(15)
a[1][2] = 10

print 'processed...'
print a
print b
print c
print d
#if __name__ == '__main__':
#    pass