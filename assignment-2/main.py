from matplotlib import pyplot
import csv, math, functools

# 读入数据
student_data = []
with open('data.csv') as f:
    file_csv = csv.reader(f)
    student_data = [list(map(float, v)) for v in file_csv]

# 计算平均数
def avg(l):
    return sum(l) / len(l)

# 计算协方差
def cov(l):
    sl, n = sum(l), len(l)
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

def zscore(A):
    m, s = avg(A), std(A)
    if s == 0:
        # 如果标准差为0，所有元素相等
        return [0 for _ in A]
    return [(x - m) / s for x in A]

# 矩阵转置
def rev(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

# 计算zscore归一化的数据矩阵
# 先转置，每门成绩zscore归一化，再转回来
zscore_mat = rev([zscore(l) for l in rev(student_data)])
# print(zscore_mat)

# 计算相关矩阵
correlation_mat = [[correlation(student_data[i], student_data[j]) for j in range(len(student_data))] for i in range(len(student_data))]
# print(correlation_mat)

# 可视化混淆矩阵
pyplot.matshow(correlation_mat, cmap=pyplot.cm.Blues) 
pyplot.colorbar()
pyplot.show()

# 根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔
# 相关性越大，距离越近 

# 通过自定义排序找到最大值的下标
index = [i for i in range(len(correlation_mat))]
with open('out.txt', 'w') as f:
    for l in correlation_mat:
        index.sort(key=functools.cmp_to_key(lambda x, y: l[y] - l[x]))
        f.write(f'{index[0]}\t{index[1]}\t{index[2]}\n')
