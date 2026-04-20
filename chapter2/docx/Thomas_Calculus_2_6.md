# 2.6 涉及无穷的极限；图像的渐近线（Limits Involving Infinity; Asymptotes of Graphs）

本节研究当自变量 $x$ 的大小趋向无穷大（即 $x \to \pm\infty$）时函数的行为，并将极限的概念推广到**无穷极限**。无穷极限为描述函数值无限增大的行为提供了简洁的符号和语言，进而用于分析具有**水平渐近线**或**垂直渐近线**的函数图像。

---

## $x \to \pm\infty$ 时的有限极限（Finite Limits as $x \to \pm\infty$）

无穷符号 $\infty$ 并不代表一个实数，它用于描述函数的定义域或值域超越一切有限界限时的行为。

以 $f(x) = \dfrac{1}{x}$ 为例（对所有 $x \neq 0$ 有定义）：当 $x$ 为正数且不断增大时，$\dfrac{1}{x}$ 趋向 $0$；当 $x$ 为负数且其绝对值不断增大时，$\dfrac{1}{x}$ 同样趋向 $0$。

> **图示说明（图2.49）：** $y = \dfrac{1}{x}$ 的图像：双曲线，分布在第一、三象限，随 $|x|$ 增大图像趋近 $x$ 轴（趋向 $0$），在 $x = 0$ 处无定义。图中标注了当 $x \to +\infty$ 和 $x \to -\infty$ 时图像趋近 $x$ 轴的趋势。

### 定义

> **定义**
>
> **1.** 若对每个 $\varepsilon > 0$，存在对应的数 $M$，使得对 $f$ 定义域中所有满足 $x > M$ 的 $x$，都有
> $$|f(x) - L| < \varepsilon$$
> 则称 $f(x)$ **当 $x$ 趋向正无穷时极限为 $L$**，记作
> $$\lim_{x \to +\infty} f(x) = L.$$
>
> **2.** 若对每个 $\varepsilon > 0$，存在对应的数 $N$，使得对 $f$ 定义域中所有满足 $x < N$ 的 $x$，都有
> $$|f(x) - L| < \varepsilon$$
> 则称 $f(x)$ **当 $x$ 趋向负无穷时极限为 $L$**，记作
> $$\lim_{x \to -\infty} f(x) = L.$$

两个基本结论（通过形式定义验证）：

$$\lim_{x \to \pm\infty} k = k \qquad \text{以及} \qquad \lim_{x \to \pm\infty} \frac{1}{x} = 0 \tag{1}$$

**例1** 证明：

(a) $\displaystyle\lim_{x \to +\infty} \frac{1}{x} = 0$　　(b) $\displaystyle\lim_{x \to -\infty} \frac{1}{x} = 0$

**解：**

(a) 给定 $\varepsilon > 0$，需找到 $M$，使得当 $x > M$ 时 $\left|\dfrac{1}{x}\right| < \varepsilon$。取 $M = \dfrac{1}{\varepsilon}$（或任何更大的正数）即可。

(b) 给定 $\varepsilon > 0$，需找到 $N$，使得当 $x < N$ 时 $\left|\dfrac{1}{x}\right| < \varepsilon$。取 $N = -\dfrac{1}{\varepsilon}$（或任何更小的数）即可。

> **图示说明（图2.50）：** 展示例1的几何意义。$y = \dfrac{1}{x}$ 的图像在 $x$ 轴上方（$x > 0$ 侧）和下方（$x < 0$ 侧）各有一条曲线。对任意正数 $\varepsilon$，图像在 $x = \dfrac{1}{\varepsilon}$（对应 $M$）之后始终落入水平带 $-\varepsilon < y < \varepsilon$ 内；在 $x = -\dfrac{1}{\varepsilon}$（对应 $N$）之前同样落入该带内。

### 定理12（无穷极限的极限运算法则）

> **定理12** 定理1中所有极限运算法则，在将 $\lim_{x \to c}$ 替换为 $\lim_{x \to +\infty}$ 或 $\lim_{x \to -\infty}$ 后仍然成立。即，$x$ 可以趋向有限数 $c$，也可以趋向 $\pm\infty$。

**例2** 利用定理12计算极限：

(a)
$$\lim_{x \to +\infty} \left(5 + \frac{1}{x}\right) = \lim_{x \to +\infty} 5 + \lim_{x \to +\infty} \frac{1}{x} = 5 + 0 = 5$$

(b)
$$\lim_{x \to -\infty} \frac{\pi\sqrt{3}}{x^2} = \lim_{x \to -\infty} \pi\sqrt{3} \cdot \frac{1}{x} \cdot \frac{1}{x} = \pi\sqrt{3} \cdot 0 \cdot 0 = 0$$

---

## 有理函数在无穷处的极限（Limits at Infinity of Rational Functions）

求有理函数当 $x \to \pm\infty$ 时的极限，方法是将分子和分母同除以分母中 $x$ 的最高次幂。

**例3** 分子次数不超过分母次数的情形：

(a)
$$\lim_{x \to +\infty} \frac{5x^2 + 8x - 3}{3x^2 + 2} = \lim_{x \to +\infty} \frac{5 + (8/x) - (3/x^2)}{3 + (2/x^2)} = \frac{5 + 0 - 0}{3 + 0} = \frac{5}{3}$$

(b)
$$\lim_{x \to -\infty} \frac{11x + 2}{2x^3 - 1} = \lim_{x \to -\infty} \frac{(11/x^2) + (2/x^3)}{2 - (1/x^3)} = \frac{0 + 0}{2 - 0} = 0$$

> **图示说明（图2.51）：** $y = \dfrac{5x^2 + 8x - 3}{3x^2 + 2}$ 的图像：有理函数曲线，两端趋近水平渐近线 $y = \dfrac{5}{3}$（图中红色水平线），图像在 $x = 0$ 附近有一个峰值，整体在 $[-5, 10]$ 的范围内展示，纵坐标约在 $-2$ 到 $2$ 之间。

> **图示说明（图2.52）：** $y = \dfrac{11x + 2}{2x^3 - 1}$ 的图像：有理函数曲线，两端趋近 $x$ 轴（水平渐近线 $y = 0$），在 $x$ 轴附近有较大波动，图像在 $[-4, 6]$ 范围内展示，纵坐标约在 $-8$ 到 $8$ 之间。

---

## 水平渐近线（Horizontal Asymptotes）

若图像上一点沿图像移动并越来越远离原点时，该点与某固定直线之间的距离趋于零，则称图像**渐近地**趋近该直线，该直线为图像的**渐近线**。

> **定义** 若
> $$\lim_{x \to +\infty} f(x) = b \qquad \text{或} \qquad \lim_{x \to -\infty} f(x) = b$$
> 则称直线 $y = b$ 为函数 $y = f(x)$ 图像的**水平渐近线（horizontal asymptote）**。

函数图像可以有零条、一条或两条水平渐近线，取决于 $x \to +\infty$ 和 $x \to -\infty$ 时极限是否存在。

**例4** 求函数 $f(x) = \dfrac{x^3 - 2}{|x|^3 + 1}$ 的水平渐近线。

**解：** 分别计算 $x \to \pm\infty$ 时的极限。

当 $x \geq 0$ 时：
$$\lim_{x \to +\infty} \frac{x^3 - 2}{x^3 + 1} = \lim_{x \to +\infty} \frac{1 - (2/x^3)}{1 + (1/x^3)} = 1$$

当 $x < 0$ 时（此时 $|x|^3 = (-x)^3 = -x^3$）：
$$\lim_{x \to -\infty} \frac{x^3 - 2}{-x^3 + 1} = \lim_{x \to -\infty} \frac{1 - (2/x^3)}{-1 + (1/x^3)} = -1$$

水平渐近线为 $y = 1$ 和 $y = -1$。注意图像对某个正数 $x$ 会穿越水平渐近线 $y = -1$。

> **图示说明（图2.53）：** $f(x) = \dfrac{x^3 - 2}{|x|^3 + 1}$ 的图像：S 形曲线，当 $x \to +\infty$ 时趋近水平渐近线 $y = 1$（上方），当 $x \to -\infty$ 时趋近 $y = -1$（下方）。图像在 $x$ 轴附近穿过，两条渐近线均以虚线标注。

**例5** 求：(a) $\displaystyle\lim_{x \to +\infty} \sin\!\left(\frac{1}{x}\right)$　　(b) $\displaystyle\lim_{x \to \pm\infty} x\sin\!\left(\frac{1}{x}\right)$

**解：** 令 $t = \dfrac{1}{x}$。

(a) 当 $x \to +\infty$ 时，$t \to 0^+$，故
$$\lim_{x \to +\infty} \sin\frac{1}{x} = \lim_{t \to 0^+} \sin t = 0$$

(b)
$$\lim_{x \to +\infty} x\sin\frac{1}{x} = \lim_{t \to 0^+} \frac{\sin t}{t} = 1, \qquad \lim_{x \to -\infty} x\sin\frac{1}{x} = \lim_{t \to 0^-} \frac{\sin t}{t} = 1$$

故 $y = 1$ 是水平渐近线。

> **图示说明（图2.54）：** $y = x\sin\!\dfrac{1}{x}$ 的图像：函数在 $x$ 轴两侧对称，随 $|x|$ 增大趋近水平渐近线 $y = 1$（图中虚线），在 $x$ 接近 $0$ 处图像波动，整体在 $[-1, 1]$ 范围的 $x$ 附近展示。

**例6** 求 $\displaystyle\lim_{x \to 0^+} x\left\lfloor \frac{1}{x} \right\rfloor$。

**解：** 令 $t = \dfrac{1}{x}$，则
$$\lim_{x \to 0^+} x\left\lfloor \frac{1}{x} \right\rfloor = \lim_{t \to +\infty} \frac{1}{t}\lfloor t \rfloor$$

由图2.55可知 $t - 1 \leq \lfloor t \rfloor \leq t$，两边除以 $t > 0$：

$$1 - \frac{1}{t} \leq \frac{1}{t}\lfloor t \rfloor \leq 1$$

由夹逼定理得 $\displaystyle\lim_{t \to +\infty} \dfrac{1}{t}\lfloor t \rfloor = 1$。

> **图示说明（图2.55）：** 最大整数函数 $y = \lfloor t \rfloor$ 的阶梯图像，夹在直线 $y = t - 1$（下界）与 $y = t$（上界）之间，三者在同一坐标系中展示，直观呈现夹逼关系。

**例7** 用夹逼定理求曲线 $y = 2 + \dfrac{\sin x}{x}$ 的水平渐近线。

**解：** 注意到

$$0 \leq \left|\frac{\sin x}{x}\right| \leq \left|\frac{1}{x}\right|$$

由于 $\displaystyle\lim_{x \to \pm\infty} \left|\dfrac{1}{x}\right| = 0$，故由夹逼定理得 $\displaystyle\lim_{x \to \pm\infty} \dfrac{\sin x}{x} = 0$，因此

$$\lim_{x \to \pm\infty} \left(2 + \frac{\sin x}{x}\right) = 2 + 0 = 2$$

直线 $y = 2$ 是该曲线的水平渐近线（左右两侧均成立）。

> **图示说明（图2.56）：** $y = 2 + \dfrac{\sin x}{x}$ 的图像：围绕水平线 $y = 2$ 上下振荡的曲线，振幅随 $|x|$ 增大而减小，图像在 $[-3\pi, 3\pi]$ 范围内展示，曲线无限多次穿越渐近线 $y = 2$，说明曲线可以无穷多次穿越其水平渐近线。

**例8** 求 $\displaystyle\lim_{x \to +\infty} \left(x - \sqrt{x^2 + 16}\right)$。

**解：** $x$ 和 $\sqrt{x^2 + 16}$ 均趋向无穷大，差的极限不明确（$\infty - \infty$ 不定型）。乘以共轭表达式：

$$\lim_{x \to +\infty} \left(x - \sqrt{x^2 + 16}\right) = \lim_{x \to +\infty} \frac{(x - \sqrt{x^2 + 16})(x + \sqrt{x^2 + 16})}{x + \sqrt{x^2 + 16}} = \lim_{x \to +\infty} \frac{-16}{x + \sqrt{x^2 + 16}}$$

当 $x \to +\infty$ 时，分母趋向无穷大，故极限为 $0$。也可用极限运算法则直接验证：

$$\lim_{x \to +\infty} \frac{-16}{x + \sqrt{x^2 + 16}} = \lim_{x \to +\infty} \frac{-16/x}{1 + \sqrt{1 + 16/x^2}} = \frac{0}{1 + \sqrt{1 + 0}} = 0$$

---

## 斜渐近线（Oblique Asymptotes）

若有理函数分子的次数比分母次数恰好高 $1$，则图像有**斜渐近线**（又称**斜线渐近线**）。通过多项式长除法，将 $f$ 表示为线性函数加上一个当 $x \to \pm\infty$ 时趋向零的余项，即可找到斜渐近线。

**例9** 求函数 $f(x) = \dfrac{x^2 - 3}{2x - 4}$ 的斜渐近线（图2.57）。

**解：** 对 $x^2 - 3$ 除以 $2x - 4$，做多项式长除法：

$$\frac{x^2 - 3}{2x - 4} = \underbrace{\left(\frac{x}{2} + 1\right)}_{\text{线性部分}} + \underbrace{\frac{1}{2x - 4}}_{\text{余项}}$$

当 $x \to \pm\infty$ 时，余项 $\dfrac{1}{2x-4} \to 0$，故直线

$$g(x) = \frac{x}{2} + 1$$

是图像的斜渐近线（左右两侧均成立）。

> **图示说明（图2.57）：** $f(x) = \dfrac{x^2 - 3}{2x - 4}$ 的图像：两段双曲线状曲线，在 $x = 2$（垂直渐近线）两侧各一段，随 $|x|$ 增大趋近斜线 $y = \dfrac{x}{2} + 1$（图中标注的斜渐近线）。图中还标注了曲线与渐近线之间的垂直距离随 $|x|$ 增大趋向零。

**分子次数高于分母次数的情形（续）：** 若有理函数分子次数大于分母次数，则当 $|x|$ 趋向无穷时极限为 $+\infty$ 或 $-\infty$（由分子分母的正负号决定）。

**例13** 求 $\displaystyle\lim_{x \to -\infty} \frac{2x^5 - 6x^4 + 1}{3x^2 + x - 7}$。

**解：** 分子分母同除以 $x^2$（分母的最高次幂）：

$$\lim_{x \to -\infty} \frac{2x^5 - 6x^4 + 1}{3x^2 + x - 7} = \lim_{x \to -\infty} \frac{2x^3 - 6x^2 + x^{-2}}{3 + x^{-1} - 7x^{-2}}$$

当 $x \to -\infty$ 时，分子趋向 $-\infty$，分母趋向 $3$，故极限为 $-\infty$。

---

## 无穷极限（Infinite Limits）

再看 $f(x) = \dfrac{1}{x}$：当 $x \to 0^+$ 时，$f(x)$ 的值无界增大，超过任何给定的正实数 $B$。我们用以下记号描述这种行为：

$$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{1}{x} = +\infty$$

这**不是**说极限存在，也不是说 $\infty$ 是某个实数，而是简洁地描述 $\dfrac{1}{x}$ 在 $x \to 0^+$ 时无界增大这一事实。

类似地，当 $x \to 0^-$ 时，$\dfrac{1}{x}$ 无界地趋向负无穷：

$$\lim_{x \to 0^-} \frac{1}{x} = -\infty$$

> **图示说明（图2.58）：** $y = \dfrac{1}{x}$ 在 $x = 0$ 附近的行为：图像在 $x \to 0^+$ 时沿 $y$ 轴正方向无限上升（右支），在 $x \to 0^-$ 时沿 $y$ 轴负方向无限下降（左支）。图中标注了任意正数 $B$ 对应的水平线和负数 $-B$ 对应的水平线，直观展示单侧无穷极限。

### 无穷极限的精确定义

> **定义**
>
> **1.** 若对每个正实数 $B$，存在对应的 $\delta > 0$，使得当 $0 < |x - c| < \delta$ 时 $f(x) > B$，则称
> $$\lim_{x \to c} f(x) = +\infty$$
>
> **2.** 若对每个负实数 $-B$，存在对应的 $\delta > 0$，使得当 $0 < |x - c| < \delta$ 时 $f(x) < -B$，则称
> $$\lim_{x \to c} f(x) = -\infty$$

> **图示说明（图2.61）：** 在 $c - \delta < x < c + \delta$ 的范围内，$f(x)$ 的图像位于水平线 $y = B$ 上方，示意无穷极限 $\lim_{x \to c} f(x) = +\infty$ 的几何含义。

> **图示说明（图2.62）：** 在 $c - \delta < x < c + \delta$ 的范围内，$f(x)$ 的图像位于水平线 $y = -B$ 下方，示意无穷极限 $\lim_{x \to c} f(x) = -\infty$ 的几何含义。

**例10** 求 $\displaystyle\lim_{x \to 1^+} \frac{1}{x - 1}$ 和 $\displaystyle\lim_{x \to 1^-} \frac{1}{x - 1}$。

**几何解法：** $y = \dfrac{1}{x-1}$ 是 $y = \dfrac{1}{x}$ 向右平移 $1$ 个单位的图像，故

$$\lim_{x \to 1^+} \frac{1}{x - 1} = +\infty, \qquad \lim_{x \to 1^-} \frac{1}{x - 1} = -\infty$$

**分析解法：** 当 $x \to 1^+$ 时，$(x-1) \to 0^+$，故 $\dfrac{1}{x-1} \to +\infty$；当 $x \to 1^-$ 时，$(x-1) \to 0^-$，故 $\dfrac{1}{x-1} \to -\infty$。

> **图示说明（图2.59）：** $y = \dfrac{1}{x-1}$ 的图像：以 $x = 1$ 为垂直渐近线，图像在 $x \to 1^+$ 时升至 $+\infty$，在 $x \to 1^-$ 时降至 $-\infty$，形态与 $y = \dfrac{1}{x}$ 完全相同但整体右移 $1$ 个单位。

**例11** 讨论 $f(x) = \dfrac{1}{x^2}$ 当 $x \to 0$ 时的行为。

**解：** 从 $0$ 的两侧趋近时，$\dfrac{1}{x^2}$ 均为正数且无界增大，故

$$\lim_{x \to 0} \frac{1}{x^2} = +\infty$$

> **图示说明（图2.60）：** $f(x) = \dfrac{1}{x^2}$ 的图像：以 $x = 0$ 为垂直渐近线，图像在 $x \to 0$ 时（从两侧）均趋向 $+\infty$，关于 $y$ 轴对称，图中标注任意高度 $B$ 均会被图像超过。

**例12** 有理函数在分母零点处可以有各种不同的行为：

(a) $\displaystyle\lim_{x \to 2} \frac{(x-2)^2}{x^2 - 4} = \lim_{x \to 2} \frac{x-2}{x+2} = 0$

(b) $\displaystyle\lim_{x \to 2} \frac{x-2}{x^2 - 4} = \lim_{x \to 2} \frac{1}{x+2} = \frac{1}{4}$

(c) $\displaystyle\lim_{x \to 2^+} \frac{x-3}{x^2 - 4} = -\infty$（$x > 2$ 时分子为负、分母为正）

(d) $\displaystyle\lim_{x \to 2^-} \frac{x-3}{x^2 - 4} = +\infty$（$x < 2$ 时分子为负、分母为负）

(e) $\displaystyle\lim_{x \to 2} \frac{x-3}{x^2 - 4}$ **不存在**（左右极限不同）

(f) $\displaystyle\lim_{x \to 2} \frac{2-x}{(x-2)^3} = \lim_{x \to 2} \frac{-1}{(x-2)^2} = -\infty$（分母为正，故值为负）

在 (a)(b) 中，分母在 $x = 2$ 处的零点被分子的因子约分消除，极限为有限值；(f) 即使约分后分母仍有零因子。

**例14** 证明 $\displaystyle\lim_{x \to 0} \frac{1}{x^2} = +\infty$。

**证明：** 给定 $B > 0$，需找 $\delta > 0$ 使得当 $0 < |x| < \delta$ 时 $\dfrac{1}{x^2} > B$。

注意 $\dfrac{1}{x^2} > B$ 当且仅当 $x^2 < \dfrac{1}{B}$，即 $|x| < \dfrac{1}{\sqrt{B}}$。

取 $\delta = \dfrac{1}{\sqrt{B}}$，则当 $|x| < \delta$ 时

$$\frac{1}{x^2} > \frac{1}{\delta^2} = B$$

故 $\displaystyle\lim_{x \to 0} \frac{1}{x^2} = +\infty$。

---

## 垂直渐近线（Vertical Asymptotes）

$f(x) = \dfrac{1}{x}$ 图像上的点沿图像移动并远离原点时，该点与 $y$ 轴（即 $x = 0$）之间的距离趋向零，因为

$$\lim_{x \to 0^+} \frac{1}{x} = +\infty \qquad \text{且} \qquad \lim_{x \to 0^-} \frac{1}{x} = -\infty$$

我们称直线 $x = 0$（$y$ 轴）为 $f(x) = \dfrac{1}{x}$ 图像的**垂直渐近线**。

> **定义** 若
> $$\lim_{x \to a^+} f(x) = \pm\infty \qquad \text{或} \qquad \lim_{x \to a^-} f(x) = \pm\infty$$
> 则称直线 $x = a$ 为函数 $y = f(x)$ 图像的**垂直渐近线（vertical asymptote）**。

> **图示说明（图2.63）：** 双曲线 $y = \dfrac{1}{x}$ 的图像，坐标轴（$y$ 轴即 $x = 0$，$x$ 轴即 $y = 0$）分别是两个分支的垂直渐近线和水平渐近线，图中分别标注"Vertical asymptote $x = 0$"和"Horizontal asymptote $y = 0$"。

**例15** 求曲线 $y = \dfrac{x+3}{x+2}$ 的水平和垂直渐近线。

**解：** 对 $x + 3$ 除以 $x + 2$ 做多项式除法：

$$y = \frac{x+3}{x+2} = 1 + \frac{1}{x+2}$$

- 当 $x \to \pm\infty$ 时，曲线趋近水平渐近线 $y = 1$；
- 当 $x \to -2$ 时，曲线趋近垂直渐近线 $x = -2$。

该曲线是 $y = \dfrac{1}{x}$ 向上平移 $1$ 个单位、向左平移 $2$ 个单位的结果，渐近线由坐标轴变为 $y = 1$ 和 $x = -2$。

> **图示说明（图2.64）：** $y = \dfrac{x+3}{x+2} = 1 + \dfrac{1}{x+2}$ 的图像：双曲线的两个分支，水平渐近线为 $y = 1$（水平虚线），垂直渐近线为 $x = -2$（垂直虚线），图像在 $x = -2$ 左右各有一支，形态与 $y = \dfrac{1}{x}$ 相同但整体平移。

**例16** 求函数 $f(x) = -\dfrac{8}{x^2 - 4}$ 的水平和垂直渐近线。

**解：** $f$ 是偶函数，图像关于 $y$ 轴对称，分母在 $x = \pm 2$ 处为零。

(a) **水平渐近线：** $\displaystyle\lim_{x \to \pm\infty} f(x) = 0$，故 $y = 0$（$x$ 轴）是水平渐近线。注意曲线只从负值方向趋近 $x$ 轴（即从下方），且 $f(0) = 2$。

(b) **垂直渐近线：** 由于

$$\lim_{x \to 2^+} f(x) = -\infty, \qquad \lim_{x \to 2^-} f(x) = +\infty$$

故 $x = 2$ 是垂直渐近线；由对称性，$x = -2$ 也是垂直渐近线。

> **图示说明（图2.65）：** $y = -\dfrac{8}{x^2 - 4}$ 的图像：关于 $y$ 轴对称，在 $x = \pm 2$ 两侧各有曲线分支，图像在 $|x| > 2$ 的两段从下方趋近 $x$ 轴（水平渐近线 $y = 0$），在 $-2 < x < 2$ 段从下方形成一个开口向下的弓形。三个垂直渐近线和水平渐近线均标注。

**例17** 函数 $y = \sec x = \dfrac{1}{\cos x}$ 和 $y = \tan x = \dfrac{\sin x}{\cos x}$ 在 $\cos x = 0$ 的所有奇数倍 $\dfrac{\pi}{2}$ 处均有垂直渐近线。

> **图示说明（图2.66）：** 两幅图分别展示 $y = \sec x$ 和 $y = \tan x$ 在 $[-\frac{3\pi}{2}, \frac{3\pi}{2}]$ 范围内的图像：两个函数均有无穷多条垂直渐近线（位于 $x = \pm\frac{\pi}{2}, \pm\frac{3\pi}{2}, \ldots$ 处），$\sec x$ 的图像由一系列开口向上和向下的 U 形弧构成（值域为 $|y| \geq 1$），$\tan x$ 的图像在每两条渐近线之间单调递增（值域为全体实数）。

---

## 主导项（Dominant Terms）

在例9中，通过长除法将 $f(x) = \dfrac{x^2 - 3}{2x - 4}$ 改写为

$$f(x) = \left(\frac{x}{2} + 1\right) + \frac{1}{2x - 4}$$

这告诉我们：

- 当 $|x|$ 很大时，$\dfrac{1}{2x-4} \approx 0$，故 $f(x) \approx \dfrac{x}{2} + 1$（线性项**主导**）；
- 当 $x$ 非常接近 $2$ 时，$\dfrac{1}{2x-4}$ 的绝对值非常大，它**主导**函数值。

**例18** 设 $f(x) = 3x^4 - 2x^3 + 3x^2 - 5x + 6$，$g(x) = 3x^4$。证明：当 $|x|$ 很大时，$f$ 与 $g$ 的行为相似（比值趋向 $1$）。

**解：** 计算

$$\lim_{x \to \pm\infty} \frac{f(x)}{g(x)} = \lim_{x \to \pm\infty} \frac{3x^4 - 2x^3 + 3x^2 - 5x + 6}{3x^4} = \lim_{x \to \pm\infty} \left(1 - \frac{2}{3x} + \frac{1}{x^2} - \frac{5}{3x^3} + \frac{2}{x^4}\right) = 1$$

> **图示说明（图2.67）：** 两幅图对比 $f(x)$ 与 $g(x) = 3x^4$ 的图像：
> - (a) 在 $[-2, 2]$ 的小范围内，两函数图像差异显著，$f$ 在 $y$ 轴附近有明显波动而 $g$ 仅为简单抛物线形态。
> - (b) 在 $[-20, 20]$ 的大范围内，两函数图像几乎完全重合，验证了 $3x^4$ 项在 $|x|$ 较大时主导多项式的行为。
