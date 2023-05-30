# Author：程序员良哥
# DateTime: 2023/2/28 20:02

# print() 函数的使用

# 可以输出数字
print(520)
print(99.9)

# 可以输出字符串， 单引号，双引号都可以
print('hello world')
print("hello world")

# 可以输出含有运算符的表达式
print(3 + 2)
print(3 * 7)

# 将数据输出到文件中
# 注意：使用 open 函数打开文件位置(*这个位置要真实存在，如果没有 E盘 就会出错); a+ 如果该文件不存在时就创建文件，如果该文件存在时，在文件内容的后面追加。自定义 addr 对象来接收地址信息
#      使用 print 函数，输出内容， * file= 指向文件的地址，一定要与上面我们自定义 addr 对象指代的地址保持一致
#      一定要记得关闭 addr 地址连接
addr = open("E:/PyOutput/demo.txt", 'a+')
print("hello world", file = addr)
addr.close()

# 不进行换行的输出(输出内容在一行当中)
print('hello', 'world', 'hello', 'python')
