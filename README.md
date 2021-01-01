# MLDM-Assignments

小组成员：卢鑫洌

实验任务文档地址：https://docs.qq.com/doc/DWXlEWVVZcG5CYWla

操作系统 windows 10

python 版本 3.7.1，需要额外安装 matplotlib

c++ 编译环境 gcc 9.2.0 使用c++17，编译命令 `g++ main.cpp -std=c++1z -m64 -o main.exe`

### 实验一、 多源数据集成、清洗和统计

合并两个数据源，去重并且去除一些部分信息缺失的数据

其中一个数据为 excel 文件，通过 excel 另存为 csv 文件

`Student` 类中包含了一个学生的基本信息

`unify_data(data)` 函数用于统一化数据的格式
- ID 统一为 202XXX
- 身高统一为 cm 作为单位
- 性别用 'male' 和 'female' 表示

`unique_data(data)` 函数用于合并 ID 重复的数据

- 具体的实现方法是通过对 ID 排序，那么 ID 相同的数据就会在相邻，然后比较去重合并

  如果两个ID相同的数据有某一项不同并且不为空，说明数据冲突，那么要将数据删除

  如果两个ID相同数据有一项为空，那么用另一个数据补充

`delete_useless_data(data)` 函数用于最后删除有空项的数据

其他几个计算函数是按照实验要求的公式实现的

最后将数据保存在 final.txt 中，并且输出一份 data.csv 和一份 data.txt 用于接下来的实验

其他细节在代码中有注释，本实验的所有代码在 assignment-1/main.py

### 实验二、 数据统计和可视化

本实验的所有画图通过 matplotlib 实现

散点图在 assignment-2/test1.py

直方图在 assignment-2/test2.py

其他在 assignment-2/main.py

结果输出再 assignment-2/out.txt

按公式实现即可

### 实验三、 k-means聚类算法

本实验的所有画图通过 matplotlib 实现

k-means 算法实现在 assignment-3/kmeans.h 中，代码有注释

assignment-3/main.cpp 会生成样例的聚类结果

代码最终会生成 'kmeansX.csv' 文件，表示设置为X类，聚类的结果是多少，每一个分组的第一个点表示聚类中心

最后通过 assignment-3/draw.py 画出散点图，结果已截图