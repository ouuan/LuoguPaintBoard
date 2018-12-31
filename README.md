# LuoguPaintBoard

## cookies.json

格式：

```
[
["cookies here"],
["cookies here"],
...
["cookies here"]
]
```

## board.json

格式：

```
[
[x,y,col],[x,y,col],...[x,y,col],
[x,y,col],[x,y,col],...[x,y,col],
...
[x,y,col],[x,y,col],...[x,y,col]
]
```

## rand.py

随机撒点，可修改timeout。

## order.py

按 `board.json` 中的顺序涂色，涂完后会循环到开头。

## count.py

显示剩余像素数，并根据cookies数估算剩余时间。

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