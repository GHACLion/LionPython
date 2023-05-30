# Author：程序员良哥
# DateTime: 2023/3/4 11:04

# 逻辑运算符, 输出的结果为 Boolean 类型， true/false
a,b=10,20
print("a>b是否正确？", a>b)
print("a<b是否正确？", a<b)
print("a>=b是否正确？", a>=b)
print("a<=b是否正确？", a<=b)
print("a!=b是否正确？", a!=b)

'''
    = 称为 赋值运算符， 而 == 称为逻辑运算符
    一个变量由三部分组成: 标识、类型、值
    == 比较的是对象的 value 值
    is 比较的是对象的标识，即 内存地址
'''
a,b=10,10
# 输出看堆空间中 id 是否相同
print(id(a))
print(id(b))
# ==对比 value 值是否相等
print(a == b)
# is对比 内存地址是否相同 ，因为 id 相同，这里输出 true
print(a is b)
# is not 对比也是 内存地址,因为 id 相同，这里输出 false
print(a is not b)

# list集合对比
list1=[11,22,33]
list2=[11,22,33]
# 同样输出堆空间中 id , 对比 id 是否相等。我们发现 id 不同，即：list1 和 list2 不是同一个对象
print(id(list1))
print(id(list2))
# 输出 value 对比 和 id 对比
print(list1==list2) # True
print(list1 is list2) # False
print(list1 is not list2) # True

