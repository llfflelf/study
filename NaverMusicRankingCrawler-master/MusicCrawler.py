import os
import json
import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname('__File__')
print(BASE_DIR) # 기본 경로 출력

print("Start Crawling")
req = requests.get('https://music.bugs.co.kr/chart') # 페이지 접속
req.encoding = None # 한글이 깨지지 않도록 설정
html = req.content # html요소 모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # html 데이터 파싱
trs = soup.select('.list > tbody > tr')[:50] # 몇 번째까지 검색할 건지 수정

data = {} # 데이터 저장

for i, tr in enumerate(trs): # enumerate 사용으로 인덱스와 값을 모두 가져옴
    rank = i + 1
    name = tr.select_one('td.left > .artist > a').text # 가수 이름   # seletc_one 을 사용하여 각각의 값을 지정 ( 경로도 각각 지정)
    title = tr.select_one('th > .title > a').text # 노래 제목
    change = tr.select_one('td > div > p').text # 곡 순위 변경수치
    print(str(rank) + ". " + name+"," + title + "," + change ) # 데이터 값 출력
    data[rank] =  name+"," + title + "," + change # 데이터 값 저장

print("Crawling Complete")

# JSON 파일로 저장
if data:
    with open(os.path.join(BASE_DIR, 'musicRank.json'), 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent='\t')
        print("Save Complete") # 저장이 제대로 되었다면 출력
else:
    print("No data to save") # 저장이 제대로 되지 않았다면 출력

