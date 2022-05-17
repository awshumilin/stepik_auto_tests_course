from selenium import webdriver
import math
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("input_value")
    x = int(x1.text)
    result = math.log(abs(12 * math.sin(x)))

    outp = browser.find_element_by_id("answer")
    outp.send_keys(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    box = browser.find_element_by_id("robotCheckbox")
    box.click()

    rad = browser.find_element_by_id("robotsRule")
    rad.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()