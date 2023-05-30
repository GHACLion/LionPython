# Author：程序员良哥
# DateTime: 2023/3/2 20:30

# 赋值运算符，运算顺序从右到左
i = 3 + 4
print(i)

a = b = c = 20
# id() 属性代表创建对象时开辟的内存空间的位置（堆中的位置）
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 由输出结果可见，a,b,c 三个对象所指向的堆空间的位置是一致的，abc在栈空间中，都创建了堆空间的引用，即id


# 支持参数赋值
a = 20
# 相当于 a=a+30
a += 30
print(a)
# 同理，其他算术运算赋值也是一样的
# 上述被重新赋值的 a= 50, a=a-10=40
a -= 10
print(a)
# a= a*2 = 80
a *= 2
print(a)
# a=a/3
a /= 3
print(a)
# 因为3不能被整除，此时 a 的类型由 int 转为 float
print(type(a))
# //代表整除, 因为 a 的类型由 int 转为 float，此时再执行整除2时，数据类型依然是 float 类型，所以输出结果是 13.0 而不是 13
a //= 2
print(a)
print(type(a))


#   支持解包赋值，解包赋值时，按照顺序，一一对应赋值，但是要求 参数个数 和 值的个数 对应，即：不能是 a,b = 10,20,30 , 只能是 a,b = 10,20
a, b, c = 10, 20, 30
print(a, b, c)


# 交换两个变量的值
a, b = 20, 30
print("交换之前：", a, b)
a, b = b, a
print("交换之后：", a, b)

# 交换多个变量的值
num1 = 10
num2 = 20
num3 = 30
num4 = 40
num1, num4, num3, num2 = num4, num2, num1, num3
print(num1, num2, num3, num4)

# 翻转一个四位数
num_4ws = 1234
# 取倒数第一位数 4
n0 = num_4ws % 10
# 取前三位 123， 给num_4ws 重新赋值 (1234 - 4) / 10 = 123
num_4ws = (num_4ws - n0) / 10
# 取倒数第二位数 3
n1 = num_4ws % 10
# 取前两位 12， 给 num_4ws 重新赋值 (123 - 3)  / 10 = 12
num_4ws = (num_4ws - n1) / 10
# 取倒数第三位数 2
n2 = num_4ws % 10
# 取第一位数 1 ， 给 num_4ws 重新赋值 （12 - 2） / 10 = 1
num_4ws = (num_4ws - n2) / 10
# 取倒数第四位数 1, 1 % 10 = 1
n3 = num_4ws % 10
num_4ws = (num_4ws - n3) / 10
# 对四位数进行翻转赋值
num_4ws = n0 * 1000 + n1 * 100 + n2 * 10 + n3 * 1
print(num_4ws)
