from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import os


setting = "//*[@id=\"root\"]/div/div/div/div[1]/div/div[3]/ul/li[12]"
setting_general = "//*[@id=\"/setting$Menu\"]/li[1]"
general_title = "//*[@id=\"root\"]/div/div/div/div[2]/div/span/span[1]/span"
backup_error = "/html/body/div[2]/div/span/div/div"
backup = "//*[@id=\"root\"]/div/div/div/div[1]/div/div[3]/ul/li[10]/a"

try:
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(current_path)
    service = Service(executable_path='{}/binaries/chromedriver'.format(current_path))
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Enable headless mode
    options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(service=service, options=options)
    #driver.implicitly_wait(10)

    driver.get("http://18.206.190.244")
    driver.maximize_window()

    driver.find_element(By.XPATH, setting).click()
    driver.find_element(By.XPATH, setting_general).click()
    assert driver.find_element(By.XPATH, general_title).text == "General"
    driver.save_screenshot('error_screenshot.png')
    time.sleep(5)
    
except WebDriverException as e:
    print(f"Error: {e}")
    driver.save_screenshot('error_screenshot.png')
   
finally:
    driver.quit()
