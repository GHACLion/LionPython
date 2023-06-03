# Author：程序员良哥
# DateTime: 2023/3/2 20:08

# 算术运算符

print(1 + 1)  # 加法运算

print(2 - 1)  # 减法运算

print(3 * 6)  # 乘法运算

print(1 / 2)  # 除法运算
print(11 / 2)  # 除法运算

print(11 // 2)  # 整除运算，商值取整

print(11 % 2)  # 取模运算

print(2 ** 3)  # 幂运算，相当于 2*2*2

# 计算圆形的周长和面积
radius = 5
PI = 3.14159265354
# 圆形面积：Πr²
area = PI * radius ** 2
# 圆形周长：2Πr
perimeter = 2 * PI * radius
# 因为禁止 string 类型和 float 类型拼接，所以对 float 数值进行强制类型转换
print('圆形的面积为：' + str(area))
print('圆形的周长为：' + str(perimeter))

# 控制小数点的位数
'''
    保留 3 位小数
    print('%.3f' % 变量名)
    
    保留 2 位小数
    print('%.2f' % 变量名)
    
    保留 1 位小数
    print('%.1f' % 变量名)
'''
weight = float(input("苹果的重量是："))
price = float(input("苹果的单价是："))
# 计算苹果的价格，定义变量 cost = 重量 * 单价
cost = weight * price
# 原始精度
print(cost)
# 保留 3 位小数
print('%.3f' % cost)
# 保留 2 位小数
print('%.2f' % cost)
# 保留 1 位小数
print('%.1f' % cost)

# 练习题
'''
    有一笔钱用于投资，金额用 money 表示，单位为元
    投资期限用 month 表示，单位为月
    每个月的利息用 rate 表示，单位为百分之一
    按每个月计算复利，那么到期后可以得到多少利息？
'''
# 复利的计算公式是:F=P(1+i)^n 。P为本金，i为投资回报率，n为时间，F为本利和。
money = float(input('请输入投资金额（单位：元）：'))
month = float(input('请输入投资期限（单位：月）：'))
# 这里利率用户输入 float 类型收益即可， 比如 17.6% ，这里只输入 17.6
rate = float(input('请输入收益率：'))
# 利率转化为 百分比，这里转化为 17.6%
rate = rate / 100
earnings = money * (1 + rate) ** month
print("到期后本息共计：" + str('%.2f' % earnings))

# 翻转浮点数
'''
注意：
    翻转仅支持对 str 类型的字符串进行翻转， 翻转格式：   hello[::-1]
    在对数字进行反转时，我们先吧数字转换为 str 类型，翻转后，再对 str 类型转换为数字类型
    
    举例
    aaa = 'Hello World'
    aaa = aaa[::-1]
    print(aaa)
'''
a = float(input('请输入一个数字：'))
# 翻转仅支持 str 类型，所以先对数字进行类型转化
a = str(a)
# 翻转的标准写法 ： a = a[::-1]
# 其实在这里，我们可以省略后续的类型转化，直接在这里反转后转化类型，写为  a = float(a[::-1])
a = float(a[::-1])
print(a, type(a))
"""
    注意上方，这里会有一个 Bug , float类型有精度限制，str 进行翻转后再转回 float 会可能出现精度的丢失
    比如：输入：6441651354684351.31654546565 超过float的取值范围，翻转后再转化，就出现了精度的丢失，不是我们期待的结果
"""


# 这里我们回到开头的第一个练习题，计算圆的周长和面积，半径让用户输入
redius = float(input('请输入圆形的半径：'))
PI = 3.14159265354
perimeter = 2 * PI * redius
print("该圆周长为：", perimeter)
# 如果对小数位数有规定，我们可以进行截取，默认四舍五入
print("该圆周长为(保留2位小数)：", '%.2f' % perimeter)
area = PI * redius ** 2
print("该圆面积为：", area)
# 同理，取小数点后2位，默认四舍五入
print("该圆面积为(保留2位小数)：", '%.2f' % area)


