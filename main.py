# 实现输入10个数字，并打印10个数的求和结果
# a = 0
# sum = 0
#
# while a < 10:
#     c = int(input("请输入数字："))
#     sum = sum + c
#     a+= 1
# print ("请输入数字：",sum)


# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# a = 0
# sum = 0
# c = 0
# big = 0
# b = 0
#
#
# while a < 10:
#     c = int(input("请输入数字："))
#     sum = sum + c
#     a+= 1
#     b = sum / a
#     if c > big:
#         big = c
# print ("数字的合：",sum)
# print ("数字的平均值：",b)
# print ("数字的最大值：",big)

# 使用random模块，如何产生 50~150之间的数？
# import random
# num = random.randint(50,150)
# print(num)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a =  int(input("请输入第一条边："))
# b =  int(input("请输入第二条边："))
# c =  int(input("请输入第三条边："))
#
# if a <= 0 or b <= 0 or c <= 0:
#     print("不能形成三角形")
# elif a + b > c or a + c > b or b + c > a:
#     print("普通三角形")
# elif a == b == c:
#     print("等边三角形")
# elif a == b or b == c or a == c:
#     print("等腰三角形")
# elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
#     print("直角三角形")

# # 有以下两个数，使用+，-号实现两个数的调换。
# a = 56
# b = 78
# print("a=",a+22)
# print("b=",b-22)



# # 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# username = "root"
# password = "admin"
# c = 0
# q=0
# while c < 3:
#     c = c + 1
#     a = input("请输入用户名：")
#     b = input("请输入密码：")
#     if a == username and b == password:
#         print("登录成功")
#         break
#
#     else:
#         if q==2:
#             print("锁定")
#         else:
#             print("请重新输入：")
#             q += 1
#
#
# 编程实现下列图形的打印
# for i in range(8):
#     for j in range(0, 10 - i):
#         print(end=" ")
#     for k in range(10 - i, 10):
#         print("*", end=" ")
#     print("")


# 使用while循环实现99乘法表的打印。
# a = 1
# b = 1
#
# while a <= 9:
#     while b <= 9:
#         print(a,"*",b,"=",a*b)
#         b+=1
#     b=1
#     a+=1

# 编程实现99乘法表的倒叙打印
# a = 9
# b = 9
#
# while a >= 1:
#     while b >= 1:
#         print(a,"*",b,"=",a*b)
#         b-=1
#     b=1
#     a-=1

# # 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# day = 0
# high = 0
# w = 3
# n = 2
# while True:
#     day = day+1
#     high = day+w
#     if high == 20:
#         print("最终天数:",day)
#         break
#     high = high - n
#     print("最终高度：",high)


# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能。
# a=0
# import random
# import time
# rannum = random.randint(1,5)
# while a<=3:
#     a+=1
#     num = input("请输入您要猜的数字：")
#     num = int(num)
#     if num > rannum:
#         print("大了！")
#     elif num < rannum:
#         print("小了！")
#     else:
#         if a<3:
#             a+=1
#             print("恭喜猜对了，奖励2000金币 数字为：",rannum)
#             break
#         else:
#             print("系统已锁定")
#             while 1:
#                 time.sleep(1)
#

# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# a=1
# b=1
# c=0
# while a<20:
#     while b<=a:
#         print(a," ",b)
#         c=c+(a*b)
#         b+=1
#     b=1
#     a+=1
# print(c)
