# Author：程序员良哥
# DateTime: 2023/2/28 20:30

# 转义字符
# \ + 转义功能的首字母，

# \n--> newline 表示换行
print('hello\nworld')

# \t--> tab 表示横向制表位
# 注意：一个制表位占4个字符，
# 所以第一个 hello的最后一个o 加三个空格，占一个制表位，所以空格为3个字符，
# 而第二个 helloooo 占据两个完整的制表位，再执行\t 时，输出空格为4个字符，即一个完整的制表位，所以第二个输出看起来，间隔比第一个大
print('hello\tworld')
print('helloooo\tworld')

# \r --> enter 表示回车，
# world 会覆盖掉 hello , 仅输出 world
print('hello\rworld')

# \b --> back 表示退格，向前删除一位，输出 hellworld, 少了一个 o
print('hello\bworld')

# \ 单斜杠 表示转义，我们在输入 \\ 双斜杠时，第一位被转义，变成了单杠，所以使用时，要写双倍的斜杠，比如网址：
print('http:\\\\www.baidu.com')
print('良哥说：\'python\'')

# 原字符，我们不希望字符串中的转义字符起作用，就使用 原字符 r ，就是在字符串的前面加上 r 或者 R
