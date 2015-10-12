a = input("输入:")
b = input("输入:")
c = input("输入:")
d = input("输入:")
e = input("输入:")
f = input("输入:")
g = input("输入:")
x = input("计数数字:")
y = input("计算位置数字:")
z = input("位数:")
n = 0
group = [a,b,c,d,e,f,g]
print("有"+ str(group.count(x))+ "个" + str(x))
while n < 7:
    if y == group[int(n)]:
        print(str(y) + "在第" + str(n+1)+ "位")
    n = n + 1
    
print("第" + str(z) + "位是" + str(group[int(z)-1]))
