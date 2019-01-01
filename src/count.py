import requests
import json

getheader={
        "refer":"https://www.luogu.org/paintBoard",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

with open("..\\data\\board.json",'r') as boardjson:
	board=json.load(boardjson)

tot=len(board)

response=requests.get("https://www.luogu.org/paintBoard/board",headers=getheader)
for i in board:
	x=i[0]
	y=i[1]
	col=i[2]
	if x*401+y<len(response.text) and int(response.text[x*401+y],32)==col:
		tot=tot-1
print(tot)
print(str(int(tot/(110*len(cookies))))+" hour(s) "+str(int(tot/(110*len(cookies))*60))+" minute(s)")
