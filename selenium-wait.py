import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

webdriver_path = 'C:\chromedriver\chromedriver.exe'
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome(webdriver_path)

    browser.get(link)

    # price = browser.find_element_by_id("price").text

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element_by_id("book").click()

    x1 = browser.find_element_by_id("input_value")
    x = int(x1.text)
    result = math.log(abs(12 * math.sin(x)))

    outp = browser.find_element_by_id("answer")
    outp.send_keys(str(result))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()



