import requests
from bs4 import BeautifulSoup #bs4 모듈안에 있는 BeautifulSoup를 불러옴.

resp = requests.get("https://search.naver.com/search.naver?query=강남구+날씨")
soup = BeautifulSoup(resp.text,"html.parser")

box = soup.find("section",{"class":"sc_new cs_weather _weather"})
local_name = box.find("span",{"class":"btn_select"}).find("em").text
temp = box.find("span",{"class":"todaytemp"}).text
content = box.find_all("p",{"class":"cast_txt"})[0].text

print(f"{local_name}의 날씨")
print(f"온도: {temp}℃")
print(content)c
