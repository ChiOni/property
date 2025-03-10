from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def getWebDriver():
    chrome_driver_path = "crawler/chromedriver.exe"
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)
    options.add_argument("--disable-gpu")  # GPU 비활성화 (윈도우에서 필요)
    options.add_argument("--disable-dev-shm-usage")  # 메모리 공유 비활성화
    options.add_argument("--window-size=1920,1080")  # 창 크기 지정
    options.add_argument("--start-maximized")  # 창 최대화
    options.add_argument("--disable-extensions")  # 확장 프로그램 비활성화

    driver =  webdriver.Chrome(service=service, options=options)
    return driver
