# RGB 与 HSV 颜色模型交互转换程序——程序简要说明

## 1. 编程语言

本程序使用 **Python 3.14.8** 编写。

程序核心的 RGB 与 HSV 颜色模型转换算法由程序自行实现，没有直接调用颜色转换库完成转换。

---

## 2. 开发环境

- 操作系统：Windows 11
- 编程语言：Python 3.14.8
- 开发工具：Visual Studio Code
- GUI 框架：Tkinter
- 版本管理：Git / GitHub
- 可执行程序打包工具：PyInstaller

程序开发过程中使用 Python 虚拟环境 `.venv` 管理项目运行环境。

---

## 3. 基本功能

本程序实现了 RGB 和 HSV 两种颜色模型下的交互式颜色选择，并能够实时进行 RGB 与 HSV 颜色值的双向转换。

主要功能如下：

1. **RGB 颜色选择**

   用户可以分别调节 Red、Green、Blue 三个颜色通道，取值范围均为 0～255。

2. **HSV 颜色选择**

   用户可以分别调节 Hue、Saturation、Value：

   - Hue：0°～359°
   - Saturation：0%～100%
   - Value：0%～100%

3. **RGB → HSV 转换**

   当 RGB 数值发生变化时，程序会自动计算对应的 HSV 数值，并同步更新 HSV 控件和颜色显示。

4. **HSV → RGB 转换**

   当 HSV 数值发生变化时，程序会自动计算对应的 RGB 数值，并同步更新 RGB 控件和颜色显示。

5. **实时颜色预览**

   用户改变 RGB 或 HSV 参数后，程序会实时显示当前颜色。

6. **Hue Spectrum 色相选择**

   用户可以通过 Hue Spectrum 色相条点击或拖动鼠标选择 Hue。

7. **Saturation × Value 二维颜色选择**

   程序提供二维颜色区域：

   - 水平方向表示 Saturation；
   - 垂直方向表示 Value。

   用户可以直接通过鼠标点击或拖动选择颜色。

8. **HEX 颜色值显示与复制**

   程序能够实时显示当前颜色对应的 HEX 值，并支持一键复制。

9. **其他辅助功能**

   - Random Color：随机生成颜色；
   - Reset：恢复初始颜色。

---

## 4. RGB 与 HSV 转换原理

### 4.1 RGB → HSV

首先将 RGB 的 0～255 数值归一化到 0～1。

计算：

```text
Cmax = max(R, G, B)
Cmin = min(R, G, B)
Δ = Cmax - Cmin
```

其中：

- V 由最大颜色分量 Cmax 决定；
- S 根据最大值与最小值之间的差值计算；
- H 根据 R、G、B 中哪个颜色分量为最大值进行分段计算。

最终得到 Hue、Saturation 和 Value。

### 4.2 HSV → RGB

首先根据 Hue 判断当前颜色所在的色相区间，然后计算：

```text
C = V × S

X = C × (1 - |(H / 60 mod 2) - 1|)

m = V - C
```

根据 Hue 所处的不同区间确定 RGB 三个通道的中间值，最后将结果转换到 0～255 范围，得到最终 RGB 数值。

---

## 5. 运行结果

### 5.1 程序主界面

程序提供 RGB、HSV 两种颜色模型的交互控制，并实时显示颜色预览。

![程序主界面](../screenshots/main-interface.png)

### 5.2 HSV 交互颜色选择

用户可以通过 Hue Spectrum 和 Saturation × Value 二维色板直接选择颜色，RGB 和 HSV 数值会同步变化。

![HSV交互颜色选择](../screenshots/hsv-picker.png)

### 5.3 RGB → HSV 转换示例

当：

```text
RGB = (255, 0, 0)
```

程序得到：

```text
HSV = (0°, 100%, 100%)
HEX = #FF0000
```

运行结果如下：

![RGB转HSV](../screenshots/rgb-to-hsv.png)

---

## 6. 程序运行方法

### 方法一：运行源程序

在项目根目录执行：

```bash
python src/main.py
```

### 方法二：运行可执行程序

直接双击：

```text
RGB-HSV-Color-Studio.exe
```

即可启动程序，无需通过 Visual Studio Code 运行。

---

## 7. 项目主要文件

```text
src/main.py
```

负责 GUI 界面、用户交互、颜色预览以及各控件之间的数据同步。

```text
src/color_converter.py
```

负责 RGB → HSV 和 HSV → RGB 的核心颜色模型转换算法。

```text
screenshots/
```

保存程序运行结果截图。

```text
RGB-HSV-Color-Studio.exe
```

Windows 可执行程序。