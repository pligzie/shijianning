from DBUtils import select
from DBUtils import update
class Bank:
    bankName = "中国工商银行账户管理系统"

    def  bank_AddUser(self,user):
        # 判断数据库是否已满
        sql1 = "select  count(*)  from user"
        data = select(sql1, [])
        if data[0][0] >= 100:  # 如果返回的统计数据超出100，则已满
            return 3
        # 判断数据是否存在改用户
        # 获取所有键，然后在判断是否有
        sql2 = "select * from user  where  account = %s"
        param2 = [user.getAccount()]
        data2 = select(sql2, param2)
        if len(data2) != 0:  # 如果通过sql语句能查到数据并且不为空，则说明改用户已存在
            return 2
        # 正常开户：insert into 表  ，否则则执行存储数据操作
        sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"  # now() 使用的mysql数据库自己的时间
        param3 = [user.getAccount(),
                  user.getUsername(),
                  user.getPassword(),
                  user.getAddress().getCountry(),
                  user.getAddress().getProvince(),
                  user.getAddress().getStreet(),
                  user.getAddress().getDoor(),
                  user.getMoney(),
                  self.bankName]
        update(sql3, param3)
        return 1
    def bank_savemoney(self):
        account=input("请输入账号")
        password=input("请输入密码")
        sql="select money from user where account = %s"
        date=select(sql,account)
        if date != sql:
            print("输入错误")
        else:
            print("账户余额为",date[0][0])
            money=input("请输入您存款的余额：")
            sql="update user set money = money + %s"
            update(sql,money)
            sql="select money from user where account=%s"
            date=select(sql,account)
            print("date[0][0]")






































