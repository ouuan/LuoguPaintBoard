为什么需要组队？

即使是所画内容不一样的团队，合并后可以共同对抗外部势力，减少空闲 Cookies 带来的损失。因此，组队是一个合作双方共赢的经营模式。

组队 / 贡献个人 Cookies 请 QQ 联系 1609483441，可根据 Cookies 数量及想画的内容进行商谈。可以共享 Cookies，也可以共享数据，Cookies 由双方分别保管。

***

## 使用教程

### 准备环境

[python 3](https://www.python.org/downloads/)

[GIMP](https://www.gimp.org/downloads/) 或者 Photoshop2020

pillow：`python -m pip install pillow`

requests：`python -m pip install requests`

### 处理图像

于以下两项中选择一项

1. GIMP
   1. 将 `LuoguPaintBoard.gpl` 复制到 `GIMP安装路径\share\gimp\2.0\palettes`
   2. 用 GIMP 打开原始图片。
   3. 图像→缩放图像。
   4. 图像→模式→索引，Use custom palette：LuoguPaintBoard，**不要**勾选“从颜色表中移除无用和重复的颜色”。“递色”选项可以自己试试看哪种效果比较好。
   5. 文件→导出为→选一个路径→选择文件类型：**bmp** →导出。
2. PS
   1. 将`LuoguPaintBoard.irs` 复制到 `Photoshop2020安装路径\Presets\Optimized Settings`
   2. 用 Photoshop2020 打开原始图片
   3. 缩放图像
   4. <kbd>Ctrl+Shift+Alt+S</kbd>, 然后Preset选择LuoguPaintBoard, Dither自己看着办
   5. 导出为bmp即可

### 生成数据

1. `python .\ImageToData.py 图片路径 左上角X坐标 左上角Y坐标`
2. 打开 `preview.html` 检查数据生成是否有问题。

P.S. 如果需要画多张图，重复执行几次即可，`ImageToData.py` 不会覆盖原有数据，而会在后面添加。

### 填写 cookies

在 `cookies.json` 里按如下格式填写：

```
[
"cookies here",
"cookies here",
...
"cookies here"
]
```

### 开始画图

默认时间间隔为 10s（一轮 cookies），如有需要请自行修改 `src` 内源码的 `timeout` 。

#### rand

随机撒点。推荐只用来画图，请不要在维护图片时使用。

#### order

按照 `data\board.json` 中的顺序依次画。推荐使用 order 维护图片。

#### run

`runrand.bat`：无限循环随机撒点。

`runorder.bat`：按照顺序画图。

如果不通过 bat 使用 py，请注意路径问题（使用 bat 路径是 `cookies.json`、 `data/board.json`，使用 py 路径是 `../cookies.json`、`../data/board.json`）。

#### count

可以获取未完成的像素数量，并根据 cookies 的数量估算剩余时间。

在与他人抢地盘时估算的剩余时间是不准的，可以使用 `loopcount.bat` 监控剩余像素数并手动估算。

`runcount.bat`：数一次。

`loopcount.bat`：一直数。