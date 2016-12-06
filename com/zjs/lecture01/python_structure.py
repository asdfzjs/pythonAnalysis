# coding: utf-8
'''
Created on 2016-12-6

@author: zhujisong
'''
#* 创建元组
tup1 = 1, 2, 3
print tup1

# 嵌套元组
tup2 = (1,2,3),(4,5)
print tup2

#* 转换为元组, list->tuple , string -> tuple
l = [1,2,3]
print tuple(l)

str = 'hello zjs'
print tuple(str)

#* 访问元组
tup3 = tuple(str)
print tup3[4]

#* 合并元组
tup1 + tup2

#* 拆包
a,b,c = tup1
print b

# 函数返回多个值  "_"表示不取这个位置的值
def return_multiple():
    t = (1,2,3)
    return t
a,_,c = return_multiple()
print c

#元组列表迭代
tuple_lst = [(1,2),(3,4),(5,6)]
for x,y in tuple_lst:
    print x+y

#*  count 方法
tup3.count('l')

#* 列表
# * 创建列表
lst_1 = [1,2,3,'a','b',(4,5)]
print lst_1

lst_2 = range(1,9)
print lst_2

#*  转换为列表，tuple -> list
lst_3 = list(tup3)
print lst_3

lst_4 = range(10)

#末尾添加
lst_4.append(11)
print lst_4

#指定位置插入
lst_4.insert(5, 12)
print lst_4

# 删除指定位置的元素并返回
item = lst_4.pop(6)
print item
print lst_4

# 删除指定的值，注意12在这里是“值”，不是“位置”
lst_4.remove(12)
print lst_4

#*合并列表
lst_3 = lst_1 + lst_2
print lst_3

lst_1.extend(lst_2)
print lst_1

#* 排序操作
import random
lst_5 = range(10)
random.shuffle(lst_5)

lst_5.sort()
print lst_5

lst_6 = ['welcome','to','python','Data','Analysis','Course']
lst_6.sort()
print lst_6

lst_6.sort(key = len, reserse=True)
print lst_6

print lst_5
print lst_5[1:5]
print lst_5[5:]
print lst_5[:5]
print lst_5[-5:]
print lst_5[-5:-2]
print lst_5[::2]
print lst_5[::-1]

## 常用序列函数
#*　enumerate
lst_6 = ['welcome','to','python','data','analysis','Course']
for i ,item in enumerate(lst_6):
    print '%i-%s' %(i,item)

str_dict = dict((i, item) for i, item in enumerate(lst_6))
print str_dict


import random
lst_5 = range(10)
random.shuffle(lst_5)
print lst_5

#sorted
lst_5_sorted = sorted(lst_5)
print lst_5
print lst_5_sorted


# * zip 压缩
lst_6 = ['Welcome', 'to', 'Python', 'Data', 'Analysis', 'Course']
lst_7 = range(5) #[0, 1, 2, 3, 4]
lst_8 = ['a', 'b', 'c']
zip_lst = zip(lst_6, lst_8, lst_7)
print zip_lst


# * zip * 解压缩
zip(*zip_lst)

list(reversed(lst_6))

#* 创建字典
empty_dict = {}
dict1 = {'a': 1, 2: 'b', '3': [1, 2, 3]}
print empty_dict
print dict1

# * 插入元素
dict1[4] = (4, 5)
print dict1

del dict1[2]
print dict1

a_value = dict1.pop('a')
print a_value
print dict1

# * 获取键、值列表
print dict1.keys()
print dict1.values()

# * 合并字典
dict2 = {4: 'new1', 5: 'news'}
dict1.update(dict2)
print dict1

# * 通过多个列表创建字典
dict_3 = {}
l1 = range(10)
l2 = list(reversed(range(10)))
for i1, i2 in zip(l1, l2):
    dict_3[i1] = i2
print dict_3

dict_4 = dict(zip(l1, l2))
print dict_4

# # hash函数
hash(12)
hash('test hash')
hash((1, 2, 3))
hash([1, 2, 3])

#集合 set
a = set(range(10))
print a
b = set(range(5,15))
print b

# * 并 交 差 异或
a | b
a & b
a - b
a ^ b   #异或

# * 判断是否为子集、父集
a.issubset(b)  #判断是否是其子集
a.issuperset(b)  #判断是否是其父集
