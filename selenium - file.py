from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element_by_css_selector('[placeholder = "Enter first name"]')
    n1.send_keys("Alexander")

    n2 = browser.find_element_by_css_selector('[placeholder = "Enter last name"]')
    n2.send_keys("Ivanov")

    n3 = browser.find_element_by_css_selector('[placeholder = "Enter email"]')
    n3.send_keys("ivanov@mailru")

    f = browser.find_element_by_id("file")
    with open("file.txt", "w") as file:
        content = file.write("automationbypython")
    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_path = os.path.join(current_dir, 'file.txt')
    f.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()