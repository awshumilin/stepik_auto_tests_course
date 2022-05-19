import pytest
from selenium import webdriver
import time
import math

@pytest.fixture
def browser():
    browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_func(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    text_field = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    answer = math.log(int(time.time()))
    text_field.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    feedb = browser.find_element_by_css_selector("pre.smart-hints__hint")
    assert feedb.text == "Correct!", f"Text not correct, but {feedb.text}"