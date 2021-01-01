#include <bits/stdc++.h>
#include "kmeans.h"

int main() {
    // 输入样例文件
    std::freopen("sample_data.txt", "r", stdin);
    std::vector<std::vector<double>> points;
    double x, y;
    while (std::cin >> x >> y) {
        std::vector<double> tmp;
        tmp.emplace_back(x);
        tmp.emplace_back(y);
        points.emplace_back(tmp);
    }
    for (int k = 2; k <= 5; ++k) {
        auto res = kmeans(2, k, points);
        std::freopen(("kmeans" + std::to_string(k) + ".txt").c_str(), "w", stdout);
        std::cout << k << std::endl;
        for (int i = 0; i < k; ++i) {
            std::cout << res[i].size() << std::endl;
            for (int j = 0; j < res[i].size(); ++j) {
                std::cout << res[i][j][0] << ' ' << res[i][j][1] << std::endl;
            }
        }
    }
}