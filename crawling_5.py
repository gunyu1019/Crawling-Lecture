import requests
from bs4 import BeautifulSoup #bs4 모듈안에 있는 BeautifulSoup를 불러옴.

resp = requests.get("https://search.naver.com/search.naver?query=용산구+날씨")
soup = BeautifulSoup(resp.text,"html.parser")

box = soup.select('section[class="sc_new cs_weather _weather"]')[0]
local_name = box.select('span[class="btn_select"] > em')[0]
temp = box.select('span[class="todaytemp"]')[0]
content = box.select('p[class="cast_txt"]')[0]

print(f"{local_name.get_text()}의 날씨")
print(f"온도: {temp.get_text()}℃")
print(content.get_text())
