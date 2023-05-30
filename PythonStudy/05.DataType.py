# Author：程序员良哥
# DateTime: 2023/3/1 20:08

# 常用数据类型

# 整数类型
n1 = 65
n2 = -36
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))

# 整数型可以表示为 十进制，二进制，八进制，十六进制
print('十进制', 118)
# 二进制以 0b 开头，b为小写
print('二进制', 0b10100111)
# 八进制以 0o 开头，o为小写
print('八进制', 0o176)
# 十六进制以 0x 开头，x为小写
print('十六进制', 0x2AEF)

# 浮点类型
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)
print(n1+n3)
# 注意，这里导入 Decimal 的包
from decimal import Decimal
# 导包以后，输出就会很精确，不会出现类似于上方 n1+n2这种不精确的情况。当然，上方不精确的情况不绝对，只是有时会出现
print(Decimal('1.1')+ Decimal('2.2'))


#布尔类型
# 布尔值可以转化为整数，我们直接拿过来执行计算就可以了，true--> 1 \ false --> 0
print(True+1)
print(False+1)
# 我们可以查看 true \ false 的数据类型
t1=True
f2=False
print(t1, type(t1))
print(f2, type(f2))


# 字符串类型
# 单引号和双引号定义的字符串必须在同一行，三引号定义在字符串可以分布在连续的多行
str1='关注良哥，java python双飞'
str2="关注良哥，java python双飞"
str3='''关注良哥，
        java python双飞'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
