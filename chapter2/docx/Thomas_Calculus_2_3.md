## 2.3 极限的精确定义

现在我们转向极限的精确定义。微积分早期历史中，关于基本概念的有效性存在大量争论，数学家和哲学家们对诸多表面矛盾争论不休。精确定义的建立解决了这些争议——它将非正式定义中"任意接近"等模糊措辞替换为可以应用于任何具体例子的明确条件。有了严格定义，我们便能避免误解、证明上一节的极限性质，并建立许多重要的极限。

要证明 $f(x)$ 在 $x \to c$ 时的极限等于 $L$，就需要证明：只要 $x$ 保持"足够接近"$c$，$f(x)$ 与 $L$ 之间的差距就可以变得"任意小"。

**例1** 考察函数 $y = 2x - 1$ 在 $x = 4$ 附近的行为。直觉上，当 $x$ 接近4时 $y$ 接近7，因此 $\displaystyle\lim_{x\to 4}(2x-1) = 7$。但 $x$ 距离4有多近，才能保证 $y = 2x-1$ 与7相差不超过2？

**解** 问题转化为：对哪些 $x$ 有 $|y - 7| < 2$？

$$|y - 7| = |(2x-1) - 7| = |2x - 8|.$$

解不等式 $|2x - 8| < 2$：

$$|2x - 8| < 2$$
$$-2 < 2x - 8 < 2 \quad \text{（去绝对值得两个不等式）}$$
$$6 < 2x < 10 \quad \text{（各项加8）}$$
$$3 < x < 5 \quad \text{（解出 }x\text{）}$$
$$-1 < x - 4 < 1. \quad \text{（解出 }x-4\text{）}$$

即：将 $x$ 限制在距4不超过1的范围内，就能保证 $y$ 与7相差不超过2。

> **图2.15示意**
>
> 坐标系中画有直线 $y=2x-1$。纵轴上标出上界 $y=9$ 和下界 $y=5$（即以7为中心、宽度为2的区间），横轴上标出 $x=3$ 和 $x=5$（即以4为中心、宽度为1的区间）。箭头标注"限制在此范围"（横轴）与"满足此条件"（纵轴），直观说明 $x$ 在1以内时 $y$ 在2以内的对应关系。

为描述任意给定的误差，引入两个正数 $\delta$（delta）和 $\varepsilon$（epsilon）。这两个希腊字母传统上用于表示变量或函数的微小变化量。

---

### 极限的定义

假设我们观察 $x$ 趋近于 $c$（但不取 $c$ 本身）时函数 $f(x)$ 的值。我们希望能够说：只要 $x$ 落在 $c$ 的某个 $\delta$ 邻域内，$f(x)$ 就保持在 $L$ 的 $\varepsilon$ 邻域内。但仅此一个 $\varepsilon$ 还不够——随着 $x$ 继续趋近 $c$，$f(x)$ 可能在 $L$ 的邻域内跳动而不趋向 $L$。

我们可以被告知误差不超过 $1/100$、$1/1000$、$1/100000$……每次都找到一个新的 $\delta$ 区间，使 $x$ 在该区间内时满足新的误差要求。这个过程可以想象成一场"挑战与应答"：

> **图2.16–2.17示意（挑战与应答过程）**
>
> 一系列成对的坐标系（共8幅），交替展示"挑战"与"应答"：
> - 第1对：挑战 $\varepsilon = 1/10$，应答给出 $\delta_{1/10}$；
> - 第2对：挑战 $\varepsilon = 1/100$，应答给出 $\delta_{1/100}$；
> - 第3对：挑战 $\varepsilon = 1/1000$，应答给出 $\delta_{1/1000}$；
> - 第4对：挑战 $\varepsilon = 1/100000$，应答给出 $\delta_{1/100000}$；
> - 最后一幅：挑战 $\varepsilon = \cdots$（任意小），表明对任意挑战都能给出应答。
>
> 每幅图中，函数 $y=f(x)$ 的图像穿过点 $(c, L)$，纵轴上标出 $L \pm \varepsilon$ 的水平带，横轴上标出以 $c$ 为中心的 $\delta$ 区间，说明在该 $\delta$ 区间内函数值落在 $\varepsilon$ 带内。

终止这一无限"挑战–应答"的方法是：证明对挑战者给出的**每一个** $\varepsilon > 0$，都能找到匹配的 $\delta > 0$，使得 $x$ 在 $c$ 的 $\delta$ 邻域内时，$f(x)$ 落在 $L$ 的 $\varepsilon$ 邻域内（图2.17）。这引导我们给出极限的精确定义。

---

> **定义** 设 $f(x)$ 在 $c$ 的某个开区间上有定义（$c$ 点本身可能除外）。若对每个数 $\varepsilon > 0$，都存在对应的数 $\delta > 0$，使得
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad 0 < |x - c| < \delta,$$
>
> 则称 $f(x)$ 在 $x$ 趋近于 $c$ 时的**极限为 $L$**，记作
>
> $$\lim_{x \to c} f(x) = L.$$

---

为直观理解这个定义，可以想象将一根圆柱轴加工至精密公差：$x$ 是拨盘设置值，我们希望直径为 $L$，但因误差只能接受直径 $f(x)$ 落在 $[L-\varepsilon, L+\varepsilon]$ 内。$\delta$ 是拨盘的控制公差——它告诉我们拨盘设置距理想值 $x=c$ 有多近，才能保证直径误差在 $\varepsilon$ 以内。误差要求越严格，$\delta$ 可能需要调得越小。

> **图2.17示意**
>
> 坐标系中展示 $\delta$ 与 $\varepsilon$ 的关系：纵轴上标出 $L$、$L+\varepsilon$、$L-\varepsilon$，横轴上标出 $c-\delta$、$c$、$c+\delta$。函数 $y=f(x)$ 的图像在 $x\in(c-\delta,\, c+\delta)$ 且 $x\neq c$ 时，函数值落在 $(L-\varepsilon,\, L+\varepsilon)$ 内。

---

### 验证定义的示例

形式定义本身不告诉我们如何求极限，但它能让我们验证猜测的极限值是否正确。以下例子展示如何用定义验证具体极限。定义的真正用途在于证明一般定理（从而简化具体极限的计算），而不仅仅是做以下这类验证。

**例2** 证明 $\displaystyle\lim_{x\to 1}(5x-3) = 2$。

**解** 令 $c=1$，$f(x) = 5x-3$，$L=2$。对任意给定的 $\varepsilon > 0$，需找 $\delta > 0$，使得当 $0 < |x-1| < \delta$ 时有 $|f(x)-2| < \varepsilon$。

从 $\varepsilon$ 不等式出发逆向求 $\delta$：

$$|(5x-3)-2| = |5x-5| < \varepsilon$$
$$5|x-1| < \varepsilon$$
$$|x-1| < \varepsilon/5.$$

取 $\delta = \varepsilon/5$（图2.18）。若 $0 < |x-1| < \delta = \varepsilon/5$，则

$$|(5x-3)-2| = |5x-5| = 5|x-1| < 5(\varepsilon/5) = \varepsilon.$$

这就证明了 $\displaystyle\lim_{x\to 1}(5x-3) = 2$。

注意：$\delta = \varepsilon/5$ 不是唯一满足条件的值，任何更小的正数同样有效。定义只要求找到**一个**有效的 $\delta$，不要求最大的那个。

> **图2.18示意**
>
> 坐标系中画有直线 $y = 5x-3$，纵轴标注 $2-\varepsilon$ 和 $2+\varepsilon$（水平带），横轴标注 $1-\varepsilon/5$ 和 $1+\varepsilon/5$（以1为中心的 $\delta$ 区间）。图示说明：$x$ 在此 $\delta$ 区间内时，函数值落在 $\varepsilon$ 带内。

---

**例3** 严格证明2.2节中图示的结论：

**(a)** $\displaystyle\lim_{x\to c} x = c$；

**(b)** $\displaystyle\lim_{x\to c} k = k$（$k$ 为常数）。

**解**

**(a)** 给定 $\varepsilon > 0$，需找 $\delta > 0$ 使得

$$|x - c| < \varepsilon \quad \text{当} \quad 0 < |x-c| < \delta.$$

取 $\delta = \varepsilon$（或任意更小的正数），蕴含关系自然成立（图2.19）。故 $\displaystyle\lim_{x\to c} x = c$。

**(b)** 给定 $\varepsilon > 0$，需找 $\delta > 0$ 使得

$$|k - k| < \varepsilon \quad \text{当} \quad 0 < |x-c| < \delta.$$

由于 $k - k = 0 < \varepsilon$，对任意正数 $\delta$ 蕴含关系均成立（图2.20）。故 $\displaystyle\lim_{x\to c} k = k$。

> **图2.19示意**
>
> 坐标系中画有直线 $y=x$，纵轴标注 $c-\varepsilon$ 和 $c+\varepsilon$，横轴标注 $c-\delta$ 和 $c+\delta$。取 $\delta \leq \varepsilon$ 时，$x$ 落在 $\delta$ 区间内则 $f(x)=x$ 落在 $\varepsilon$ 带内。
>
> **图2.20示意**
>
> 坐标系中画有水平直线 $y=k$，纵轴标注 $k-\varepsilon$ 和 $k+\varepsilon$，横轴标注 $c-\delta$ 和 $c+\delta$。因常数函数值始终为 $k$，对任意正 $\delta$ 均有 $|f(x)-k|=0 < \varepsilon$。

---

### 代数方法求 $\delta$

在例2和例3中，满足 $|f(x)-L| < \varepsilon$ 的 $x$ 区间关于 $c$ 对称，可取半区间长度为 $\delta$。若该区间关于 $c$ 不对称，则取 $\delta$ 为 $c$ 到区间**较近端点**的距离。

**例4** 对极限 $\displaystyle\lim_{x\to 5}\sqrt{x-1} = 2$，针对 $\varepsilon = 1$，求有效的 $\delta > 0$，即找 $\delta > 0$ 使得

$$|\sqrt{x-1} - 2| < 1 \quad \text{当} \quad 0 < |x-5| < \delta.$$

**解** 分两步进行。

**第1步：** 解不等式 $|\sqrt{x-1} - 2| < 1$，找含 $x=5$ 的开区间。

$$|\sqrt{x-1} - 2| < 1$$
$$-1 < \sqrt{x-1} - 2 < 1$$
$$1 < \sqrt{x-1} < 3$$
$$1 < x - 1 < 9$$
$$2 < x < 10.$$

不等式对开区间 $(2, 10)$ 内所有 $x \neq 5$ 成立。

**第2步：** 找 $\delta > 0$，使以5为中心的区间 $(5-\delta,\, 5+\delta)$ 包含在 $(2, 10)$ 内。5到区间 $(2,10)$ 的较近端点的距离为 $5-2=3$（图2.21）。取 $\delta = 3$（或更小的正数），则 $0 < |x-5| < 3$ 自动将 $x$ 限制在 $(2,10)$ 内，从而

$$|\sqrt{x-1} - 2| < 1 \quad \text{当} \quad 0 < |x-5| < 3. \qquad \blacksquare$$

> **图2.21示意**
>
> 数轴上标出点2、5、8、10，以5为中心的半径为3的区间 $(2,8)$ 落在 $(2,10)$ 内，两端均有标注3的间距。
>
> **图2.22示意**
>
> 坐标系中画有函数 $y=\sqrt{x-1}$ 的图像（类似根号曲线），纵轴标注1、2、3，横轴标注0、1、2、5、8、10，并标注以5为中心的左右各3的范围。

---

### 代数求 $\delta$ 的一般步骤

> 对给定的 $f$、$L$、$c$、$\varepsilon > 0$，寻找满足
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad 0 < |x-c| < \delta$$
>
> 的 $\delta > 0$，可按如下两步进行：
>
> **第1步：** 解不等式 $|f(x) - L| < \varepsilon$，找包含 $c$ 的开区间 $(a, b)$，使不等式对该区间内所有 $x \neq c$ 成立。（不要求在 $x=c$ 处成立；$f$ 在 $c$ 处的值不影响极限的存在性。）
>
> **第2步：** 找 $\delta > 0$，使以 $c$ 为中心的开区间 $(c-\delta,\, c+\delta)$ 落在 $(a, b)$ 内。对该 $\delta$ 区间内所有 $x \neq c$，不等式 $|f(x)-L| < \varepsilon$ 均成立。

---

**例5** 证明若

$$f(x) = \begin{cases} x^2, & x \neq 2 \\ 1, & x = 2 \end{cases}$$

则 $\displaystyle\lim_{x\to 2} f(x) = 4$。

**解** 需证：对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得

$$|f(x) - 4| < \varepsilon \quad \text{当} \quad 0 < |x-2| < \delta.$$

**第1步：** 对 $x \neq 2$，$f(x) = x^2$，解 $|x^2 - 4| < \varepsilon$（假设 $\varepsilon < 4$）：

$$|x^2 - 4| < \varepsilon$$
$$-\varepsilon < x^2 - 4 < \varepsilon$$
$$4 - \varepsilon < x^2 < 4 + \varepsilon$$
$$\sqrt{4-\varepsilon} < |x| < \sqrt{4+\varepsilon}$$
$$\sqrt{4-\varepsilon} < x < \sqrt{4+\varepsilon}.$$

不等式对开区间 $\left(\sqrt{4-\varepsilon},\, \sqrt{4+\varepsilon}\right)$ 内所有 $x \neq 2$ 成立（图2.23）。

**第2步：** 取 $\delta = \min\!\left\{2 - \sqrt{4-\varepsilon},\; \sqrt{4+\varepsilon} - 2\right\}$（即 $x=2$ 到区间较近端点的距离）。若 $\delta$ 取此值或更小正值，则 $0 < |x-2| < \delta$ 将 $x$ 限制在 $\left(\sqrt{4-\varepsilon},\, \sqrt{4+\varepsilon}\right)$ 内，从而对所有 $x$ 有

$$|f(x) - 4| < \varepsilon \quad \text{当} \quad 0 < |x-2| < \delta.$$

当 $\varepsilon \geq 4$ 时，取 $\delta = \min\!\left\{2,\; \sqrt{4+\varepsilon} - 2\right\}$。

> **图2.23示意**
>
> 坐标系中画有抛物线 $y=x^2$，图上标出 $x=2$ 处有空心圆点（对应 $f(2)=1$ 处有实心点在 $y=1$）。纵轴标注 $4-\varepsilon$ 和 $4+\varepsilon$，横轴标注 $\sqrt{4-\varepsilon}$ 和 $\sqrt{4+\varepsilon}$，说明在此区间内函数值落在 $\varepsilon$ 带内。

---

### 用定义证明定理

通常我们不用形式定义去验证具体极限，而是诉诸2.2节的定理。但定义正是这些定理的证明工具（见附录5）。作为示例，我们证明定理1的第1条——**和法则**。

**例6** 已知 $\displaystyle\lim_{x\to c} f(x) = L$，$\displaystyle\lim_{x\to c} g(x) = M$，证明

$$\lim_{x\to c}(f(x) + g(x)) = L + M.$$

**解** 给定 $\varepsilon > 0$，需找正数 $\delta$ 使得

$$|f(x) + g(x) - (L+M)| < \varepsilon \quad \text{当} \quad 0 < |x-c| < \delta.$$

整理各项：

$$|f(x) + g(x) - (L+M)| = |(f(x)-L) + (g(x)-M)| \leq |f(x)-L| + |g(x)-M|.$$

（最后一步使用了**三角不等式** $|a+b| \leq |a| + |b|$。）

由 $\displaystyle\lim_{x\to c} f(x) = L$，存在 $\delta_1 > 0$ 使得

$$|f(x) - L| < \frac{\varepsilon}{2} \quad \text{当} \quad 0 < |x-c| < \delta_1.$$

由 $\displaystyle\lim_{x\to c} g(x) = M$，存在 $\delta_2 > 0$ 使得

$$|g(x) - M| < \frac{\varepsilon}{2} \quad \text{当} \quad 0 < |x-c| < \delta_2.$$

取 $\delta = \min\{\delta_1,\, \delta_2\}$。若 $0 < |x-c| < \delta$，则 $|x-c| < \delta_1$ 且 $|x-c| < \delta_2$，故

$$|f(x) + g(x) - (L+M)| \leq |f(x)-L| + |g(x)-M| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

这就证明了 $\displaystyle\lim_{x\to c}(f(x)+g(x)) = L+M$。
