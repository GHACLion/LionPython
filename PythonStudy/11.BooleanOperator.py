# Author：程序员良哥
# DateTime: 2023/3/4 11:29

# 布尔运算符
'''
    Python 严格区分大小写，能识别的 Bool 类型只有两个值
    True & False
    Python 无法识别：TRUE, TRue, TRUe , FAlse, FaLsE 等
'''


# and 逻辑与  全真为真，有假则假
a, b = 1, 2
print(a == 1 and b == 2)  # true and true --> true
print(a == 1 and b < 2)   # true and false --> false
print(a != 1 and b == 2)  # false and true --> false
print(a != 1 and b != 2)  # false and false --> false

# or 逻辑或    有真为真，全假则假
print(a == 1 or b == 2)   # true and true --> true
print(a == 1 or b < 2)   # true and false --> true
print(a != 1 or b == 2)  # false and true --> true
print(a != 1 and b != 2)  # false and false --> false


# not 的用法，对 Boolean 类型的运算数取反，真为假，假为真
q1 = True
q2 = False
print(not q1)  # not True --> False
print(not q2)  # not False --> True


# in & not in 的用法
s = 'hello world'
print('w' in s)
print('q' in s)
print('w' not in s)
print('q' not in s)