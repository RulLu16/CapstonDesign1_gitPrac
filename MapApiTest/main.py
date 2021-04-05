from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from pip._vendor import requests

url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=CE7&radius=350&y=37.550950&x=126.941017"
result = requests.get(urlparse(url).geturl(), headers={"Authorization": "KakaoAK 000000000000000000000000000"}) # 본인 api 키 입력
driver=webdriver.Chrome(executable_path=r'C:\Users\may05\PycharmProjects\chromedriver.exe') # 본인 크롬 드라이버 위치 입력
driver.implicitly_wait(3)

json_obj = result.json()
market_list = json_obj.get("documents")

for market in market_list:
    driver.get(market.get("place_url"))
    menu_list = driver.find_element_by_class_name("list_menu").find_elements_by_class_name("loss_word")
    # 에러 처리 안되어있어서 조금만 class name 바뀌면 에러남. 나중에 시간나면 고칠 예정
    for i in menu_list:
        print(i.text)
    print()
