# Database-PyQt5
# 基于 Python + PyQt5 的数据库操作练习

## 实验选题

第二题:  图形界面的实验项目

## 操作系统

Windows / Linux

## 开发环境

Python3、PyQt5、SQLite

## 程序源码

程序结构如下，主要分为三个文件 MainPageUI.py 、 QtMainUI.py 、 webstore.sqlite 。其中  MainPageUI.py 为主程序文件，对应相关增删改查功能的实现，QtMainUI.py 为页面布局文件，webstore.sqlite 为数据库文件。
├── MainPageUI.py
├── QtMainUI.py
└── webstore.sqlite
运行截图

### 主页面

![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592358609444-6111f7d3-e1e2-46da-b101-3a08e5473cfc.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=20520&status=done&style=none&width=600)

### 查询功能

查询功能根据商品号进行查询，下图展示了查询商品号为 103 的商品信息。
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592358731460-9a57732e-f240-4024-b6a0-76ba0cdff3d9.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=26603&status=done&style=none&width=600)

下图展示了所查询的商品号不存在的情况。
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592358918955-1c1ac842-ef8b-4ab5-bf5e-f80116a0d8e2.png#align=left&display=inline&height=424&margin=%5Bobject%20Object%5D&name=image.png&originHeight=424&originWidth=602&size=61379&status=done&style=none&width=602)

下图分别展示了查询第一条、前一条、后一条和最后一条的功能。
查询第一条结果:
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359023304-b6ab166e-e6fd-4574-997a-777e5c698cbc.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23671&status=done&style=none&width=600)

查询前一条结果（当前为 103 号商品）
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359174957-2ea28aa8-3249-4364-9196-c0a13ebb88f6.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23575&status=done&style=none&width=600)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359216324-870fe834-7b89-4f6b-8f43-ee5398084894.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23334&status=done&style=none&width=600)

查询后一条结果（当前为 103 号商品）
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359174957-2ea28aa8-3249-4364-9196-c0a13ebb88f6.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23575&status=done&style=none&width=600)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359257306-6830d07e-1b88-4f13-80d8-012a847e7d81.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23121&status=done&style=none&width=600)

查询最后一条结果
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359277841-ffc61982-0633-433d-8bc4-fb3d11291eec.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23504&status=done&style=none&width=600)

### 删除功能

下图展示了删除商品号为 101 的商品信息后数据库变动情况。
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359641664-d6bd34e5-73de-44e0-9257-67db672fb2cd.png#align=left&display=inline&height=420&margin=%5Bobject%20Object%5D&name=image.png&originHeight=420&originWidth=596&size=55920&status=done&style=none&width=596)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359766445-8d9892af-6149-4ba0-953f-faf728c1fbb2.png#align=left&display=inline&height=124&margin=%5Bobject%20Object%5D&name=image.png&originHeight=124&originWidth=329&size=11283&status=done&style=none&width=329)

### 插入功能

下图展示了手动输入商品号为 108 的商品信息后点击插入按钮的结果。
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359390217-0be068b1-9ffb-4f8c-9dc5-140a720daa40.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23135&status=done&style=none&width=600)

插入后点击查询 108 号可查看相应信息，为验证是否插入到数据库中，下图展示了插入后数据库信息。
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592359788597-43b3834f-aef6-4b23-a6e6-e498d20443cd.png#align=left&display=inline&height=146&margin=%5Bobject%20Object%5D&name=image.png&originHeight=146&originWidth=318&size=13403&status=done&style=none&width=318)

### 修改功能

下图展示了修改商品号 102 的商品品牌由苹果改为 Apple 后的结果。修改前：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592360006787-5cfab84b-b0df-46ed-86d5-0cc65960f6af.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23316&status=done&style=none&width=600)

修改后：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592360040562-7c784800-e2db-42e5-8252-afd5843d2d79.png#align=left&display=inline&height=422&margin=%5Bobject%20Object%5D&name=image.png&originHeight=422&originWidth=600&size=23368&status=done&style=none&width=600)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/537512/1592360057210-c5155899-dad1-4033-bb74-1a70acfcd24f.png#align=left&display=inline&height=139&margin=%5Bobject%20Object%5D&name=image.png&originHeight=139&originWidth=318&size=13359&status=done&style=none&width=318)
