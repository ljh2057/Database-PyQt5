from PyQt5 import QtWidgets,QtSql
from QtMainUI import Ui_Form
import sys
class MainWindow(QtWidgets.QMainWindow, Ui_Form):  # 组合继承
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton_query.clicked.connect(self.query_query)
        self.pushButton_first.clicked.connect(self.query_first)
        self.pushButton_last.clicked.connect(self.query_last)
        self.pushButton_pre.clicked.connect(self.query_pre)
        self.pushButton_next.clicked.connect(self.query_next)
        self.pushButton_delete.clicked.connect(self.query_delete)
        self.pushButton_insert.clicked.connect(self.query_insert)
        self.pushButton_modify.clicked.connect(self.query_insert)
        self.create_db()

    def create_db(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('webstore.sqlite')
            db.open()
            query = QtSql.QSqlQuery()
            # 创建一个数据库表
            query.exec_("create table products(ID int primary key, "
                        "pname varchar(20), brand varchar(20),price float(7,2),stock smallint)")
            query.exec_("insert into products values(101, '数码相机', '奥林巴斯',1330.00,3)")
            query.exec_("insert into products values(102, '平板电脑', '苹果',1999.00,5)")
            query.exec_("insert into products values(103, '笔记本电脑', 'Lenovo',4999.00,8)")
            query.exec_("insert into products values(104, '苹果手机', '苹果',5300.00,5)")
            query.exec_("insert into products values(105, '台式计算机', '戴尔',4500.00,10)")
            query.exec_("insert into products values(109, '3G手机', 'Samsung',3500.00,10)")
            print('创建数据库成功')
        except Exception as e:
            print(e)

    # 查询
    def query_query(self):
        sqlStr="select * from products where id="+self.lineEdit_id.text()
        self.updateInfo(sqlStr)

    # 第一条
    def query_first(self):
        sqlStr="SELECT * FROM products LIMIT 1"
        self.updateInfo(sqlStr)

    # 前一条
    def query_pre(self):
        curId=self.lineEdit_id.text()
        sqlStr="select * from products where id=(select max(id) from products where id< %s)"%(curId)
        self.updateInfo(sqlStr)

    # 后一条
    def query_next(self):
        curId=self.lineEdit_id.text()
        sqlStr="select * from products where id=(select min(id) from products where id> %s)"%(curId)
        self.updateInfo(sqlStr)

    # 最后一条
    def query_last(self):
        sqlStr="SELECT * FROM products ORDER BY id DESC LIMIT 1"
        self.updateInfo(sqlStr)

    # 删除
    def query_delete(self):
        sqlStr="delete FROM products WHERE id="+self.lineEdit_id.text()
        self.query = QtSql.QSqlQuery(sqlStr)
        QtWidgets.QMessageBox.about(self, '信息', '删除成功')

    # 插入
    def query_insert(self):
        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO products (id, pname, brand,price,stock) "
                      "VALUES (:id, :pname, :brand,:price,:stock)")
        query.bindValue(":id", self.lineEdit_id.text())
        query.bindValue(":pname", self.lineEdit_pname.text())
        query.bindValue(":brand", self.lineEdit_brand.text())
        query.bindValue(":price", self.lineEdit_price.text())
        query.bindValue(":stock", self.lineEdit_stock.text())
        query.exec_()
        QtWidgets.QMessageBox.about(self, '信息', '插入成功')

    # 修改
    def query_insert(self):
        curInfo=(self.lineEdit_pname.text(),self.lineEdit_brand.text(),self.lineEdit_price.text(),self.lineEdit_stock.text(),self.lineEdit_id.text())
        sqlStr="UPDATE products SET pname='%s', brand='%s',price=%s,stock=%s WHERE id=%s"%curInfo
        self.query = QtSql.QSqlQuery(sqlStr)
        QtWidgets.QMessageBox.about(self, '信息', '修改成功')


    def updateInfo(self, sqlStr):
        self.query = QtSql.QSqlQuery(sqlStr)
        if (self.query.next()):
            resList = [self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3),
                       self.query.value(4)]
            self.lineEdit_id.setText(str(resList[0]))
            self.lineEdit_pname.setText(resList[1])
            self.lineEdit_brand.setText(resList[2])
            self.lineEdit_price.setText(str(resList[3]))
            self.lineEdit_stock.setText(str(resList[4]))
            QtWidgets.QApplication.processEvents()
        else:
            QtWidgets.QMessageBox.about(self, '信息', '没有商品')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
