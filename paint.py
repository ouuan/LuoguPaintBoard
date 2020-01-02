import requests
import random
import time
import json
import sys

WIDTH = 800
HEIGHT = 400
COLORS = 32
GETTIMEOUT = 5
POSTTIMEOUT = 5
GETBOARDFREQ = 20
COOKIETIMEOUT = 10
PAINTBOARDURL = "https://www.luogu.com.cn/paintBoard"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

if len(sys.argv) == 1 or not(sys.argv[1] in ['order', 'rand', 'battle']):
	print('python paint.py <mode=order|rand|battle>')
	quit()

mode = sys.argv[1]

with open('cookies.json', 'r') as cookiesjson:
	cookies = json.load(cookiesjson)

if len(cookies) == 0:
	print('No cookie found.')
	quit()

with open("data/board.json", 'r') as boardjson:
	board = json.load(boardjson)

if len(board) == 0:
	print('The plan is empty.')
	quit()

cur = 0
cnt = 0

now = [[2 for j in range(HEIGHT)] for i in range(WIDTH)]
old = [[2 for j in range(HEIGHT)] for i in range(WIDTH)]
lastChange = [[0 for j in range(HEIGHT)] for i in range(WIDTH)]

def getCookie():
	global cur, COOKIETIMEOUT
	cur = (cur + 1) % len(cookies)
	if cur == 0:
		time.sleep(COOKIETIMEOUT)
	return cookies[cur]

def paint(x, y, col):
	global cur, PAINTBOARDURL, UA, POSTTIMEOUT
	data = {
		'x': x,
		'y': y,
		'color': col
	}
	headers = {
		"refer": PAINTBOARDURL,
		"user-agent": UA,
		"cookie": getCookie()
	}
	try:
		response = requests.post(PAINTBOARDURL + "/paint", data = data, headers = headers, timeout = POSTTIMEOUT)
	except:
		print("POST error: ", cur)
		return -1
	try:
		if response.json()['status'] == 200:
			now[x][y] = col
			print(cur, x, y, col)
			return 0
		elif response.json()['status'] == 500:
			print(cur, response.json()['data'])
			return 1
		else:
			print(cur, response.json()['data'])
			return 2
	except:
		print(cur, response.text)
		return 3

lastGet = 0

def getBoard():
	global cnt, lastGet, HEIGHT, WIDTH, COLORS, PAINTBOARDURL, GETTIMEOUT
	lastGet = time.time()
	try:
		getheader = {
			"refer": PAINTBOARDURL,
			"user-agent": UA
		}
		response = requests.get(PAINTBOARDURL + "/board", headers = getheader, timeout = GETTIMEOUT)
	except:
		print("Get board failed.")
	else:
		try:
			cnt = cnt + 1
			for i in range(WIDTH):
				for j in range(HEIGHT):
					old[i][j] = now[i][j]
			res = response.text
			for i in range(WIDTH):
				for j in range(HEIGHT):
					now[i][j] = int(res[i * (HEIGHT + 1) + j], COLORS)
					if now[i][j] != old[i][j]:
						lastChange[i][j] = cnt
			remain = 0
			for i in board:
				if now[i[0]][i[1]] != i[2]:
					remain = remain + 1
			print('Remain: ', remain)
		except:
			print('Get response parse error.')

def chooseCell():
	if mode == 'order':
		for cell in board:
			x = cell[0]
			y = cell[1]
			if now[x][y] != cell[2]:
				return cell
		return random.choice(board)
	elif mode == 'rand':
		todolist = []
		for cell in board:
			x = cell[0]
			y = cell[1]
			if now[x][y] != cell[2]:
				todolist.append(cell)
		if len(todolist) == 0:
			return random.choice(board)
		return random.choice(todolist)
	elif mode == 'battle':
		mostRecentChanged = -1
		for cell in board:
			x = cell[0]
			y = cell[1]
			if now[x][y] != cell[2] and lastChange[x][y] > mostRecentChanged:
				mostRecentChanged = lastChange[x][y]
		if mostRecentChanged >= 0:
			print('Most recent changed: ' + str(mostRecentChanged))
		else:
			return random.choice(board)
		todolist = []
		for cell in board:
			x = cell[0]
			y = cell[1]
			if now[x][y] != cell[2] and lastChange[x][y] == mostRecentChanged:
				todolist.append(cell)
		return random.choice(todolist)

getBoard()

while True:
	if (time.time() - lastGet > GETBOARDFREQ):
		getBoard()
	cell = chooseCell()
	x = cell[0]
	y = cell[1]
	col = cell[2]
	if now[x][y] != col:
		while True:
			if paint(x, y, col) == 0:
				break
	elif time.time() - lastGet > 1:
		getBoard()
