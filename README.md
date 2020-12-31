## 关于这个项目

**本项目已停止维护**，大约明年会写一个新的。你可以继续使用，但作者**不会回答问题、修复 bug、更新功能**。

1.  这个项目是我两年前写的，当时我，非常菜 :new_moon_with_face:
2.  这个项目是同步（sync）的，所以，Cookies 数量比较多（我之前用的时候大约是超过 30~40 个）时，即使把两次绘制的间隔时间调到 0 也无法充分利用每个 Cookie（即，一个 Cookie 的冷却时间已经到了，但还没轮到它）。
3.  我想写一个异步的工具。
4.  紧接着，我想：为什么不写一个把绘制绘板的各个流程集成到一起的工具呢？
5.  我想用 Electron 写。
6.  Electron 太难用了。
7.  我今年高三。

只不过我还是写了一个 [模拟洛谷冬日绘板服务器](https://github.com/ouuan/fake-luogu-paintboard-server)。

## 使用教程

### 准备环境

- [python 3](https://www.python.org/downloads/)

- [GIMP](https://www.gimp.org/downloads/) 或者 Photoshop

- pillow：`python -m pip install pillow`

- requests：`python -m pip install requests`

### 处理图像

于以下两项中选择一项：

#### GIMP

1. 将 `LuoguPaintBoard.gpl` 复制到 `GIMP安装路径\share\gimp\2.0\palettes`。

2. 用 GIMP 打开原始图片。

3. 图像 → 缩放图像。

4. 图像 → 模式 → 索引，Use custom palette：LuoguPaintBoard，**不要** 勾选“从颜色表中移除无用和重复的颜色”。“递色”选项可以自己试试看哪种效果比较好。

5. 文件 → 导出为 → 选一个路径 → 选择文件类型：**bmp** → 导出。
   
#### PS

1. 将`LuoguPaintBoard.irs` 复制到 `Photoshop安装路径\Presets\Optimized Settings`。

2. 用 Photoshop 打开原始图片。

3. 缩放图像。

4. <kbd>Ctrl+Shift+Alt+S</kbd>, 然后 Preset 选择 LuoguPaintBoard, Dither 自行选择。

5. 导出为 bmp 即可。

### 生成数据

请在 `data` 文件夹下生成数据。

1. `python ImageToData.py 图片路径 左上角X坐标 左上角Y坐标`，依次对每张图片运行（此脚本为增量更新）。

2. 打开 `preview.html` 检查数据生成是否有问题。

### 填写 cookies

在 `cookies.json` 里按如下格式填写：

```
[
	"_uid=xxxxx;__client_id=xxxxxxxxxxxxx",
	"_uid=xxxxx;__client_id=xxxxxxxxxxxxx",
	"_uid=xxxxx;__client_id=xxxxxxxxxxxxx"
]
```

### 运行脚本

`python paint.py <mode=order|rand|battle>`

三种模式分别为：

- order: 每次画需要画的点中在 `board.json` 里最靠前的一个。

- rand: 每次在需要画的点中随机选择。

- battle: 优先画最近被修改过的格子。

为防止出现未被捕获的异常，建议循环运行脚本。

### 常量设置

时间的单位均为秒。

- `WIDTH`：绘板宽度。
- `HEIGHT`：绘板高度。
- `COLORS`：颜色数量。
- `GETTIMEOUT`：单次读取绘板（GET 请求）用时上限。
- `POSTTIMEOUT`：单次画绘板（POST 请求）用时上限。
- `GETBOARDFREQ`：读取绘板间隔时间。
- `COOKIETIMEOUT`：一轮 Cookies 画完之后的等待时间。
- `PAINTBOARDURL`：绘板地址。
- `UA`：header 中使用的 User Agent。
