//https://ac.nowcoder.com/acm/contest/108299/G
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

const ld pi = acos(-1);

struct Point{
    ll x, y;
    Point operator+(const Point& p) const {
        return {x + p.x, y + p.y};
    }
    Point operator-(const Point& p) const {
        return {x - p.x, y - p.y};
    }
    ll operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    ll operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }

};

using Vector = Point;

ld angle(const Vector& a) {
    return atan2l(a.y, a.x);
}

ll dist2(const Point& a, Point& b) {
    return (b - a) * (b - a);
}

ll dist2(const Vector& a) {
    return a * a;
}

// 无向角
ld angleBetween(const Vector& a, const Vector& b) {
    return atan2l(abs(a ^ b), a * b);
}

// 有向角
ld angleTo(const Vector& a, const Vector& b) {
    ld c = atan2l(a ^ b, a * b);
    if (c < 0) return 2 * pi + c;
    else return c;
}

void solve() {
    int n, x, y;
    cin >> n >> x >> y;
    Point O = {x, y};
    vector<Point> Pol(n);
    for (int i = 0; i < n; ++i) {
        cin >> Pol[i].x >> Pol[i].y;
    }
    // 逆时针旋转，都在左侧，点在内部，只要有一个在右侧就一定在外部，用 AB × AP，逆时针（左侧）为正，顺时针（右侧）为负
    for (int i = 0; i < n; ++i) {
        Vector a = Pol[(i + 1) % n] - Pol[i];
        Vector b = O - Pol[i];
        if ((a ^ b) < 0) {
            cout << 2 * pi << '\n';
            return;
        }
    }
    ll max_dist2 = 0;
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
