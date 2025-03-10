import time
import json
import pandas as pd
from driver import getWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

date   = datetime.today().strftime("%Y-%m-%d")
driver = getWebDriver()
with open("db/apt.json", "r", encoding="utf-8") as f:
    apt = json.load(f)

print("부동산 매물 현황 크롤링")
# 특정 아파트 조회로 이동 -> 동일매물 묶기
driver.get(f"https://new.land.naver.com/complexes/1000")
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="complexOverviewList"]/div[2]/div[1]/div[3]/div/label'))

data = []
for name, idxs in apt.items():
    for idx in idxs:
        driver.get(f"https://new.land.naver.com/complexes/{idx}")
        time.sleep(2)

        # 거래 유형 [매매]만 필터링
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//input[@id="complex_article_trad_type_filter_1"]'))
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "articleListArea")))
        article_list_html = driver.find_element(By.ID, "articleListArea").get_attribute("outerHTML")
        items = BeautifulSoup(article_list_html, "html.parser").select("#articleListArea > div")
        for item in items:
            dong  = item.select_one(".item_title .text").text.strip().split(" ")[-1]
            def price_convert(str_price):
                  num_price = (
                      int(str_price.split(" ")[0].replace("억","")) if len(str_price.split(" "))==1 else 
                      int(str_price.split(" ")[0].replace("억","")) + round(int(str_price.split(" ")[1].replace(",",""))*0.0001,1)
                  )
                  return num_price
            price = price_convert(item.select_one(".price_line .price").text.strip())
            size, floor, direction = item.select_one(".info_area .line .spec").text.strip().split(', ')
            if any([x in floor for x in ['저/','1/','2/']]): # 저층, 1층, 2층 제외
                continue
            data.append([date, name, dong, price, size, floor, direction])
    print(f'-- {name} 완료')

# pd.DataFrame(data, columns=["날짜", "이름", "동", "가격", "면적", "층수", "방향"]).to_csv("db/items.csv", index=False, encoding="utf-8-sig")

items = pd.concat([pd.read_csv("db/items.csv"), pd.DataFrame(data, columns=["날짜", "이름", "동", "가격", "면적", "층수", "방향"])])
items.to_csv("db/items.csv", index=False, encoding="utf-8-sig")