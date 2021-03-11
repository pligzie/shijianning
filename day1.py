id1 = 1
nam1 = "短袖"
price1 = 36
quanlity1 = "A+"
type1 = "上衣"
num1 = 500

id2 = 2
nam2 = "卫衣"
price2 = 70
quanlity2 = "B+"
type2 = "上衣"
num2 = 700

id3 = 3
nam3 = "牛仔裤"
price3 = 55
quanlity3 = "A+"
type3 = "裤子"
num3 = 400

id4 = 4
nam4 = "短裤"
price4 = 40
quanlity4 = "C+"
type4 = "裤子"
num4 = 300

print("---------------------------------------------")
print("-           欢迎来到jason衣服商城系统             -")
print("---------------------------------------------")
print("编号     名称     价格     品质     类型     销量")
print(id1,"     ",nam1,"   ",   price1 ,"     ",quanlity1,"    ",type1,"   ",num1,"    " )
print(id2,"     ",nam2,"   ",   price2 ,"     ",quanlity2,"    ",type2,"   ",num2,"    " )
print(id3,"     ",nam3,"  ",   price3 ,"     ",quanlity3,"    ",type3,"   ",num3,"    " )
print(id4,"     ",nam4,"   ",   price4 ,"     ",quanlity4,"    ",type4,"   ",num4,"    " )
print("总金额",(num1 * price1 + num2 * price2 + num3 * price3 + num4 * price4),"￥")