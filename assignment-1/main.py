import csv, math

'''
一共两个数据源
data1.csv 通过excel另存得到
data2.txt
'''

data_student = []
city_list = ['Beijing', 'Guangzhou', 'Shenzhen', 'Shanghai']
constitution_list = ['bad', 'general', 'good', 'excellent']

# 计算平均数
def avg(l):
    if l == []:
        return 0
    return sum(l) / len(l)

# 计算协方差
def cov(l):
    sl, n = sum(l), len(l)
    if n == 1 or n == 0:
        return 0
    return (sum([x * x for x in l]) - sl * sl / n) / (n - 1)

# 计算标准差
def std(l):
    return math.sqrt(cov(l))

# 计算相关性
def correlation(A, B):
    def sol(l):
        al, sl = avg(l), std(l)
        return [(x - al) / sl for x in l]
    return sum([x * y for x, y in zip(sol(A), sol(B))])

'''
需要处理的数据有：
空缺的数据补全
身高转换成cm
Gender改成male和female
体测成绩用分数表示，最高4分
'''

class Student:
    def __init__(self, ID, name, city, gender, height, constitution, data):
        self.ID = ID

        self.name = name
        self.city = city
        self.gender = gender
        self.height = float(height) if height != '' else 0

        # 体测成绩用分数表示，最高4分
        self.constitution = constitution_list.index(constitution) + 1 if constitution != '' else 0

        self.data = [float(x) if x != '' else 0 for x in data] # 如果是空缺，为0

    def sum(self):
        return sum(self.data)

    def avg(self):
        return self.sum() / len(self.data)

    def print(self):
        print(self.ID, self.name, self.city, self.gender)

# 统一数据格式
def unify_data(data):
    # 统一ID
    if data[0] != '' and len(data[0]) <= 3:
        data[0] = str(int(data[0]) + 202000)
    # 统一性别格式
    if data[3] == 'boy':
        data[3] = 'male'
    elif data[3] == 'girl':
        data[3] = 'female'
    elif data[3] != 'male' and data[3] != 'female':
        data[3] = ''
    # 统一身高单位
    if data[4] != '' and float(data[4]) < 3:
        data[4] = str(int(float(data[4]) * 100))
        # 这里需要转int再转str，不然比较的时候会因为多.0丢失一些数据
    return data

# 数据去重
def unique_data(data):
    # 先统一化数据
    data = [unify_data(x) for x in data]
    # 去重，ID 相同的数据可能冲突，要处理
    data.sort(key=lambda x: int(x[0]))
    p = 0
    while p < len(data):
        while p + 1 < len(data) and data[p + 1][0] == data[p][0]:
            for i in range(len(data[p])):
                if data[p][i] == data[p + 1][i]:
                    continue
                if data[p][i] != '' and data[p + 1][i] != '':
                    data[p][i] = ''
                    data[p + 1][i] = ''
                elif data[p][i] != '':
                    data[p + 1][i] = data[p][i]
            data[p][0] = ''
            p += 1
        p += 1

    # 把重复项的第一项赋值为空字符串，排序后会到数组的最前面，
    # 删除无用项
    data.sort(key=lambda x: x[0])
    while len(data) > 0 and data[0][0] == '':
        data = data[1:]
    # print([x[0] for x in data])
    return data

# 删除有空项目的数据
def delete_useless_data(data):
    def check(x):
        for i in range(len(x)):
            if x[i] == '' and i != len(x) - 2:
                return False
        return True
    return [x for x in data if check(x)]

data1, data2 = [], []

# 读入数据源1
with open('data1.csv', 'r', encoding='utf-8') as file:
    data1 = list(csv.reader(file))
    data1 = data1[1:] # 去除第一行的头
    data1 = unique_data(data1)

# 读入数据源2
with open('data2.txt', 'r', encoding='utf-8') as file:
    data2 = list(csv.reader(file))
    data2 = data2[1:] # 去除第一行的头
    data2 = unique_data(data2)


# 合并两个数据源并去重
data = delete_useless_data(unique_data(data1 + data2))
data_student = [Student(x[0], x[1], x[2], x[3], x[4], x[-1], x[5:-2]) for x in data]

# 1. 学生中家乡在Beijing的所有课程的平均成绩。

for i in range(9):
    tmp = []
    for student in data_student:
        if student.city == 'Beijing':
            tmp.append(student.data[i])
    print(f'C{i + 1}的平均成绩为{avg(tmp)}\n')

# 2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。

cnt = 0
for student in data_student:
    if student.city == 'Guangzhou' and student.data[0] > 80 and student.data[8] > 9 and student.gender == 'male':
        student.print()
        cnt += 1
print(f'学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量:{cnt}\n')


# 3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？

Guangzhou_constitution = []
Shanghai_constitution = []
for student in data_student:
    if student.city == 'Guangzhou' and student.gender == 'female':
        Guangzhou_constitution.append(student.constitution)
    if student.city == 'Shanghai' and student.gender == 'female':
        Shanghai_constitution.append(student.constitution)
print('广州和上海两地女生的平均体能测试成绩，哪个地区的更强些：', end='')
if avg(Guangzhou_constitution) < avg(Shanghai_constitution):
    print('上海')
elif avg(Guangzhou_constitution) > avg(Shanghai_constitution):
    print('广州')
else:
    print('相等')

print()

# 4. 学习成绩和体能测试成绩，两者的相关性是多少？

constitutions = [student.constitution for student in data_student]
for i in range(9):
    course = [student.data[i] for student in data_student]
    print(f' c{i + 1}成绩 与 体测成绩 的相关性: {correlation(course, constitutions)}\n')

# 保存文件

with open('final.txt', 'w') as f:
    for student in data_student:
        f.write(student.ID + '\t' + student.name + '\t\t' + student.city + '\t\t' + student.gender + '\t' + str(student.height) + ',')
        for v in student.data:
            f.write(str(v) + '\t')
        f.write(str(student.constitution) + '\n')

with open('data.csv', 'w') as f:
    for student in data_student:
        for v in student.data:
            f.write(str(v) + ',')
        f.write(str(student.constitution) + '\n')

with open('data.txt', 'w') as f:
    for student in data_student:
        for v in student.data:
            f.write(str(v) + ' ')
        f.write(str(student.constitution) + '\n')