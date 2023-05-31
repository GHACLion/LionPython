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