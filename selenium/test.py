from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import os

URL = "http://http://34.229.61.21:30000/9/#/volume"
VOLUME_PAGE = "//*[@id=\"root\"]//li[6]/a"
VOLUME_NAME = "pvc-46569a7c-55c9-4863-af4d-d23d437849e0"

try:
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(current_path)
    service = Service(executable_path='{}/binaries/chromedriver'.format(current_path))
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Enable headless mode
    options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(30)

    driver.get(URL)
    #driver.maximize_window()
    time.sleep(5)
    #driver.find_element(By.XPATH, VOLUME_PAGE).click()
    table = driver.find_element(By.XPATH, "//*[@id=\"volumeTable\"]/div/div/div/div/div/div[1]/div[2]/table/tbody")
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            if cell.text == VOLUME_NAME:
                cell.click()
    """
    driver.find_element(By.XPATH, setting_general).click()
    assert driver.find_element(By.XPATH, general_title).text == "General"
    driver.save_screenshot('error_screenshot.png')
    time.sleep(5)
    """
except WebDriverException as e:
    print(f"Error: {e}")
    driver.save_screenshot('error_screenshot.png')
   
finally:
    driver.quit()
