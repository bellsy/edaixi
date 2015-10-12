a = input("请输入:")
b = input("请输入:")
#c = input("请输入:")
d = input("请输入次数:")
n = 0
r = float(a)*float(b)
while n < int(d):
    r = float(a) * float(b)
    r = r**int(d)
    n = n + 1
print(len(str(r))-2)
    

