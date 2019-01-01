# LuoguPaintBoard

## Requirements

[python 3](https://www.python.org/downloads/)

[GIMP](https://www.gimp.org/downloads/)

pillow：`python -m pip install pillow`

requests：`python -m pip install requests`

## cookies.json

```
[
["cookies here"],
["cookies here"],
...
["cookies here"]
]
```

## board.json

```
[
[x,y,col],[x,y,col],...[x,y,col],
[x,y,col],[x,y,col],...[x,y,col],
...
[x,y,col],[x,y,col],...[x,y,col]
]
```

## rand.py

随机撒点，可修改timeout。请不要使用 `rand.py` 对已经画好的图片进行维护。

## order.py

按 `board.json` 中的顺序涂色，涂完后会循环到开头。推荐使用 `order.py` 对已经画好的图片进行维护。

## count.py

显示剩余像素数，并根据cookies数估算剩余时间。请注意，在跟其他人抢位置的时候估算是不准的。

## preview.html

预览效果。需要 `board2.json` 配合。

## board2.json

在 `board.json` 的最开头加上 `var board=`：

```
var board=[
[x,y,col],[x,y,col],...[x,y,col],
[x,y,col],[x,y,col],...[x,y,col],
...
[x,y,col],[x,y,col],...[x,y,col]
]
```

## runxxx.bat

便于使用py。并且无限循环，在发生异常时不会停止。

## runcount.bat

数一次。

## loopcount.bat

一直数。

## ImageToData.py

将索引图转化为数据。

使用方法：`python ImageToData.py 图片路径 左上角X坐标 左上角Y坐标`

生成的数据会在原 `board.json` 的基础上添加，并自动生成 `board2.json`。

索引图生成方法：

1. 将 `LuoguPaintBoard.gpl` 复制到 `GIMP安装路径\share\gimp\2.0\palettes`
2. 用 GIMP 打开原始图片。
3. 图像→缩放图像。
4. 图像→模式→索引，Use custom paletter：LuoguPaintBoard，**不要**勾选“从颜色表中移除无用和重复的颜色”。“递色”选项可以自己试试看哪种效果比较好。
5. 文件→导出为→选一个路径→选择文件类型：**bmp** →导出。