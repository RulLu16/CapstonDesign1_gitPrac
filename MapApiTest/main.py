#-*- encoding: utf-8 -*

from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from playsound import playsound

from pip._vendor import requests

headers = {
    #Transfer-Encoding: chunked # 보내는 양을 모를 때 헤더에 포함
    'Host': 'kakaoi-newtone-openapi.kakao.com',
    'Content-Type': 'application/xml',
    'X-DSS-Service': 'DICTATION',
    'Authorization': f'KakaoAK 00000000000000000',
}

url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=CE7&radius=350&y=37.550950&x=126.941017"
result = requests.get(urlparse(url).geturl(), headers={"Authorization": "KakaoAK 00000000000000000"}) # 본인 api 키 입력
driver=webdriver.Chrome(executable_path=r'C:\Users\may05\PycharmProjects\chromedriver.exe') # 본인 크롬 드라이버 위치 입력
driver.implicitly_wait(3)

json_obj = result.json()
market_list = json_obj.get("documents")
idx = 1

for market in market_list:
    driver.get(market.get("place_url"))
    menu_list = driver.find_element_by_class_name("list_menu").find_elements_by_class_name("loss_word")
    # 에러 처리 안되어있어서 조금만 class name 바뀌면 에러남. 나중에 시간나면 고칠 예정
    for i in menu_list:
        data = "<speak>" + i.text + "</speak>"
        data = data.encode('utf-8')
        response = requests.post('https://kakaoi-newtone-openapi.kakao.com/v1/synthesize', headers=headers, data=data)
        voice = response.content

        with open(str(idx) + ".mp3", "wb+") as mp3:
            mp3.write(response.content)
        playsound(str(idx) + ".mp3")
        print(i.text)
        idx += 1
    #response = requests.post('https://kakaoi-newtone-openapi.kakao.com/v1/synthesize', headers=headers, data="<speak>가 있습니다.</speak>")
    print()
