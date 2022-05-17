from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_id("input_value").text)
    result = math.log(abs(12 * math.sin(x)))

    browser.find_element_by_id("answer").send_keys(str(result))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
