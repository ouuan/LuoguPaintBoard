from PIL import Image
import json
import sys

DataPath = "board.json"
Data2Path = "board2.json"

if len(sys.argv) < 4:
    print("ImageToData.py <ImagePath> <LeftTopX> <LeftTopY>")
    quit()

try:
    im = Image.open(sys.argv[1])
except:
    print('Open image ' + sys.argv[1] + ' failed.')
    quit()

if im.mode != "P":
    print("Index image required. Please read README.md for more information.")
    quit()

img_array = im.load()

try:
    with open(DataPath, 'r') as boardjson:
        board = json.load(boardjson)
except:
    board = []

w, h = im.size
for i in range(w):
    for j in range(h):
        board.append([i + int(sys.argv[2]), j + int(sys.argv[3]), img_array[i, j]])

board = json.dumps(board)
with open(DataPath, 'w+') as f:
    f.write(board)
with open(Data2Path, 'w+') as f:
    f.write("var board = " + board)

print("Finished.")
