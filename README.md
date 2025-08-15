# <center><font face="微软雅黑" font color=00a0c0 size=7>acm板子</font>
&nbsp;

---

树状数组

```cpp
#include <bits/stdc++.h>
using namespace std;
int i, j, ii, n, m, op, k, x, y, res, a[500005],t[500005],sum[500005];

inline int lowbit(int x) {
    return x & (-x);
}

int add(int x) {
    res = 0;
    for (ii = x; ii; ii -= lowbit(ii)) {
        res += t[ii];
    }
    return res;
}

// O(n)建树
void init() {
    for (i = 1; i <= n; ++i) {
        sum[i] = sum[i - 1] + a[i];
    }
    for (i = 1; i <= n; ++i) {
        t[i] = sum[i] - sum[i - lowbit(i)];
    }
}


int main() {
    cin >> n >> m;
    for (i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    init();
    for (i = 1; i <= m; ++i) {
        cin >> op;
        if (op == 1) {
            cin >> x >> k;
            for (j = x; j <= n; j += lowbit(j)) {
                t[j] += k;
            }
        }else {
            cin >> x >> y;
            cout << add(y) - add(x - 1) << '\n';
        }
    }
    return 0;
}
```

---
大数求逆元


```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long

string a1, b1;
const ll m = 19260817;
ll a,b,c,ans;
int k[19260820];

int main(){
    cin >> a1 >> b1;
    for(int i=0; i < a1.size(); i++) {
        a = ((a * 10) % m + a1[i] - '0') % m;
    }
    for(int i=0; i < b1.size(); ++i) {
        b = ((b * 10) % m + b1[i] - '0') % m;
    }
    if(b == 0){
        cout << "Angry!";
        return 0;
    }
    k[1] = 1;

    // O(n)求逆元，注意m(MOD)必须要是质数！

    for(int i=2; i<=b; ++i) {
        k[i] = (((-m / i + m) % m) * k[m % i] + m) % m;
    }
    ans = (a * k[b]) % m;
    cout << ans;
    return 0;
}
```
---
整除分块
```cpp
#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef long long ll;

signed main() {
    int n, k, l = 1, r;
    cin >> n >> k;
    int res = n * k;
    while(l <= n){
        ll t = k / l ;
        if(t == 0) break;
        r = min(k / t, n);
        res -= t * (r + l) * (r - l + 1) / 2 ;
        l = r + 1;
    }
    cout << res;
    return 0;
}
```
---

树状数组2
```cpp
#include <bits/stdc++.h>
using namespace std;
#define int long long

const int maxn = 5e5 + 20;
int n, m, i, ii, j, jj, res, op, x, y, k, a[maxn], t[maxn];

inline int lowbit(int x){
    return x&(-x);
}

void build() {
    for (i = 1; i <= n; ++i) {
        t[i] = a[i] - a[i - lowbit(i)];
    }
}

int sum(int x) {
    res = 0;
    for (ii = x; ii; ii -= lowbit(ii)) {
        res += t[ii];
    }
    return res;
}

void add(int x, int k) {
    for (jj = x; jj <= n; jj += lowbit(jj)) {
        t[jj] += k;
    }
}

signed main() {
    cin >> n >> m;
    for (i = 1; i <= n; ++i) cin >> a[i];
    
    build();

    for (i = 1; i <= m; ++i) {
        cin >> op;
        if (op == 1) {
            cin >> x >> y >> k;
            add(x, k);
            add(y + 1, -k);
        }else {
            cin >> x;
            cout << sum(x) << '\n';
        }
    }
    return 0;
}
```

---

任意数的逆元

python
```py
a, b = map(int, input().split())
print(pow(a, -1, b))
```
&nbsp;
c++
```cpp
#include <iostream>
using namespace std;

int modinv(int a, int b) {
    int b0 = b, t, q;
    int x0 = 0, x1 = 1;
    
    if (b == 1) return 0;

    while (a > 1) {
        q = a / b;
        t = b;
        b = a % b;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0) x1 += b0;
    if (a == 1) return x1;
    else return -1;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << modinv(a, b);
    return 0;
}
```

---
扩展欧拉定理解决字符串指数快速幂

```cpp
#include<bits/stdc++.h>
using namespace std;
int phi(int x)//欧拉函数
{
	int ans=1,num=1;
	for(int i=2;i*i<=x;i++)
	{
		if(!(x%i))
		{
			num=i-1,x/=i;
			while(!(x%i)) num=num*i,x/=i;
			ans=num*ans;
		}
	}
	if(x!=1) ans=ans*(x-1);
	return ans;
}
inline int read(int mod)//改进快读，让他边读边输入
{
	//g用来判断b与phi(m)的大小，如果小于，就不能加了，这是坑点！
	int x=0;
	bool g=false;
	char c=getchar();
	while(c<'0'||c>'9') c=getchar();
	while(c>='0'&&c<='9')
	{
		x=(x<<3)+(x<<1)+(c^'0');
		if(x>=mod) x%=mod,g=true;
		c=getchar();
	}
	if(g) return (x+mod);
	else return x;
}
int a,mod;
char b[20000005];
inline int quickpow(int a,int b)//快速幂
{
	long long ans=1,base=(long long)a;
	while(b)
	{
		if(b&1) ans=ans*base%mod;
		b>>=1;
		base=base*base%mod;
	}
	return (int)(ans%mod);
}
int p;
int main() {
	scanf("%d%d",&a,&mod);
	int p=phi(mod);
	int cishu=read(p);//得出的化简次数
	int s=quickpow(a,cishu);
	printf("%d\n",s);
	return 0;
}
```
---
BFS

```cpp
int main() {
    cin >> n;
    for(int i = 1; i <= n - 1; ++i) {
        cin >> u >> r;
        G[u].push_back(r);
        G[r].push_back(u);
    }
    dfs(1, 0);
    q.push(ans);
    while(!q.empty()) {  //标准BFS
        int e = q.front();
        q.pop();
        vis[e] = true;
        sum += dis[e];
        for(int i = 0; i < G[e].size(); ++i){
            if(!vis[G[e][i]]){
                q.push(G[e][i]);
                dis[G[e][i]] = dis[e] + 1;
            }
        }
    }
    cout << ans << sum;  //完美输出
    return 0;
}
```

---
双指针求子串模板
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, i, j, cnt[26];
string s;

bool check() {
    for (int i = 0; 3 < 26; ++i) {
        if (!cnt[i])3return false;
    }
    return true;
}

int main() {
    cin >> s;
    n = s.size();
    int res = 0x3f3f3f3f;
    
    // 初始化左右指针
    i = 0, j = 0;
    
    // 扩展窗口直到包含所有字符
    while (j < n) {
        cnt[s[j] - 'a']++;
        j++;
        
        // 当窗口包含所有字符时，尝试收缩左边界
        while (check() && i < j) {
            // 更新最小长度
            res = min(res, j - i);
            
            // 收缩左边界
            cnt[s[i] - 'a']--;
            i++;
        }
    }
    
    cout << res;
    return 0;
}

```

---
反悔贪心（实际上就是堆）
```cpp
#include<bits/stdc++.h>
using namespace std;

int n, v, s;
long long ans, sum;
vector<long long> a[100010];
priority_queue<long long, vector<long long>, greater<>> q;  // 维护当前最大的i个战力

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> v >> s;
        a[s].emplace_back(v);  // 按s值分组存储战力
    }
    for (int i = n; i >= 1; --i) {
        //这个地方很好，此时遍历到s=i时实际上已经处理过了s>=i的情况
        for (auto u : a[i]) {
            q.emplace(u);
            sum += u;
        }
        // 维护堆大小不超过i（只保留最大的i个战力）
        while (q.size() > i) {
            sum -= q.top();
            q.pop(); 
        }
        ans = max(ans, sum);
    }
    
    cout << ans;
    return 0;
}
```

---
可以分解为2个素数的乘积的数
```cpp
#include <bits/stdc++.h>
using namespace std;
const int N=1e8+10;
int b[N],a[N],c,st[N],t,l,r,i=2,j;

void init(){
  for(;i<=1e8;i++){
    if(!st[i]) b[c++]=i;  // 若i是素数，加入素数数组b
    a[i] = a[i-1]+(st[i] == 1);  // 统计前i个数中半素数的数量
    
    // 欧拉筛法变种，标记合数
    for(int j = 0; b[j] <= 1e8 / i; ++j){
      st[i*b[j]]=st[i]+1;  // 关键：st值表示素因子分解的"步数"
      if(i%b[j]==0)break;  // 保证每个合数只被最小素因子筛除
    }
  }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    init();
    cin >> t;
    for(i=0;i<t;++i) {
        cin >> l >> r;
        cout << a[r] - a[l - 1] << '\n';
    }
    return 0;
}
```

---
纸币问题3（组合数量）
```cpp
#include<bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;
const int W = 1e4 + 5;
const int inf = 2e9;
const int mod = 1e9 + 7;
int n,w;
int a[N];
int f[W];

int main() {
	cin>>n>>w;
	for(int i = 1; i<=n; i++) {
		cin>>a[i];
	}
	f[0] = 1; //边界
	for(int i = 1; i<=n;i++) {
		for(int j = a[i]; j<=w; j++) {
			f[j] += f[j - a[i]] % mod;
			f[j] %= mod;
		}
	}
	cout<<f[w]<<endl;
	return 0;
}
```


pbds解决中位数问题
```cpp
#include <bits/extc++.h>
using namespace std;
#define int long long
#define ll long long
template<typename T>
using ordered_multiset = __gnu_pbds::tree<
    std::pair<T, int>,
    __gnu_pbds::null_type,
    std::less<std::pair<T, int>>,
    __gnu_pbds::rb_tree_tag,
    __gnu_pbds::tree_order_statistics_node_update
>;


signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t --) {
        int n, q;
        std::cin >> n >> q;
        std::vector<ll> nums(n);
        ordered_multiset<ll> ost;

        for (int i = 0; i < n; ++i) {
            std::cin >> nums[i];
            ost.insert({nums[i], i});
        }

        int min_loss = ceil((n - 1) / 2.0);

        for (int i = 0; i < q; ++i) {
            int p, v;
            cin >> p >> v;
            p--;
            ost.erase({nums[p], p});

            nums[p] += v;

            ost.insert({nums[p], p});

            int pivot = ost.find_by_order(n - min_loss) -> first;
            int numb = ost.order_of_key({pivot, -1});
            if (ost.size() - ost.order_of_key({pivot, n + 1}) >= min_loss) {
                int cnt = ost.order_of_key({pivot, n + 1}) - ost.order_of_key({pivot, -1});
                numb += cnt;
            }
            cout << numb << '\n';
        }
    }

    return 0;
}
```


```python
for _ in range(int(input())):
    a, b = map(int, input().split())
    d = abs(a * a - b * b)
    print(d - ((d > 1) + (d > 4) + (d + 1) // 4))
```

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector f(2 * n + 1, 2 * n + 1);  // f[i] 表示从 i 开始约束区间 i -> f[i]
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        l--;  // 0-index
        f[l] = min(f[l], r);  // 从 r 开始才放下一个 '('
    }
    vector<int> dp(2 * n + 1);  // dp[i] 是从位置 i 开始，保障的左括号的数量，基于贪心从右向左更新
    for (int i = 2 * n - 1; i; --i) {
        f[i] = min(f[i], f[i + 1]);  // 最小值前缀，表示从 i 开始最小区间右端点的 index
        if (f[i] > 2 * n) {
            dp[i] = 0;
        } else {
            dp[i] = 1 + dp[f[i]];  // 从 i 开始最少要放'('的数量
        }
    }
    if (dp[0] > n) {
        cout << -1 << '\n';
        return;
    }
    string s;
    int cnt = n;
    for (int i = 0; i < 2 * n; ++i) {
        if (dp[i + 1] < cnt) {  // 之后的问题，提前放左括号
            s += '(';
            cnt--;
        } else {
            s += ')';
        }
    }
    int b = 0;
    for (auto c : s) {
        if (c == '(') {
            b++;
        } else {
            b--;
        }
        if (b < 0) {
            cout << -1 << '\n';
            return;
        }
    }
    cout << s << '\n';
}


int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
```

pbds板子

```cpp
#include <bits/extc++.h>
using namespace std;
__gnu_pbds::gp_hash_table<string, int> mp;

// 建议比赛使用 map 或 __gnu_pbds::gp_hash_table

int main() {
    int t, op, score;
    string name;
    cin >> t;
    while (t--) {
        cin >> op;
        if (op == 1) {
            cin >> name >> score;
            mp[name] = score;
            cout << "OK\n";
        } else if (op == 2) {
            cin >> name;
            if (mp.find(name) != mp.end()) {  // 不支持 count
                cout << mp[name] << '\n';
            } else {
                cout << "Not found\n";
            }
        } else if (op == 3) {
            cin >> name;
            if (mp.find(name) != mp.end()) {
                mp.erase(name);
                cout << "Deleted successfully\n";
            } else {
                cout << "Not found\n";
            }
        } else {
            cout << mp.size() << '\n';
        }
    }
    return 0;
}
```

计算几何模板版
```cpp
template<typename T>
struct Point {
    T x, y;
    Point(T x_ = 0, T y_ = 0) : x(x_), y(y_) {}
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }
    Point operator*(const T& p) const {
        return Point(x * p, y * p);
    }
    T operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    T operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }
};

template<typename T>
using Vector = Point<T>;

```

计算几何 - 角度
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

const ld pi = acosl(-1), eps = 1e-7;

ll sgn(ld x) {
    if (abs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

template<class T>
struct Point {
    T x, y;
    Point(T x_ = 0, T y_ = 0) : x(x_), y(y_) {}
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }
    Point operator*(const T& p) const {
        return Point(x * p, y * p);
    }
    T operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    T operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }
    bool operator==(const Point& p) const {
        return sgn(x - p.x) == 0 && sgn(y - p.y) == 0;
    }
    bool operator!=(const Point& p) const {
        return sgn(x - p.x) != 0 || sgn(y - p.y) != 0;
    }
};

using Vector = Point;

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
```
计算几何 - 角度
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

const ld pi = acosl(-1);

struct Point {
    ll x, y;
    Point(ll x = 0, ll y = 0) : x(x), y(y) {}
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }
    Point operator* (const ll& p) const {
        return Point(x * p, y * p);
    }
    ld operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    ld operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }
};
using Vector = Point;

int main() {
    int n;
    cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i].x >> p[i].y;
    }
    vector<Vector> vec;
    for (int i = 1; i < n; ++i) {
        vec.push_back(p[i] - p[0]);
    }
    ld res = 0;
    for (int i = 0; i < n - 2; ++i) {
        res += (vec[i] ^ vec[i + 1]) / 2;
    }
    ll round_res = abs(res) + 0.5;
    cout << round_res;
    return 0;
}
/*
也能过
for (int i = 0; i < n; ++i) {
    res += (p[i] ^ p[(i + 1) % n]) / 2;
}
*/
```
计算几何 - 旋转方向
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

const ld pi = acosl(-1);

struct Point{
    ll x, y;
    Point(ll x = 0, ll y = 0) : x(x), y(y) {}
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    Point operator-(const Point& p) const {
        return Point(x - p.x, y - p.y);
    }
    Point operator* (const ll& p) const {
        return Point(x * p, y * p);
    }
    ll operator*(const Point& p) const {
        return x * p.x + y * p.y;
    }
    ll operator^(const Point& p) const {
        return x * p.y - y * p.x;
    }
};
using Vector = Point;

// 此题可能是凹多边形，计算面积正负即可

int main() {
    int n;
    cin >> n;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i].x >> p[i].y;
    }
    ll res = 0;
    for (int i = 0; i < n; ++i) {
        res += p[i] ^ p[(i + 1) % n];
    }
    if (res > 0) cout << "counter";
    cout << "clockwise";
    return 0;
}
/*
用原点向量则需要取模 (i + 1) % n
for (int i = 1; i < n - 1; ++i) {
    res += (p[i] - p[0]) ^ (p[i + 1] - p[0]);
}
*/
```
出栈序列最大字典序
```python
n = int(input())
a = list(map(int,input().split()))
stack = []
b = [0] * n
tmp = 0
for i in range(n - 1, -1, -1):
    tmp = max(a[i], tmp)
    b[i] = tmp
for i in range(n):
    if b[i] == a[i]:
        print(a[i], end = " ")
    else:    
        stack.append(a[i])
print(*stack[::-1])
```
配对 枚举
```cpp
#include <bits/stdc++.h>
using namespace std;
int n, tmp, cnt[10005], ans;
int main() {
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> tmp;
        cnt[tmp] ++;
    }
    for (int k = 2; k <= 10000; ++k) {
        int r = 0;
        for (int i = 1; i <= k - i; ++i) {
            int t;
            if (i == k - i) {
                t = cnt[i] / 2;
            } else {
                t = min(cnt[i], cnt[k - i]);
            }
            r += t << 1;
        }
        ans = max(ans, r);
    }
    cout << ans;
    return 0;
}
```

矩阵快速幂
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
typedef vector<vector<ll>> mat;
constexpr ll mod = 1e9 + 7;

mat operator*(const mat& a, const mat& b) {
    mat res(2, vector<ll>(2));
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 2; ++k) {
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % mod;
            }
        }
    }
    return res;
}

mat operator^(mat a, ll b) {
    mat res = {{1, 0}, {0, 1}};
    while (b) {
        if (b & 1) {
            res = res * a;
        }
        a = a * a;
        b >>= 1;
    }
    return res;
}

void solve() {
    ll x, y, a, b, n;
    cin >> x >> y >> a >> b >> n;
    
    if (n == 0) {
        cout << x % mod << '\n';
        return;
    }
    if (n == 1) {
        cout << y % mod << '\n';
        return;
    }
    
    mat trans = {{a, b}, {1, 0}};
    mat power = trans ^ (n - 1);
    mat init = {{y}, {x}};
    mat res = power * init;
    
    cout << res[0][0] % mod << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```
