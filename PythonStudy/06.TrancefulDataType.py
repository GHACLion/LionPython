# Author：程序员良哥
# DateTime: 2023/3/1 20:45

# 数据类型转换

# str()函数   将其他数据类型转换为 str 类型
name = '良哥'
age = 30
# int类型的年龄不能直接进行字符串拼接，我需要将年龄转换为字符串类型， 使用：str(age)
print('我是' + name + ', 今年' + str(age) + '岁')

a = 10
b = 90.4
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))




# int()函数   将其他数据类型转换为 int 类型
s1 = '123'
s2 = 98.4
s3 = '54.86'
s4 = True
s5 = 'hello'
# 将 str 转成 int 类型，字符串为 整数数字串
print(int(s1), type(int(s1)))
# 将 float 转成 int 类型，截取整数部分，舍掉小数部分
print(int(s2), type(int(s2)))
# 将 str 转成 int 类型，报错，因为字符串为 小数串
#报错 print(int(s3), type(int(s3)))
# 将 bool 转成 int 类型，true =1 , false =0
print(int(s4), type(int(s4)))
# 将 str 转成 int 类型，报错，引文字符串必须为 整数数字串， 非数字串不允许转换
# print(int(s5), type(int(s5)))




# float()函数     将其他数据类型转成 float 类型
s1='123.36'
s2='98'
s3=True
s4='hello'
s5=76
print(type(s1), type(s2), type(s3), type(s4), type(s5))

print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(s3), type(float(s3)))
# 字符串中的数据如果是非数字串，则不允许转换
# print(float(s4), type(float(s4)))
print(float(s5), type(float(s5)))
