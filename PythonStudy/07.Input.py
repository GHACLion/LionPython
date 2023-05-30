# Author：程序员良哥
# DateTime: 2023/3/2 19:39

# 输入函数 input()
# 可以用来提出问题，待用户输入答案后，把用户输入内容赋值给变量，再打印变量
present=input('大圣想要什么礼物呢？')
print(present,type(present))

# 从键盘录入两个整数，计算两个整数的和
a=input('请输入一个加数：')
b=input('请输入另一个加数：')
print(type(a), type(b))
print(a+b)
# 注意：input默认输入的类型是 str , 所以上述 a+b 相当于进行了 输入的两个字符串的拼接
# 解决方案有多种，我们可以先赋值再转换
a=int(input('请输入一个加数：'))
b=int(input('请输入另一个加数：'))
print(type(a), type(b))
print(a+b)
