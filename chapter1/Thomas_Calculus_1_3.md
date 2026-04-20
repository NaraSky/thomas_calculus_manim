# 1.3 三角函数（Trigonometric Functions）

本节回顾弧度制与六个基本三角函数。

---

## 角的度量（Angles）

角可以用**度（degrees）**或**弧度（radians）**来度量。在半径为 $r$ 的圆中，圆心角 $A'CB'$ 所对应的弧度数，定义为该角所对弧长 $s$ 中包含的"半径单位"数。若用 $\theta$ 表示以弧度度量的圆心角，则：

$$\theta = \frac{s}{r}, \quad \text{即} \quad s = r\theta \quad (\theta \text{ 以弧度计}) \tag{1}$$

> **图示说明（图1.36）：** 左侧为半径为 $r$ 的圆，圆心角 $A'CB'$ 所对弧长为 $s$，弧度 $\theta = s/r$；右侧为单位圆（$r=1$），此时 $\theta$ 直接等于弧长 $AB$。两圆并列展示弧度定义。

若圆为单位圆（$r = 1$），则圆心角的弧度值就等于它所截取的弧长。由于单位圆一整圈为 $360°$ 或 $2\pi$ 弧度，故：

$$\pi \text{ 弧度} = 180°$$

$$1 \text{ 弧度} = \frac{180°}{\pi} \approx 57.3°, \qquad 1° = \frac{\pi}{180} \approx 0.017 \text{ 弧度}$$

部分常用角的度数与弧度换算见下表：

**表1.1 角的度数与弧度对照**

| 度数 | $-180°$ | $-135°$ | $-90°$ | $-45°$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ | $270°$ | $360°$ |
|------|---------|---------|--------|--------|------|-------|-------|-------|-------|--------|--------|--------|--------|--------|--------|
| 弧度 $\theta$ | $-\pi$ | $-\dfrac{3\pi}{4}$ | $-\dfrac{\pi}{2}$ | $-\dfrac{\pi}{4}$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |

---

## 标准位置角（Angles in Standard Position）

在 $xy$ 平面中，若一个角的顶点在原点，始边沿正 $x$ 轴方向，则称该角处于**标准位置**。逆时针旋转的角取正值，顺时针旋转的角取负值。

> **图示说明（图1.37）：** 两幅示意图：左图展示正值角（逆时针旋转），始边沿正 $x$ 轴，终边在第一象限；右图展示负值角（顺时针旋转），终边在第四象限。两图均标出始边和终边。

逆时针旋转的角可以超过 $2\pi$ 弧度，顺时针旋转的角可以取任意大小的负值。

> **图示说明（图1.38）：** 四幅示意图分别展示标准位置角 $\dfrac{9\pi}{4}$、$3\pi$、$-\dfrac{3\pi}{4}$、$-\dfrac{5\pi}{2}$ 的终边位置，说明弧度值可以超过 $2\pi$ 或为负值。

**角度约定：** 本书此后若无特别说明，所有角均以**弧度**为单位。

---

## 六个基本三角函数（The Six Basic Trigonometric Functions）

锐角的三角函数用直角三角形的三边定义。对于任意角（包括钝角和负角），将角置于标准位置，设终边与半径为 $r$ 的圆交于点 $P(x, y)$，则六个三角函数定义为：

$$\sin\theta = \frac{y}{r}, \qquad \csc\theta = \frac{r}{y}$$

$$\cos\theta = \frac{x}{r}, \qquad \sec\theta = \frac{r}{x}$$

$$\tan\theta = \frac{y}{x}, \qquad \cot\theta = \frac{x}{y}$$

> **图示说明（图1.39）：** 直角三角形示意图，标出斜边（hypotenuse）、邻边（adjacent）、对边（opposite）及角 $\theta$，并列出六个三角函数的直角三角形定义：$\sin\theta = \text{对}/\text{斜}$，$\cos\theta = \text{邻}/\text{斜}$，$\tan\theta = \text{对}/\text{邻}$，以及对应的倒数关系。

> **图示说明（图1.40）：** 坐标平面中，以原点为圆心、$r$ 为半径的圆，终边与圆交于点 $P(x,y)$，图中标出 $x$、$y$、$r$ 及角 $\theta$，对应一般角三角函数的坐标定义。

商关系与倒数关系：

$$\tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad \cot\theta = \frac{1}{\tan\theta}, \qquad \sec\theta = \frac{1}{\cos\theta}, \qquad \csc\theta = \frac{1}{\sin\theta}$$

当 $x = \cos\theta = 0$ 时，$\tan\theta$ 和 $\sec\theta$ 无定义（即 $\theta = \pm\dfrac{\pi}{2}, \pm\dfrac{3\pi}{2}, \ldots$）；当 $y = 0$ 时，$\cot\theta$ 和 $\csc\theta$ 无定义（即 $\theta = 0, \pm\pi, \pm 2\pi, \ldots$）。

---

## 特殊角的精确值

利用两个常用直角三角形可以得到特殊角的精确三角函数值：

> **图示说明（图1.41）：** 两个常用直角三角形：
> - 等腰直角三角形（两直角边均为 $1$，斜边为 $\sqrt{2}$，两锐角均为 $\pi/4$）；
> - $30°$-$60°$-$90°$ 三角形（短直角边为 $1$，长直角边为 $\sqrt{3}$，斜边为 $2$，角分别为 $\pi/6$、$\pi/3$、$\pi/2$）。

由此可得：

$$\sin\frac{\pi}{4} = \frac{1}{\sqrt{2}}, \quad \sin\frac{\pi}{6} = \frac{1}{2}, \quad \sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$$

$$\cos\frac{\pi}{4} = \frac{1}{\sqrt{2}}, \quad \cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}, \quad \cos\frac{\pi}{3} = \frac{1}{2}$$

$$\tan\frac{\pi}{4} = 1, \quad \tan\frac{\pi}{6} = \frac{1}{\sqrt{3}}, \quad \tan\frac{\pi}{3} = \sqrt{3}$$

---

## ASTC 法则

**ASTC 法则**（记忆口诀："All Students Take Calculus"）用于判断各象限中三角函数的正负：

> **图示说明（图1.42）：** 坐标平面被分为四个象限，各象限标注为：第一象限（A）所有三角函数为正；第二象限（S）仅正弦为正；第三象限（T）仅正切为正；第四象限（C）仅余弦为正。

**例：** 由图1.43中 $\dfrac{2\pi}{3}$ 所对应的参考三角形可得：

$$\sin\frac{2\pi}{3} = \frac{\sqrt{3}}{2}, \quad \cos\frac{2\pi}{3} = -\frac{1}{2}, \quad \tan\frac{2\pi}{3} = -\sqrt{3}$$

> **图示说明（图1.43）：** 单位圆中，角 $\dfrac{2\pi}{3}$ 的终边在第二象限，对应参考三角形两直角边分别为 $\dfrac{1}{2}$（水平）和 $\dfrac{\sqrt{3}}{2}$（竖直），点 $P$ 坐标为 $\left(-\dfrac{1}{2},\ \dfrac{\sqrt{3}}{2}\right)$。

**表1.2 部分角的 $\sin\theta$、$\cos\theta$、$\tan\theta$ 值**

| 度数 | $-180°$ | $-135°$ | $-90°$ | $-45°$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ | $270°$ | $360°$ |
|------|---------|---------|--------|--------|------|-------|-------|-------|-------|--------|--------|--------|--------|--------|--------|
| $\theta$（弧度） | $-\pi$ | $-\frac{3\pi}{4}$ | $-\frac{\pi}{2}$ | $-\frac{\pi}{4}$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
| $\sin\theta$ | $0$ | $-\frac{\sqrt{2}}{2}$ | $-1$ | $-\frac{\sqrt{2}}{2}$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ | $0$ |
| $\cos\theta$ | $-1$ | $-\frac{\sqrt{2}}{2}$ | $0$ | $\frac{\sqrt{2}}{2}$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-\frac{1}{2}$ | $-\frac{\sqrt{2}}{2}$ | $-\frac{\sqrt{3}}{2}$ | $-1$ | $0$ | $1$ |
| $\tan\theta$ | $0$ | $1$ | — | $-1$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | — | $-\sqrt{3}$ | $-1$ | $-\frac{\sqrt{3}}{3}$ | $0$ | — | $0$ |

（"—"表示无定义）

---

## 周期性与三角函数的图像（Periodicity and Graphs of the Trigonometric Functions）

当角 $\theta$ 与角 $\theta + 2\pi$ 处于标准位置时，它们的终边重合，因此所有三角函数值相同，称三角函数具有**周期性**。

> **定义** 若存在正数 $p$，使得对所有 $x$ 都有 $f(x + p) = f(x)$，则函数 $f(x)$ 是**周期函数（periodic function）**。满足此条件的最小正数 $p$ 称为函数的**周期（period）**。

### 六个三角函数的周期

**周期为 $\pi$：**

$$\tan(x + \pi) = \tan x, \qquad \cot(x + \pi) = \cot x$$

**周期为 $2\pi$：**

$$\sin(x + 2\pi) = \sin x, \quad \cos(x + 2\pi) = \cos x, \quad \sec(x + 2\pi) = \sec x, \quad \csc(x + 2\pi) = \csc x$$

### 奇偶性

**偶函数：**

$$\cos(-x) = \cos x, \qquad \sec(-x) = \sec x$$

**奇函数：**

$$\sin(-x) = -\sin x, \quad \tan(-x) = -\tan x, \quad \csc(-x) = -\csc x, \quad \cot(-x) = -\cot x$$

> **图示说明（图1.44）：** 六幅图分别展示六个基本三角函数的图像（横轴为 $x$，纵轴为 $y$）：
>
> - **(a) $y = \sin x$**：定义域 $(-\infty, +\infty)$，值域 $[-1, 1]$，周期 $2\pi$，关于原点对称的波形曲线，在 $x = 0, \pm\pi, \pm 2\pi, \ldots$ 处过零点。
>
> - **(b) $y = \cos x$**：定义域 $(-\infty, +\infty)$，值域 $[-1, 1]$，周期 $2\pi$，关于 $y$ 轴对称的波形曲线，在 $x = 0$ 时取最大值 $1$。
>
> - **(c) $y = \tan x$**：定义域 $x \neq \pm\dfrac{\pi}{2}, \pm\dfrac{3\pi}{2}, \ldots$，值域 $(-\infty, +\infty)$，周期 $\pi$，在每个周期内从 $-\infty$ 单调递增至 $+\infty$，有一系列垂直渐近线。
>
> - **(d) $y = \sec x$**：定义域 $x \neq \pm\dfrac{\pi}{2}, \pm\dfrac{3\pi}{2}, \ldots$，值域 $y \leq -1$ 或 $y \geq 1$，周期 $2\pi$，图像由一系列开口向上和向下的曲线弧构成，有垂直渐近线。
>
> - **(e) $y = \csc x$**：定义域 $x \neq 0, \pm\pi, \pm 2\pi, \ldots$，值域 $y \leq -1$ 或 $y \geq 1$，周期 $2\pi$，图像结构与 $\sec x$ 类似但相位不同。
>
> - **(f) $y = \cot x$**：定义域 $x \neq 0, \pm\pi, \pm 2\pi, \ldots$，值域 $(-\infty, +\infty)$，周期 $\pi$，在每个周期内从 $+\infty$ 单调递减至 $-\infty$，有一系列垂直渐近线。
>
> 每幅图中的阴影区域表示函数的一个完整周期。

---

## 三角恒等式（Trigonometric Identities）

平面上任意点 $P(x, y)$ 满足 $x = r\cos\theta$，$y = r\sin\theta$。当 $r = 1$ 时，由勾股定理得到最基本的三角恒等式：

$$\cos^2\theta + \sin^2\theta = 1 \tag{3}$$

> **图示说明（图1.45）：** 单位圆中，角 $\theta$ 的终边与圆交于点 $P(\cos\theta, \sin\theta)$，参考直角三角形的两直角边分别为 $|\cos\theta|$ 和 $|\sin\theta|$，斜边为 $1$，直观展示恒等式 $\cos^2\theta + \sin^2\theta = 1$ 的几何意义。

将式 $(3)$ 分别除以 $\cos^2\theta$ 和 $\sin^2\theta$，得到：

$$1 + \tan^2\theta = \sec^2\theta$$

$$1 + \cot^2\theta = \csc^2\theta$$

### 和角公式（Addition Formulas）

$$\cos(A + B) = \cos A\cos B - \sin A\sin B \tag{4a}$$

$$\sin(A + B) = \sin A\cos B + \cos A\sin B \tag{4b}$$

### 二倍角公式（Double-Angle Formulas）

将式 $(4)$ 中 $A = B = \theta$，得：

$$\cos 2\theta = \cos^2\theta - \sin^2\theta \tag{5a}$$

$$\sin 2\theta = 2\sin\theta\cos\theta \tag{5b}$$

### 半角公式（Half-Angle Formulas）

由 $\cos^2\theta + \sin^2\theta = 1$ 与 $\cos^2\theta - \sin^2\theta = \cos 2\theta$ 联立可得：

$$\cos^2\theta = \frac{1 + \cos 2\theta}{2} \tag{6}$$

$$\sin^2\theta = \frac{1 - \cos 2\theta}{2} \tag{7}$$

这两个公式在积分学中十分常用。

---

## 余弦定理（The Law of Cosines）

若三角形 $ABC$ 的三边为 $a, b, c$，$\theta$ 为 $c$ 边所对的角，则：

$$c^2 = a^2 + b^2 - 2ab\cos\theta \tag{8}$$

**证明：** 将三角形置于坐标系中，原点在 $C$，正 $x$ 轴沿一条边方向。则 $A$ 的坐标为 $(b, 0)$，$B$ 的坐标为 $(a\cos\theta,\ a\sin\theta)$。

> **图示说明（图1.46）：** 三角形 $ABC$ 置于坐标系中，$C$ 在原点，$A$ 在 $(b, 0)$，$B$ 在 $(a\cos\theta, a\sin\theta)$，标出三边 $a, b, c$ 及角 $\theta$，展示余弦定理的几何推导。

$A$ 与 $B$ 之间距离的平方为：

$$c^2 = (a\cos\theta - b)^2 + (a\sin\theta)^2 = a^2(\cos^2\theta + \sin^2\theta) + b^2 - 2ab\cos\theta = a^2 + b^2 - 2ab\cos\theta$$

余弦定理是勾股定理的推广：当 $\theta = \dfrac{\pi}{2}$ 时，$\cos\theta = 0$，得 $c^2 = a^2 + b^2$。

---

## 两个特殊不等式（Two Special Inequalities）

对任意以弧度度量的角 $\theta$，正弦和余弦函数满足：

$$-|\theta| \leq \sin\theta \leq |\theta| \qquad \text{以及} \qquad -|\theta| \leq 1 - \cos\theta \leq |\theta|$$

**推导：** 设 $\theta \neq 0$ 为标准位置角，单位圆上 $|\theta|$ 等于弧 $AP$ 的长度，故弦 $AP$ 的长度小于 $|\theta|$。

> **图示说明（图1.47）：** 单位圆中，$A = (1, 0)$，$P$ 为角 $\theta > 0$ 对应的单位圆上的点，$Q$ 为 $P$ 在 $x$ 轴上的投影，直角三角形 $APQ$ 的两直角边分别为 $|\sin\theta|$ 和 $1 - \cos\theta$。弧长 $AP = |\theta|$，弦长 $AP < |\theta|$，由勾股定理推出上述不等式。

三角形 $APQ$ 是直角三角形，两直角边为 $QP = |\sin\theta|$，$AQ = 1 - \cos\theta$，由勾股定理：

$$\sin^2\theta + (1 - \cos\theta)^2 = (AP)^2 \leq \theta^2 \tag{9}$$

左边两项均为非负数，各自小于其和，故：

$$\sin^2\theta \leq \theta^2 \quad \text{且} \quad (1-\cos\theta)^2 \leq \theta^2$$

取平方根即得：

$$|\sin\theta| \leq |\theta| \quad \text{且} \quad |1 - \cos\theta| \leq |\theta|$$

这两个不等式在下一章中会用到。

---

## 三角函数图像的变换（Transformations of Trigonometric Graphs）

1.2 节中的平移、拉伸、压缩和反射规则同样适用于三角函数。对于一般正弦函数（正弦型函数）：

$$f(x) = A\sin\!\left(\frac{2\pi}{B}(x - C)\right) + D$$

各参数的含义如下：

| 参数 | 含义 |
|------|------|
| $\|A\|$ | **振幅（amplitude）**：图像在中轴线上下的最大偏移量 |
| $\|B\|$ | **周期（period）**：函数完成一次完整振荡所需的 $x$ 的变化量 |
| $C$ | **水平位移（horizontal shift）**：图像沿 $x$ 轴方向的平移量 |
| $D$ | **垂直位移（vertical shift）**：中轴线 $y = D$ 相对于 $x$ 轴的偏移量 |

变换结构：

$$y = a\,f\!\left(b(x + c)\right) + d$$

其中：$a$ 控制垂直拉伸/压缩（若为负则关于 $y = d$ 反射）；$b$ 控制水平拉伸/压缩（若为负则关于 $x = -c$ 反射）；$c$ 控制水平平移；$d$ 控制垂直平移。

> **图示说明（正弦型函数图像示意图）：** 一条正弦型曲线，中轴线为水平线 $y = D$，振幅 $A$ 标注为曲线峰值 $D + A$ 与中轴线的距离，峰谷间的水平距离标注为一个完整周期 $B$，水平位移 $C$ 标注为曲线相对于原点的横向偏移，垂直位移 $D$ 标注为中轴线距 $x$ 轴的距离。
