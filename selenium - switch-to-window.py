from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id("input_value").text)
    result = math.log(abs(12 * math.sin(x)))

    browser.find_element_by_id("answer").send_keys(str(result))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()