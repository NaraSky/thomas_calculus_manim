## 2.6 涉及无穷的极限；图像的渐近线

本节研究自变量 $x$ 的绝对值无限增大（即 $x \to \pm\infty$）时函数的行为，并将极限概念推广到**无穷极限**。无穷极限为描述函数值无限增大的行为提供了简洁的符号和语言，这些思想用于分析具有水平渐近线或竖直渐近线的函数图像。

---

### 当 $x \to \pm\infty$ 时的有限极限

无穷符号 $\infty$ 不表示实数，它用于描述函数在定义域或值域上超越所有有限界限的行为。

以函数 $f(x) = 1/x$ 为例（图2.49）：当 $x$ 为正值且无限增大时，$1/x$ 趋近于零；当 $x$ 为负值且绝对值无限增大时，$1/x$ 同样趋近于零。我们说 $f(x) = 1/x$ 在 $x \to +\infty$ 和 $x \to -\infty$ 时极限均为0。

> **图2.49示意**
>
> 坐标系中画有双曲线 $y=1/x$ 的两支，在第一、三象限各一支，均以坐标轴为渐近线。当 $x$ 趋向 $\pm\infty$ 时，曲线趋近 $x$ 轴（$y=0$）。

---

> **定义**
>
> **1.** 若对每个 $\varepsilon > 0$，存在对应的数 $M$，使得对 $f$ 定义域中所有 $x$，
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad x > M,$$
>
> 则称 $f(x)$ 在 **$x$ 趋向正无穷时**的极限为 $L$，记作 $\displaystyle\lim_{x\to\infty}f(x) = L$。
>
> **2.** 若对每个 $\varepsilon > 0$，存在对应的数 $N$，使得对 $f$ 定义域中所有 $x$，
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad x < N,$$
>
> 则称 $f(x)$ 在 **$x$ 趋向负无穷时**的极限为 $L$，记作 $\displaystyle\lim_{x\to-\infty}f(x) = L$。

---

计算 $x \to \pm\infty$ 时极限的策略与2.2节处理有限极限类似，起点函数换为 $y=k$ 和 $y=1/x$。两个基本事实为：

$$\lim_{x\to\pm\infty}k = k \quad \text{且} \quad \lim_{x\to\pm\infty}\frac{1}{x} = 0. \tag{1}$$

**例1** 证明：**(a)** $\displaystyle\lim_{x\to\infty}\frac{1}{x}=0$；**(b)** $\displaystyle\lim_{x\to-\infty}\frac{1}{x}=0$。

**解**

**(a)** 给定 $\varepsilon>0$，需找 $M$ 使得当 $x>M$ 时 $|1/x|<\varepsilon$。取 $M=1/\varepsilon$（或任意更大的正数）即可（图2.50）。

**(b)** 给定 $\varepsilon>0$，需找 $N$ 使得当 $x<N$ 时 $|1/x|<\varepsilon$。取 $N=-1/\varepsilon$（或任意更小的数）即可。

> **图2.50示意**
>
> 双轴坐标系中画有 $y=1/x$ 的图像。纵轴上标出 $\varepsilon$ 和 $-\varepsilon$ 的水平带，标注 $M=1/\varepsilon$（右侧）和 $N=-1/\varepsilon$（左侧）。当 $x>M$ 时图像进入上方 $\varepsilon$ 带并保持在内；当 $x<N$ 时图像进入下方 $-\varepsilon$ 带并保持在内。

---

> **定理12** 定理1中所有极限定律在将 $\displaystyle\lim_{x\to c}$ 替换为 $\displaystyle\lim_{x\to\infty}$ 或 $\displaystyle\lim_{x\to-\infty}$ 后仍然成立。

**例2** 利用定理12的性质：

**(a)**

$$\lim_{x\to\infty}\!\left(5+\frac{1}{x}\right) = \lim_{x\to\infty}5 + \lim_{x\to\infty}\frac{1}{x} = 5+0 = 5 \quad \text{（和法则）}$$

**(b)**

$$\lim_{x\to-\infty}\frac{\pi\sqrt{3}}{x^2} = \lim_{x\to-\infty}\pi\sqrt{3}\cdot\frac{1}{x}\cdot\frac{1}{x} = \pi\sqrt{3}\cdot 0\cdot 0 = 0 \quad \text{（积法则）} \qquad \blacksquare$$

---

### 有理函数在无穷处的极限

求有理函数在 $x\to\pm\infty$ 时的极限，将分子分母除以分母中 $x$ 的最高次幂，结果取决于分子分母的次数。

**例3** 分子次数不超过分母次数的情形：

**(a)**

$$\lim_{x\to\infty}\frac{5x^2+8x-3}{3x^2+2} = \lim_{x\to\infty}\frac{5+(8/x)-(3/x^2)}{3+(2/x^2)} = \frac{5+0-0}{3+0} = \frac{5}{3}.$$

（分子分母同除以 $x^2$。图2.51显示图像趋近水平线 $y=5/3$。）

**(b)**

$$\lim_{x\to-\infty}\frac{11x+2}{2x^3-1} = \lim_{x\to-\infty}\frac{(11/x^2)+(2/x^3)}{2-(1/x^3)} = \frac{0+0}{2-0} = 0.$$

（分子分母同除以 $x^3$。图2.52显示图像趋近 $x$ 轴。）

> **图2.51示意**：坐标系中画有函数 $y=\dfrac{5x^2+8x-3}{3x^2+2}$ 的图像，以及水平渐近线 $y=5/3$，图像在 $x$ 较大时从两侧趋近此直线。
>
> **图2.52示意**：坐标系中画有函数 $y=\dfrac{11x+2}{2x^3-1}$ 的图像，以 $x$ 轴（$y=0$）为水平渐近线，图像在两端趋向0。

---

### 水平渐近线

---

> **定义** 若 $\displaystyle\lim_{x\to\infty}f(x)=b$ 或 $\displaystyle\lim_{x\to-\infty}f(x)=b$，则称直线 $y=b$ 是函数 $y=f(x)$ 图像的**水平渐近线**。

---

函数图像可以有零条、一条或两条水平渐近线，取决于函数在 $x\to\infty$ 和 $x\to-\infty$ 时是否有极限。

**例4** 求函数 $f(x) = \dfrac{x^3-2}{|x|^3+1}$ 的水平渐近线。

**解** 分别计算 $x\to\pm\infty$ 时的极限：

当 $x\geq 0$：

$$\lim_{x\to\infty}\frac{x^3-2}{x^3+1} = \lim_{x\to\infty}\frac{1-(2/x^3)}{1+(1/x^3)} = 1.$$

当 $x<0$：

$$\lim_{x\to-\infty}\frac{x^3-2}{(-x)^3+1} = \lim_{x\to-\infty}\frac{1-(2/x^3)}{-1+(1/x^3)} = -1.$$

水平渐近线为 $y=1$ 和 $y=-1$（图2.53）。注意，曲线在正 $x$ 处穿越水平渐近线 $y=-1$，说明曲线可以越过渐近线。

> **图2.53示意**
>
> 坐标系中画有函数 $f(x)=\dfrac{x^3-2}{|x|^3+1}$ 的图像，以两条水平虚线 $y=1$（右侧渐近线）和 $y=-1$（左侧渐近线）为界。曲线在正 $x$ 值处穿越 $y=-1$，说明函数可以跨越水平渐近线。

**例5** 求 **(a)** $\displaystyle\lim_{x\to\infty}\sin(1/x)$；**(b)** $\displaystyle\lim_{x\to\pm\infty}x\sin(1/x)$。

**解**

**(a)** 令 $t=1/x$，则 $x\to\infty$ 时 $t\to 0^+$，故

$$\lim_{x\to\infty}\sin\frac{1}{x} = \lim_{t\to 0^+}\sin t = 0.$$

**(b)** 令 $t=1/x$：

$$\lim_{x\to\infty}x\sin\frac{1}{x} = \lim_{t\to 0^+}\frac{\sin t}{t} = 1, \quad \lim_{x\to-\infty}x\sin\frac{1}{x} = \lim_{t\to 0^-}\frac{\sin t}{t} = 1.$$

水平渐近线为 $y=1$（图2.54）。

> **图2.54示意**
>
> 坐标系中画有函数 $y=x\sin(1/x)$ 的图像，在 $x=0$ 附近有振荡，两端均趋近水平线 $y=1$。

**例6** 求 $\displaystyle\lim_{x\to 0^+}x\lfloor 1/x\rfloor$。

**解** 令 $t=1/x$，则 $x\to 0^+$ 时 $t\to\infty$，故

$$\lim_{x\to 0^+}x\lfloor 1/x\rfloor = \lim_{t\to\infty}\frac{\lfloor t\rfloor}{t}.$$

由图2.55可知 $t-1\leq\lfloor t\rfloor\leq t$，各项除以 $t>0$：

$$1-\frac{1}{t}\leq\frac{\lfloor t\rfloor}{t}\leq 1.$$

由夹逼定理，$\displaystyle\lim_{t\to\infty}\frac{\lfloor t\rfloor}{t}=1$，故所求极限为1。

> **图2.55示意**
>
> 坐标系中画有取整函数 $y=\lfloor t\rfloor$（阶梯形）被夹在直线 $y=t-1$（从下方）和 $y=t$（从上方）之间，说明夹逼的几何意义。

夹逼定理同样适用于 $x\to\pm\infty$ 时的极限。

**例7** 用夹逼定理求曲线 $y=2+\dfrac{\sin x}{x}$ 的水平渐近线。

**解** 因为 $0\leq|\sin x/x|\leq|1/x|$，且 $\displaystyle\lim_{x\to\pm\infty}|1/x|=0$，由夹逼定理知

$$\lim_{x\to\pm\infty}\frac{\sin x}{x}=0, \quad \text{故} \quad \lim_{x\to\pm\infty}\!\left(2+\frac{\sin x}{x}\right)=2.$$

直线 $y=2$ 是曲线的水平渐近线（图2.56）。本例说明曲线可以无限次穿越水平渐近线。

> **图2.56示意**
>
> 坐标系中画有函数 $y=2+(\sin x)/x$ 的图像，以水平线 $y=2$ 为渐近线，曲线在 $[-3\pi, 3\pi]$ 范围内多次穿越该渐近线，振荡幅度随 $|x|$ 增大而减小。

**例8** 求 $\displaystyle\lim_{x\to\infty}\!\left(x-\sqrt{x^2+16}\right)$。

**解** 两项均趋向无穷，不能直接相减（$\infty - \infty$ 无意义）。乘以共轭式：

$$\lim_{x\to\infty}\!\left(x-\sqrt{x^2+16}\right) = \lim_{x\to\infty}\frac{x^2-(x^2+16)}{x+\sqrt{x^2+16}} = \lim_{x\to\infty}\frac{-16}{x+\sqrt{x^2+16}}.$$

分母趋向无穷，分子为常数，故极限为0。也可用极限定律直接验证：

$$\lim_{x\to\infty}\frac{-16/x}{1+\sqrt{1+16/x^2}} = \frac{0}{1+1} = 0. \qquad \blacksquare$$

---

### 斜渐近线

若有理函数分子次数比分母次数恰好高1次，图像有**斜渐近线**（斜线渐近线）。做多项式除法，将 $f$ 表示为线性函数加余项，余项在 $x\to\pm\infty$ 时趋向零。

**例9** 求函数 $f(x)=\dfrac{x^2-3}{2x-4}$ 的斜渐近线（图2.57）。

**解** 用 $(2x-4)$ 除 $(x^2-3)$：

$$f(x) = \frac{x^2-3}{2x-4} = \underbrace{\left(\frac{x}{2}+1\right)}_{\text{线性部分}} + \underbrace{\left(\frac{1}{2x-4}\right)}_{\text{余项}}.$$

当 $x\to\pm\infty$ 时，余项趋向零，直线 $g(x)=\dfrac{x}{2}+1$ 是图像的斜渐近线（在左右两侧均成立）。

> **图2.57示意**
>
> 坐标系中画有函数 $y=\dfrac{x^2-3}{2x-4}$ 的图像（双曲线状，$x=2$ 处有竖直渐近线），以及斜渐近线 $y=x/2+1$（虚线）。图中标注曲线与斜线之间的竖直距离随 $|x|$ 增大趋向零。

---

### 无穷极限

再看函数 $f(x)=1/x$：当 $x\to 0^+$ 时，函数值无限增大，超过任何正实数 $B$。我们称 $f(x)$ 在 $x\to 0^+$ 时**趋向正无穷**，记作

$$\lim_{x\to 0^+}\frac{1}{x} = +\infty.$$

这不是说极限存在，也不是说 $+\infty$ 是实数。这只是说明极限不存在——因为 $1/x$ 无限增大。类似地，

$$\lim_{x\to 0^-}\frac{1}{x} = -\infty.$$

> **图2.58示意**
>
> 坐标系中画有 $y=1/x$ 的图像，右支在 $x\to 0^+$ 时向上无限延伸（趋向 $+\infty$），左支在 $x\to 0^-$ 时向下无限延伸（趋向 $-\infty$）。两侧分别标注"无论 $B$ 多大，图像都会更高"和"无论 $-B$ 多低，图像都会更低"。

**例10** 求 $\displaystyle\lim_{x\to 1^+}\frac{1}{x-1}$ 和 $\displaystyle\lim_{x\to 1^-}\frac{1}{x-1}$。

**几何解法：** $y=1/(x-1)$ 是 $y=1/x$ 向右平移1个单位的结果（图2.59），故

$$\lim_{x\to 1^+}\frac{1}{x-1}=+\infty, \quad \lim_{x\to 1^-}\frac{1}{x-1}=-\infty.$$

**分析解法：** 当 $x\to 1^+$ 时，$(x-1)\to 0^+$，故 $1/(x-1)\to+\infty$；当 $x\to 1^-$ 时，$(x-1)\to 0^-$，故 $1/(x-1)\to-\infty$。

**例11** 讨论 $f(x)=1/x^2$ 在 $x\to 0$ 时的行为。

**解** 无论从哪侧趋近零，$1/x^2$ 的值均为正且无界增大（图2.60），故

$$\lim_{x\to 0}\frac{1}{x^2}=+\infty. \qquad \blacksquare$$

注意 $y=1/x$ 在 $x\to 0$ 时没有一致行为（从右趋向 $+\infty$，从左趋向 $-\infty$），极限不存在。$y=1/x^2$ 不同：从两侧均趋向正无穷，故可以写 $\displaystyle\lim_{x\to 0}(1/x^2)=+\infty$。

> **图2.59示意**：坐标系中画有 $y=1/(x-1)$ 的图像，以 $x=1$ 为竖直渐近线，形状与 $y=1/x$ 相同但向右平移了1个单位。
>
> **图2.60示意**：坐标系中画有 $y=1/x^2$ 的图像，两支均在第一、二象限，在 $x=0$ 两侧均向上无界延伸。

**例12** 有理函数在分母零点附近的各种行为：

**(a)** $\displaystyle\lim_{x\to 2}\frac{(x-2)^2}{x^2-4} = \lim_{x\to 2}\frac{x-2}{x+2} = 0$（分子零点消去分母零点，极限存在）

**(b)** $\displaystyle\lim_{x\to 2}\frac{x-2}{x^2-4} = \lim_{x\to 2}\frac{1}{x+2} = \frac{1}{4}$（消去后可代入）

**(c)** $\displaystyle\lim_{x\to 2^+}\frac{x-3}{x^2-4} = \lim_{x\to 2^+}\frac{x-3}{(x-2)(x+2)} = -\infty$（$x>2$ 且 $x$ 近2时值为负）

**(d)** $\displaystyle\lim_{x\to 2^-}\frac{x-3}{x^2-4} = +\infty$（$x<2$ 且 $x$ 近2时值为正）

**(e)** $\displaystyle\lim_{x\to 2}\frac{x-3}{x^2-4}$ 不存在（左右极限不相等）

**(f)** $\displaystyle\lim_{x\to 2}\frac{2-x}{(x-2)^3} = \lim_{x\to 2}\frac{-(x-2)}{(x-2)^3} = \lim_{x\to 2}\frac{-1}{(x-2)^2} = -\infty$（分母为正，故值为负）

---

**例13** 求 $\displaystyle\lim_{x\to-\infty}\frac{2x^5-6x^4+1}{3x^2+x-7}$。

**解** 分子分母同除以 $x^2$（分母最高次幂）：

$$\lim_{x\to-\infty}\frac{2x^3-6x^2+x^{-2}}{3+x^{-1}-7x^{-2}}.$$

当 $x\to-\infty$ 时，分子中 $2x^3\to-\infty$，分母趋近3，故极限为 $-\infty$。

---

### 无穷极限的精确定义

---

> **定义**
>
> **1.** 若对每个正实数 $B$，存在 $\delta>0$，使得
>
> $$f(x) > B \quad \text{当} \quad 0 < |x-c| < \delta,$$
>
> 则称 $f(x)$ 在 $x\to c$ 时**趋向正无穷**，记作 $\displaystyle\lim_{x\to c}f(x)=+\infty$。
>
> **2.** 若对每个负实数 $-B$，存在 $\delta>0$，使得
>
> $$f(x) < -B \quad \text{当} \quad 0 < |x-c| < \delta,$$
>
> 则称 $f(x)$ 在 $x\to c$ 时**趋向负无穷**，记作 $\displaystyle\lim_{x\to c}f(x)=-\infty$。

---

> **图2.61示意**：对 $c-\delta<x<c+\delta$（$x\neq c$），函数图像在水平线 $y=B$ 上方，说明 $f(x)>B$。
>
> **图2.62示意**：对 $c-\delta<x<c+\delta$（$x\neq c$），函数图像在水平线 $y=-B$ 下方，说明 $f(x)<-B$。

**例14** 证明 $\displaystyle\lim_{x\to 0}\frac{1}{x^2}=+\infty$。

**解** 给定 $B>0$，需找 $\delta>0$ 使得 $0<|x|<\delta$ 时 $1/x^2>B$。

由 $\dfrac{1}{x^2}>B$ 等价于 $x^2<\dfrac{1}{B}$，即 $|x|<\dfrac{1}{\sqrt{B}}$。

取 $\delta=1/\sqrt{B}$，则 $|x|<\delta$ 时

$$\frac{1}{x^2}>\frac{1}{\delta^2}=B.$$

由定义，$\displaystyle\lim_{x\to 0}\frac{1}{x^2}=+\infty$。

---

### 竖直渐近线

$f(x)=1/x$ 的图像与 $y$ 轴（$x=0$）之间的距离随图像向上延伸而趋向零（图2.63）。由于

$$\lim_{x\to 0^+}\frac{1}{x}=+\infty \quad \text{且} \quad \lim_{x\to 0^-}\frac{1}{x}=-\infty,$$

我们说直线 $x=0$（$y$ 轴）是 $f(x)=1/x$ 图像的**竖直渐近线**。

---

> **定义** 若 $\displaystyle\lim_{x\to a^+}f(x)=\pm\infty$ 或 $\displaystyle\lim_{x\to a^-}f(x)=\pm\infty$，则称直线 $x=a$ 是函数 $y=f(x)$ 图像的**竖直渐近线**。

---

> **图2.63示意**
>
> 坐标系中画有双曲线 $y=1/x$ 的两支，坐标轴分别标注为竖直渐近线（$x=0$，即 $y$ 轴）和水平渐近线（$y=0$，即 $x$ 轴），说明双曲线以坐标轴为渐近线。

**例15** 求曲线 $y=\dfrac{x+3}{x+2}$ 的水平渐近线和竖直渐近线。

**解** 用 $(x+2)$ 除 $(x+3)$：

$$y = \frac{x+3}{x+2} = 1 + \frac{1}{x+2}.$$

当 $x\to\pm\infty$ 时，$1/(x+2)\to 0$，曲线趋近水平渐近线 $y=1$；当 $x\to-2$ 时，$1/(x+2)\to\pm\infty$，$x=-2$ 是竖直渐近线（图2.64）。

> **图2.64示意**
>
> 坐标系中画有 $y=\dfrac{x+3}{x+2}=1+\dfrac{1}{x+2}$ 的图像：以竖直虚线 $x=-2$ 为竖直渐近线，以水平虚线 $y=1$ 为水平渐近线，整体形状是将 $y=1/x$ 向左平移2、向上平移1后的双曲线。

**例16** 求函数 $f(x)=\dfrac{-8}{x^2-4}$ 的所有渐近线。

**解** $f$ 为偶函数，图像关于 $y$ 轴对称（图2.65）。

**(a) 水平渐近线：** $\displaystyle\lim_{x\to\infty}f(x)=0$，故 $y=0$ 是水平渐近线（由对称性，对两侧均成立）。注意曲线仅从 $x$ 轴下方趋近（即曲线始终在 $x$ 轴下方）。

**(b) 竖直渐近线：** 分母在 $x=\pm 2$ 处为零。由于

$$\lim_{x\to 2^+}f(x)=-\infty, \quad \lim_{x\to 2^-}f(x)=+\infty,$$

$x=2$ 是竖直渐近线。由对称性，$x=-2$ 也是竖直渐近线。

> **图2.65示意**
>
> 坐标系中画有函数 $y=-8/(x^2-4)$ 的图像，关于 $y$ 轴对称，有两条竖直渐近线（$x=\pm 2$，均为虚线）和一条水平渐近线（$x$ 轴，$y=0$）。曲线在 $|x|>2$ 段位于 $x$ 轴下方，在 $|x|<2$ 段趋向正无穷。

**例17** 函数 $y=\sec x=1/\cos x$ 和 $y=\tan x=\sin x/\cos x$ 在 $\cos x=0$ 的奇数倍 $\pi/2$ 处均有竖直渐近线（图2.66）。

> **图2.66示意**
>
> 两个并排坐标系：左图画有 $y=\sec x$ 的图像，在 $x=\pm\pi/2,\,\pm 3\pi/2,\ldots$ 处各有竖直渐近线，曲线在渐近线之间呈抛物线状（$|\sec x|\geq 1$）；右图画有 $y=\tan x$ 的图像，在相同的奇数倍 $\pi/2$ 处各有竖直渐近线，曲线在各区间内单调递增。

---

### 主导项

以例9的函数 $f(x)=\dfrac{x^2-3}{2x-4}$ 为例，其分解为

$$f(x) = \underbrace{\left(\frac{x}{2}+1\right)}_{\text{主导项（}|x|\text{大时）}} + \underbrace{\left(\frac{1}{2x-4}\right)}_{\text{主导项（}x\text{近2时）}}.$$

当 $|x|$ 很大时，$1/(2x-4)$ 接近零，$f(x)\approx x/2+1$；当 $x$ 很接近2时，$1/(2x-4)$ 绝对值极大，主导 $f$ 的行为。

**例18** 令 $f(x)=3x^4-2x^3+3x^2-5x+6$，$g(x)=3x^4$。证明当 $|x|$ 很大时，两者行为相近。

**解** 计算它们的比值：

$$\lim_{x\to\pm\infty}\frac{f(x)}{g(x)} = \lim_{x\to\pm\infty}\left(1-\frac{2}{3x}+\frac{1}{x^2}-\frac{5}{3x^3}+\frac{2}{x^4}\right) = 1.$$

当 $|x|$ 很大时 $f/g\to 1$，说明两者几乎相同（图2.67）。对于 $|x|$ 较小时，两者图像差异明显；对于 $|x|$ 较大时，图像几乎重合。

> **图2.67示意**
>
> (a) 小范围（$x\in[-2,2]$）坐标系：$f(x)$ 的图像（蓝色）与 $g(x)=3x^4$ 的图像（橙色）有明显差别，说明两者在 $|x|$ 小时不同。
> (b) 大范围（$x\in[-20,20]$）坐标系：两条曲线几乎重合，说明 $3x^4$ 在 $|x|$ 大时主导多项式 $f(x)$ 的行为。
