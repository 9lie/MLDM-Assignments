#ifndef KMEANS
#define KMEANS

double distance(const std::vector<double> &a, const std::vector<double> &b) {
    // 计算两个向量之间的欧式距离
    double sum = 0;
    for (int i = 0; i < a.size(); ++i) {
        sum += (a[i] - b[i]) * (a[i] - b[i]);
    }
    return std::sqrt(sum);
}

std::vector<std::vector<std::vector<double>>> kmeans(int d, int k, const std::vector<std::vector<double>> &points) {
    assert(k <= points.size());
    int count = 60; // 最大轮数
    std::vector<std::vector<double>> centers(k); // k个聚类中心
    std::vector<int> point_to(points.size()); // 记录每个点与哪个聚类中心最近，初始化为0

    std::vector<int> index(points.size());
    std::iota(index.begin(), index.end(), 0); // 初始化下标
    std::random_shuffle(index.begin(), index.end()); // 打乱数组，选前k个作为中心
    for (int i = 0; i < k; ++i) {
        centers[i] = points[index[i]];
    }

    while (count--) {
        // 根据当前的聚类中心分组
        for (int i = 0; i < points.size(); ++i) {
            for (int j = 0; j < k; ++j) {
                if (distance(points[i], centers[point_to[i]]) > distance(points[i], centers[j])) {
                    point_to[i] = j;
                }
            }
        }
        // 根据当前聚类分组计算新的聚类中心
        for (int i = 0; i < k; ++i) {
            centers[i].assign(d, 0);
            int cnt = 0; // 当前组有多少个点
            for (int j = 0; j < points.size(); ++j) {
                if (point_to[j] == i) {
                    ++cnt;
                    for (int p = 0; p < d; ++p) {
                        centers[i][p] += points[j][p];
                    }
                }
            }
            if (cnt > 0) {
                for (int j = 0; j < d; ++j) {
                    centers[i][j] /= cnt;
                }
            }
        }
    }

    std::vector<std::vector<std::vector<double>>> ret(k); // 结果
    for (int i = 0; i < k; ++i) {
        ret[i].emplace_back(centers[i]);
        for (int j = 0; j < points.size(); ++j) {
            if (point_to[j] == i) {
                ret[i].emplace_back(points[j]);
            }
        }
    }
    return ret;
}

#endif