# Author：程序员良哥
# DateTime: 2023/3/4 17:52

# 程序结构分为三种：顺序结构，选择结构，循环结构

'''
    在讲解程序结构前，先了解一个概念：对象的布尔值, 它会影响我们 条件语句的判断
    Python一切皆对象，所有的对象都有一个布尔值
    获取的对象的布尔值，我们使用内置函数 bool()

    以下对象的布尔值为 False
    ● False
    ● 数值0
    ● None
    ● 空字符串
    ● 空列表
    ● 空元组
    ● 空字典
    ● 空集合
'''

# 测试对象的布尔值 为 False
print('-----------布尔值为 False------------')
print(bool(False))      # False
print(bool(0))          # 数值0
print(bool(None))       # None
print(bool(''))         # 空字符串
print(bool([]))         # 空列表
print(bool(list()))     # 空列表
print(bool(()))         # 空元组
print(bool(tuple()))    # 空元组
print(bool({}))         # 空字典
print(bool(dict()))     # 空字典
print(bool(set()))      # 空集合

# 除以上几种对象布尔值为 False 外，其他所有对象布尔值均为 True
print('-----------布尔值为 True------------')
print(bool(True))
print(bool(12))
print(bool('helloworld'))

# 举例说明 对象布尔值 影响 程序走向。 如果输入的 年龄值为 0, 0的布尔值为 false, 所以会 输出 else 中的语句
age = int(input('请输入你的年龄：'))
if age:
    print(age)
else:
    print("看到 对象布尔值 的威力了吗？")







# 顺序结构
'''把大象放进冰箱需要几步？'''
print('------程序开始-------')
print('1.把冰箱门打开')
print('2.把大象放进去')
print('3.把冰箱门关上')
print('------程序结束-------')



'''
重要提示：

    在介绍逻辑判断之前呢，有必要说明一下 Python 中的 缩进。
    在 Java 或者 C 或 C++ 等语言中，我们会使用 大括号{} 代表一个组合的代码块。
    但是：
    在 Python 中， 
    1. if 必须和 英文冒号 : 连用 
    2.我们使用的 仅仅是 缩进 来代表同一逻辑下的代码块。所以，同一个 if 条件下的多个执行，全部都需要 缩进 。且仅 缩进 一次。
    3.如果在 if 下取消了缩进，我们就认为，未缩进代码，与 if 同级，并不归属于 if 条件
    4.在 if 语句块内部，也不能随意使用缩进，会出现 语法错误 ，使用 嵌套if 条件时，每个 if 下，独立去计算 缩进
    
    举例：
    x = 1
    if x > 0
        print("X大于1")
            print("语法错误") # 如果在这里继续使用 缩进，会有语法错误。
    
    缩进 在 Python 中有特殊的含义，并不能随便使用。 
    
    举例：如果没有 if 判断，就不能使用缩进
    x = 1 
        print(x) # 使用缩进后虽然可以正常运行，但是会提示 语法错误
        
    举例： 使用 嵌套 if 时，每个 if 下的 缩进 需要独立计算
    x = 1
    if x > 0:
        print("X大于0")
        if x < 100:
            print("X小于100") # 这样再执行 缩进 就是正确的；
'''

# 举例说明
a = float(input("请输入一个数字与100比较："))
if a > 100:
    print("大于100啦，还得是我输入的比较大")
    print("我还在 if 条件里")
print("好家伙，无论if条件是否满足，我都在 if 条件之外，我和 if 同级别，if 条件无论是否满足，我都执行")



'''
    下面介绍 单分支语句， 双分支语句， 多分支语句
'''

# 选择结构 之 单分支语句
money = 1000 # 余额
s = int(input('请输入取款金额: '))  # 取款金额
# 对余额进行判断，余额大于取款金额，吐出钞票，反之，余额小于取款金额，提示“余额不足”，返回上级
if money >= s:
    money = money - s     # 使用 Tab 缩进代表方法体，取款后，给余额重新赋值
    print('取款成功，余额为：', money)
# 单分支语句对条件表达式以外的，不执行，比如：余额1000，我取1200，则跳过方法体，因为是单分支结构，不满足条件，程序直接结束。
print("执行结束")



# 选择结构 之 双分支语句写法1
num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(num, '为偶数')
else:
    print(num, '为奇数')
print("执行结束")


# 选择结构 之 双分支语句写法2（写法2是对上述写法1的简写形式） 例1：判断输入奇偶数
num = int(input('请输入一个整数：'))
print("该数为偶数" if num % 2 == 0 else "该数为奇数")

#  选择结构 之 双分支语句写法2（写法2是对上述写法1的简写形式） 例2：判断输入的两个数的大小
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))
# if 条件表达式 判断结果为 true, 执行 if 左侧的语句，如果 if 条件表达式判断结果为 false, 执行 else 右侧的语句
print(str(num_a) + '大于等于' + str(num_b)  if  num_a >= num_b  else   str(num_a) + '小于' + str(num_b))


# 选择结构 之 多分支语句
'''
    从键盘录入一个 0~100 整数，用来代替成绩
    90~100  A
    80~89   B
    70~79   C
    60~69   D
    0~59    E
    小于0 或者 大于100 为非法数据
'''
score = int(input('请输入你的成绩: '))
if 100 >= score >= 90:
    print('你的成绩为：', score, '分， 等级为 A')
elif 90 > score >= 80:
    print('你的成绩为：', score, '分， 等级为 B')
elif 80 > score >= 70:
    print('你的成绩为：', score, '分， 等级为 C')
elif 70 > score >= 60:
    print('你的成绩为：', score, '分， 等级为 D')
elif 60 > score >= 0:
    print('你的成绩为：', score, '分， 等级为 E')
else:
    print('非法成绩：请输入 0~100 的整数成绩')

# 选择结构 之 嵌套if语句
'''
    超市购物活动
    会员折扣：
        1.会员 >= 200     8折
        2.会员 >= 100     9折
    非会员折扣：
        1.非会员 >= 200    9.5折
    其他不打折
'''
answer = input('您是会员吗？ y/n')
money = float(input('请输入您的消费金额：'))
# 判断是否会员
if answer == 'y':
    # 会员计算
    if money >= 200.00:
        print('尊敬的会员，您享受8折优惠，折后金额为：', money*0.8)
    elif 100.00 < money < 200.00:
        print('尊敬的会员，您享受9折优惠，折后金额为：', money*0.9)
    else:
        print('尊敬的会员，您本次消费不享受折扣优惠，已为您累计', int(money), '积分')
else:
    # 非会员计算
    if money >= 200.00:
        print('尊敬的非会员用户，您享受9.5折优惠，折后金额为：', money*0.95)
    else:
        print('尊敬的非会员用户，您本次消费无法享受优惠，请支付：', money, '元')