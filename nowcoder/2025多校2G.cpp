//https://ac.nowcoder.com/acm/contest/108299/G
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

const ld pi = acosl(-1), eps = 1e-16;

ll sgn(ld x) {
    if (abs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

typedef struct Point{
    ld x, y;
    Point(ld x = 0, ld y = 0) : x(x), y(y) {}
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }
    Point operator* (const ld& p) const {
        return Point(x * p, y * p);
    }
    ld operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    ld operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }
    bool operator== (const Point &p) const {
        return sgn(x - p.x) == 0 and sgn(y - p.y) == 0;
    }
    bool operator!= (const Point &p) const {
        return sgn(x - p.x) or sgn(y - p.y);
    }
} Vector;

inline ld angle(const Vector& a) {
    return atan2l(a.y, a.x);
}
// 极角 [0, 2π)
inline ld polarAngle(const Vector& a) {
    ld b = angle(a);
    if (b < 0) return 2 * pi + b;
    return b;
}
inline ld dist2(const Point& a, const Point& b) {
    return (b - a) * (b - a);
}
inline ld dist(const Point& a, const Point& b) {
    return sqrt(dist2(a, b));
}
inline ld dist2(const Vector& a) {
    return a * a;
}
inline ld dist(const Vector& a) {
    return sqrt(dist2(a));
}
// 无向角 [0, π]
inline ld angleBetween(const Vector& a, const Vector& b) {
    return atan2l(abs(a ^ b), a * b);
}
// 逆向角 [0, 2π)
inline ld angleTo(const Vector& a, const Vector& b) {
    ld c = atan2l(a ^ b, a * b);
    if (c < 0) return 2 * pi + c;
    return c;
}
// 判断点和直线的关系 1 左 0 重合 -1 右
inline ll orient(const Point& a, const Point& b, const Point& p) {
    return sgn((b - a) ^ (p - a));
}

void solve() {
    int n;
    ld x, y;
    cin >> n >> x >> y;
    Point O(x, y);
    vector<Point> Pol(n);
    for (int i = 0; i < n; ++i) {
        cin >> Pol[i].x >> Pol[i].y;
    }
    // 逆时针旋转，都在左侧，点在内部，只要有一个在右侧就一定在外部，用 AB × AP，逆时针（左侧）为正，顺时针（右侧）为负
    for (int i = 0; i < n; ++i) {
        if (orient(Pol[i], Pol[(i + 1) % n], O) == -1) {
            cout << 2 * pi << '\n';
            return;
        }
    }
    ld max_dist2 = 0;
    vector<Vector> md;
    for (int i = 0; i < n; ++i) {
        max_dist2 = max(max_dist2, dist2(Pol[i], O));
    }
    for (int i = 0; i < n; ++i) {
        if (dist2(Pol[i], O) == max_dist2) {
            md.emplace_back(Pol[i] - O);
        }
    }

    int m = md.size();
    if (md.size() < 2) {
        cout << 2 * pi << '\n';
        return;
    }
    ld res = 0;
    for (int i = 0; i < m; ++i) {
        res = max(res, angleTo(md[i],md[(i + 1) % m]));
    }
    cout << res << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    cout << fixed << setprecision(15);
    while (t--) solve();
    return 0;
}
