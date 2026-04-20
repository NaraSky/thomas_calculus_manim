## 2.4 单侧极限

本节将极限概念推广到**单侧极限**——即 $x$ 仅从左侧（$x < c$）或仅从右侧（$x > c$）趋近于 $c$ 时的极限。单侧极限使我们能够描述在某点处左右行为不同的函数，也使我们能够在区间端点处讨论极限。

---

### 从一侧趋近极限

设函数 $f$ 在 $c$ 的两侧均有定义。$f$ 在 $x \to c$ 时有极限 $L$，要求 $f(x)$ 从两侧趋近 $c$ 时都趋近 $L$，因此这种极限有时称为**双侧极限**。

若 $f$ 在 $c$ 处不存在双侧极限，但仅从一侧趋近时有极限，则称之为**单侧极限**：从右侧趋近的极限称为**右极限**，从左侧趋近的称为**左极限**。

函数 $f(x) = x/|x|$（图2.24）在 $x \to 0^+$ 时极限为1，在 $x \to 0^-$ 时极限为 $-1$。由于两个单侧极限不相等，$f(x)$ 在0处不存在（双侧）极限。

> **图2.24示意**
>
> 坐标系中画有函数 $y = x/|x|$ 的图像：$x > 0$ 时函数值为1（水平线），$x < 0$ 时函数值为 $-1$（水平线），原点处函数无定义，两段图像均用实线表示，清晰显示左右极限不同。

若 $f(x)$ 在区间 $(c, b)$（$c < b$）上有定义，且当 $x$ 从右侧趋近 $c$ 时 $f(x)$ 任意接近 $L$，则 $f$ 在 $c$ 处有**右极限** $L$，记作

$$\lim_{x \to c^+} f(x) = L.$$

符号 "$x \to c^+$" 表示仅考虑 $x > c$ 时的函数值，不考虑 $x \leq c$ 时的情况。

类似地，若 $f(x)$ 在区间 $(a, c)$（$a < c$）上有定义，且当 $x$ 从左侧趋近 $c$ 时 $f(x)$ 任意接近 $M$，则 $f$ 在 $c$ 处有**左极限** $M$，记作

$$\lim_{x \to c^-} f(x) = M.$$

符号 "$x \to c^-$" 表示仅考虑 $x < c$ 时的函数值。

> **图2.25示意**
>
> 两个并排坐标系，分别说明右极限和左极限。
> (a) 右极限：$x$ 从右向左趋近 $c$（箭头向左），函数值 $f(x)$ 趋近 $L$（水平虚线），标注 $\displaystyle\lim_{x\to c^+} f(x) = L$。
> (b) 左极限：$x$ 从左向右趋近 $c$（箭头向右），函数值 $f(x)$ 趋近 $M$（水平虚线），标注 $\displaystyle\lim_{x\to c^-} f(x) = M$。

对函数 $f(x) = x/|x|$，有

$$\lim_{x \to 0^+} f(x) = 1 \quad \text{且} \quad \lim_{x \to 0^-} f(x) = -1.$$

---

现在给出函数在定义域边界点处极限的定义。当 $f$ 的定义域为 $c$ 左侧的区间（如 $(a, c]$ 或 $(a, c)$）时，$f$ 在 $c$ 处有极限当且仅当左极限存在；当定义域为 $c$ 右侧的区间（如 $[c, b)$ 或 $(c, b)$）时，$f$ 在 $c$ 处有极限当且仅当右极限存在。

**例1** 函数 $f(x) = \sqrt{4-x^2}$ 的定义域为 $[-2, 2]$，图像为上半圆（图2.26）。有

$$\lim_{x \to -2^+}\sqrt{4-x^2} = 0 \quad \text{且} \quad \lim_{x \to 2^-}\sqrt{4-x^2} = 0.$$

该函数在 $(-2, 2)$ 内每一点均有双侧极限；在 $x=2$ 处有左极限，在 $x=-2$ 处有右极限。由于 $f$ 在 $\pm 2$ 两侧均无定义，这两点不存在双侧极限。但在定义域边界点处，$f$ 确实有极限：

$$\lim_{x \to -2}\sqrt{4-x^2} = 0 \quad \text{且} \quad \lim_{x \to 2}\sqrt{4-x^2} = 0. \qquad $$

> **图2.26示意**
>
> 坐标系中画有上半圆 $y = \sqrt{4-x^2}$，两端点分别为 $(-2, 0)$ 和 $(2, 0)$（均为实心点），圆弧位于 $x$ 轴上方，说明函数在 $x = \pm 2$ 处有单侧极限0。

单侧极限具有2.2节定理1中列出的所有极限性质：两个函数之和的右极限等于各自右极限之和，等等。多项式和有理函数的极限定理，以及夹逼定理，对单侧极限同样成立。单侧极限与内点处极限的关系如下。

---

> **定理6** 设函数 $f$ 在包含 $c$ 的开区间上有定义（$c$ 点本身可能除外）。则 $f(x)$ 在 $x \to c$ 时有极限，当且仅当左极限和右极限均存在且相等：
>
> $$\lim_{x \to c} f(x) = L \quad \Longleftrightarrow \quad \lim_{x \to c^-} f(x) = L \quad \text{且} \quad \lim_{x \to c^+} f(x) = L.$$

---

**例2** 对图2.27所示函数，各点处的极限情况如下：

> **图2.27示意**
>
> 坐标系中画有定义在 $[0,4]$ 上的函数 $y=f(x)$，图像由若干段组成：$x=0$ 处从右侧开始，$x=1$ 处左右极限不相等（有跳跃），$x=2$ 处极限为1但函数值为2（空心圆在 $y=1$，实心点在 $y=2$），$x=3$ 处极限与函数值均为2，$x=4$ 处为右端点。

| 点 | 左极限 | 右极限 | 双侧极限 | 说明 |
|:-:|:-:|:-:|:-:|:-:|
| $x=0$ | 不存在 | $1$ | $1$ | $f$ 在 $x=0$ 左侧无定义；$x=0$ 为定义域端点 |
| $x=1$ | $0$ | $1$ | 不存在 | $f(1)=1$，但左右极限不相等 |
| $x=2$ | $1$ | $1$ | $1$ | $f(2)=2$，极限存在但不等于函数值 |
| $x=3$ | $2$ | $2$ | $2$ | $f(3)=2$，极限等于函数值 |
| $x=4$ | $1$ | 不存在 | $1$ | $f(4)\neq 1$；$f$ 在 $x=4$ 右侧无定义；$x=4$ 为定义域端点 |

在 $[0, 4]$ 内每一个其他点 $c$ 处，$f(x)$ 的极限均等于 $f(c)$。

定理6适用于函数定义域的内点；在边界点处，函数有极限当且仅当相应的单侧极限存在。

---

### 单侧极限的精确定义

2.3节极限的形式定义可以自然地修改为单侧极限。

---

> **定义**
>
> **(a)** 设 $f$ 的定义域包含 $c$ 右侧的区间 $(c, d)$。若对每个 $\varepsilon > 0$，存在 $\delta > 0$，使得
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad c < x < c + \delta,$$
>
> 则称 $f$ 在 $c$ 处的**右极限为 $L$**，记作 $\displaystyle\lim_{x \to c^+} f(x) = L$。
>
> **(b)** 设 $f$ 的定义域包含 $c$ 左侧的区间 $(b, c)$。若对每个 $\varepsilon > 0$，存在 $\delta > 0$，使得
>
> $$|f(x) - L| < \varepsilon \quad \text{当} \quad c - \delta < x < c,$$
>
> 则称 $f$ 在 $c$ 处的**左极限为 $L$**，记作 $\displaystyle\lim_{x \to c^-} f(x) = L$。

---

> **图2.28示意**
>
> 右极限定义的示意图：坐标系中，纵轴标注 $L-\varepsilon$ 和 $L+\varepsilon$，横轴标注 $c$ 和 $c+\delta$（仅右侧）。当 $x \in (c,\, c+\delta)$ 且 $x \neq c$ 时，$f(x)$ 落在 $\varepsilon$ 带内。
>
> **图2.29示意**
>
> 左极限定义的示意图：坐标系中，纵轴标注 $L-\varepsilon$ 和 $L+\varepsilon$，横轴标注 $c-\delta$ 和 $c$（仅左侧）。当 $x \in (c-\delta,\, c)$ 时，$f(x)$ 落在 $\varepsilon$ 带内。

**例3** 证明 $\displaystyle\lim_{x \to 0^+}\sqrt{x} = 0$。

**解** 给定 $\varepsilon > 0$，令 $c = 0$，$L = 0$，需找 $\delta > 0$ 使得

$$|\sqrt{x} - 0| < \varepsilon \quad \text{当} \quad 0 < x < \delta,$$

即

$$\sqrt{x} < \varepsilon \quad \text{当} \quad 0 < x < \delta. \quad (\sqrt{x} \geq 0 \text{ 时 } |\sqrt{x}| = \sqrt{x})$$

两边平方得：$x < \varepsilon^2$ 当 $0 < x < \delta$。取 $\delta = \varepsilon^2$，则

$$\sqrt{x} < \varepsilon \quad \text{当} \quad 0 < x < \delta = \varepsilon^2,$$

即 $|\sqrt{x} - 0| < \varepsilon$ 当 $0 < x < \varepsilon^2$。由定义，$\displaystyle\lim_{x \to 0^+}\sqrt{x} = 0$（图2.30）。

> **图2.30示意**
>
> 坐标系中画有 $f(x) = \sqrt{x}$ 的图像（从原点出发的上凸根号曲线）。纵轴标注 $\varepsilon$，横轴标注 $\delta = \varepsilon^2$，以及某点 $x$ 和对应的函数值 $f(x)$，说明当 $x < \delta$ 时 $f(x) < \varepsilon$。

**例4** 证明 $y = \sin(1/x)$ 在 $x$ 从任一侧趋近零时均无极限（图2.31）。

**解** 当 $x \to 0$ 时，$1/x$ 无界增大，$\sin(1/x)$ 的值在 $-1$ 到 $1$ 之间反复振荡，不趋近任何固定值 $L$。即使将 $x$ 限制为正值或负值，情况也相同。因此，函数在 $x=0$ 处既没有右极限，也没有左极限。

> **图2.31示意**
>
> 坐标系中画有函数 $y = \sin(1/x)$ 的图像：在 $x=0$ 附近，函数在 $-1$ 与 $1$ 之间无限振荡，振荡频率随 $|x|$ 减小而急剧加快，靠近纵轴处的振荡过于密集未予画出。

---

### 含 $(\sin\theta)/\theta$ 的极限

一个核心结论是：$(\sin\theta)/\theta$ 在弧度制下当 $\theta \to 0$ 时的极限为1。这可从图2.32直观看出，并可用夹逼定理严格验证。

> **图2.32示意**
>
> 坐标系中画有函数 $f(\theta) = (\sin\theta)/\theta$ 的图像：在 $\theta = 0$ 两侧，函数值均趋近1（纵截距处有空洞），在 $\theta = \pm\pi,\, \pm 2\pi,\, \pm 3\pi$ 处有零点，整体类似衰减振荡曲线，但在 $\theta=0$ 附近接近水平线 $y=1$。

---

> **定理7——$\sin\theta/\theta$ 在 $\theta \to 0$ 时的极限**
>
> $$\lim_{\theta \to 0}\frac{\sin\theta}{\theta} = 1 \quad (\theta \text{ 以弧度计}) \tag{1}$$

---

**证明** 思路：分别证明右极限和左极限均为1，再由定理6得双侧极限为1。

**右极限的证明：** 取 $0 < \theta < \pi/2$（图2.33）。注意到

$$\text{面积} \triangle OAP < \text{面积扇形} OAP < \text{面积} \triangle OAT.$$

用 $\theta$ 表示各面积：

$$\text{面积} \triangle OAP = \frac{1}{2} \cdot 1 \cdot \sin\theta = \frac{1}{2}\sin\theta$$

$$\text{面积扇形} OAP = \frac{1}{2}r^2\theta = \frac{1}{2}(1)^2\theta = \frac{\theta}{2} \tag{2}$$

$$\text{面积} \triangle OAT = \frac{1}{2} \cdot 1 \cdot \tan\theta = \frac{1}{2}\tan\theta$$

（注：扇形面积公式 $\theta/2$ 仅在 $\theta$ 以弧度计时成立。）

于是

$$\frac{1}{2}\sin\theta < \frac{1}{2}\theta < \frac{1}{2}\tan\theta.$$

> **图2.33示意**
>
> 单位圆坐标系，圆心 $O$，$A(1,0)$。圆上一点 $P$，对应弧度 $\theta$，$P$ 的坐标为 $(\cos\theta, \sin\theta)$；$Q$ 为 $P$ 在 $x$ 轴的投影，即 $(\cos\theta, 0)$；$T$ 为过 $A$ 的切线与 $OP$ 延长线的交点，$T$ 的纵坐标为 $\tan\theta$。图中标注三角形 $OAP$、扇形 $OAP$、三角形 $OAT$ 的关系，说明面积的大小次序。

各项除以正数 $\dfrac{1}{2}\sin\theta$（$0 < \theta < \pi/2$ 时为正）：

$$1 < \frac{\theta}{\sin\theta} < \frac{1}{\cos\theta}.$$

取倒数，不等号方向反转：

$$1 > \frac{\sin\theta}{\theta} > \cos\theta.$$

由 $\displaystyle\lim_{\theta\to 0^+}\cos\theta = 1$（2.2节例11b），夹逼定理给出

$$\lim_{\theta \to 0^+}\frac{\sin\theta}{\theta} = 1.$$

**左极限：** $\sin\theta$ 与 $\theta$ 均为奇函数，故 $f(\theta) = (\sin\theta)/\theta$ 为**偶函数**，图像关于 $y$ 轴对称（图2.32）。由对称性，左极限存在且与右极限相等：

$$\lim_{\theta \to 0^-}\frac{\sin\theta}{\theta} = 1 = \lim_{\theta \to 0^+}\frac{\sin\theta}{\theta}.$$

由定理6，$\displaystyle\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1$。

---

**例5** 证明：**(a)** $\displaystyle\lim_{y\to 0}\frac{\cos y - 1}{y} = 0$；**(b)** $\displaystyle\lim_{x\to 0}\frac{\sin 2x}{5x} = \dfrac{2}{5}$。

**解**

**(a)** 利用半角公式 $\cos y = 1 - 2\sin^2(y/2)$：

$$\lim_{y\to 0}\frac{\cos y - 1}{y} = \lim_{y\to 0}\frac{-2\sin^2(y/2)}{y}$$

$$= -\lim_{\theta\to 0}\frac{\sin\theta}{\theta}\cdot\sin\theta \quad \text{（令 }\theta = y/2\text{）}$$

$$= -(1)(0) = 0. \quad \text{（由式(1)及2.2节例11a）}$$

**(b)** 式(1)不能直接用于 $\dfrac{\sin 2x}{5x}$，因分母是 $5x$ 而非 $2x$。乘以 $\dfrac{2/5}{2/5}$：

$$\lim_{x\to 0}\frac{\sin 2x}{5x} = \lim_{x\to 0}\frac{(2/5)\cdot\sin 2x}{(2/5)\cdot 5x} = \frac{2}{5}\lim_{x\to 0}\frac{\sin 2x}{2x} \quad \text{（令 }\theta = 2x\text{，由式(1)）}$$

$$= \frac{2}{5}(1) = \frac{2}{5}. \qquad \blacksquare$$

---

**例6** 求 $\displaystyle\lim_{t\to 0}\frac{\tan t\sec 2t}{3t}$。

**解** 将 $\tan t$ 和 $\sec 2t$ 展开：

$$\lim_{t\to 0}\frac{\tan t\sec 2t}{3t} = \lim_{t\to 0}\frac{1}{3}\cdot\frac{1}{t}\cdot\frac{\sin t}{\cos t}\cdot\frac{1}{\cos 2t}$$

$$= \frac{1}{3}\lim_{t\to 0}\frac{\sin t}{t}\cdot\frac{1}{\cos t}\cdot\frac{1}{\cos 2t}$$

$$= \frac{1}{3}(1)(1)(1) = \frac{1}{3}. \quad \text{（由式(1)及2.2节例11b）} \qquad \blacksquare$$

---

**例7** 证明：对非零常数 $A$ 和 $B$，

$$\lim_{\theta\to 0}\frac{\sin A\theta}{\sin B\theta} = \frac{A}{B}.$$

**解** 同乘以 $A\theta$ 和 $B\theta$：

$$\lim_{\theta\to 0}\frac{\sin A\theta}{\sin B\theta} = \lim_{\theta\to 0}\frac{\sin A\theta}{A\theta}\cdot\frac{A\theta}{B\theta}\cdot\frac{B\theta}{\sin B\theta}$$

$$= \lim_{\theta\to 0}\frac{\sin A\theta}{A\theta}\cdot\frac{B\theta}{\sin B\theta}\cdot\frac{A}{B}$$

$$= (1)(1)\cdot\frac{A}{B} = \frac{A}{B}.$$

（第一个因子令 $u = A\theta$，由 $\displaystyle\lim_{u\to 0}\dfrac{\sin u}{u}=1$；第二个因子令 $v = B\theta$，由 $\displaystyle\lim_{v\to 0}\dfrac{v}{\sin v}=1$。）
