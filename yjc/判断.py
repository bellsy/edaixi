x = input("请输入数字:")
y = input("请再次输入数字")
a = int(x)
b = int(y)
if a + b > 10:
    print("加法:ok")
else:
    print("加法:no")
print("加法规则，结果大于10，ok")

if a - b > 3:
    print("减法:ok")
else:
    print("减法:no")
print("减法规则:结果大于3，ok")

if a * b > 15:
    print("乘法:ok")
else:
    print("乘法:no")
print("乘法规则:结果大于15，ok")

if a / b > 2:
    print("除法:ok")
else:
    print("除法:no")
print("除法规则:结果大于2，ok")
